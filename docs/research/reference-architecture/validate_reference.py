#!/usr/bin/env python3
"""Validate DEC-CRA v1 contracts and design provenance. Synthetic data only."""
from pathlib import Path
import json, copy, hashlib, sys
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parent
SCHEMA=json.loads((ROOT/'CONTRACTS.json').read_text())
Draft202012Validator.check_schema(SCHEMA)
validator=Draft202012Validator(SCHEMA,format_checker=FormatChecker())
BUDGET={"max_wall_ms":30000,"max_cpu_ms":20000,"max_peak_rss_mib":8192,"max_output_tokens":1500,"max_steps":8}
USAGE={"wall_ms":10,"cpu_ms":5,"peak_rss_mib":500,"output_tokens":10,"steps":1}
sha="0"*64
sample={
 "CaseRequest":{"case_id":"case:1","objective":"Analyze synthetic network change","language":"mixed","input_refs":["input:1"],"budget":BUDGET},
 "DecisionProposal":{"case_id":"case:1","decision_id":"dec:1","action":"retrieve","uncertainty":"estimated","reason_ref":"reason:1","confidence":0.6,"calibration_profile_id":"profile:1"},
 "Allocation":{"case_id":"case:1","allocation_id":"alloc:1","budget":BUDGET,"spent":USAGE,"status":"granted"},
 "ExpertInvocation":{"case_id":"case:1","invocation_id":"inv:1","expert_id":"security","model_id":"baseline","model_revision":"sha256:test","tokenizer_revision":"rev1","task_ref":"task:1","budget":BUDGET},
 "ExpertResult":{"case_id":"case:1","invocation_id":"inv:1","status":"success","result_refs":["result:1"],"usage":USAGE},
 "MemoryHandle":{"case_id":"case:1","handle_id":"mem:1","representation":"structured","compatibility_fingerprint":"sha256:test","lease_expiry_utc":"2026-11-17T00:00:00Z","permitted_operations":["read"]},
 "KnowledgeRequest":{"case_id":"case:1","query_ref":"query:1","collections":["synthetic"],"max_hits":5},
 "KnowledgeResult":{"case_id":"case:1","request_ref":"query:1","hits":[{"source_ref":"src:1","source_revision":"1","score":0.8}],"status":"success"},
 "ToolAction":{"case_id":"case:1","action_id":"action:1","tool_id":"calculator","parameters_ref":"params:1","authorization_context_ref":"auth:1","idempotency_key":"key:1"},
 "ToolReceipt":{"case_id":"case:1","action_id":"action:1","status":"succeeded","effect_refs":["effect:1"],"verified_by_ref":"verification:1"},
 "EvidenceEvent":{"event_id":"event:1","case_id":"case:1","trace_id":"trace:1","sequence":1,"timestamp_utc":"2026-11-16T14:00:00Z","event_type":"transition","previous_state":"PLANNED","new_state":"RUNNING","integrity_sha256":sha},
 "CaseResult":{"case_id":"case:1","trace_id":"trace:1","outcome":"completed","claim_refs":["claim:1"],"source_refs":["src:1"],"usage":USAGE}
}
def wrap(k,p):return {"schema_version":"1.0.0","kind":k,"payload":p}
def errors(k,p):return list(validator.iter_errors(wrap(k,p)))
positive={k:wrap(k,p) for k,p in sample.items()}
for k,p in sample.items():assert not errors(k,p), (k,errors(k,p)[0])
negative=[
 ("DecisionProposal",dict(sample["DecisionProposal"],action="invalid_action")),
 ("DecisionProposal",dict(sample["DecisionProposal"],confidence=1.5)),
 ("CaseRequest",dict(sample["CaseRequest"],budget=dict(BUDGET,max_steps=-1))),
 ("ToolAction",dict(sample["ToolAction"],authorization_context_ref="")),
 ("MemoryHandle",dict(sample["MemoryHandle"],representation="anything")),
 ("EvidenceEvent",dict(sample["EvidenceEvent"],integrity_sha256="broken")),
 ("CaseResult",dict(sample["CaseResult"],outcome="success")),
 ("ExpertInvocation",dict(sample["ExpertInvocation"],extra="disallowed"))
]
for k,p in negative:assert errors(k,p),("should reject",k,p)

# State machine is separate from JSON schema. Test both legal and prohibited transitions.
legal={
 "ACCEPTED":{"PLANNED"},
 "PLANNED":{"RUNNING"},
 "RUNNING":{"WAIT_EVIDENCE","VERIFYING","FAILED","INCONCLUSIVE"},
 "WAIT_EVIDENCE":{"RUNNING","FAILED","INCONCLUSIVE"},
 "VERIFYING":{"RUNNING","COMPLETED","FAILED","INCONCLUSIVE"},
 "COMPLETED":set(),"FAILED":set(),"INCONCLUSIVE":set()
}
def transition(a,b):return b in legal[a]
assert transition("ACCEPTED","PLANNED") and transition("VERIFYING","COMPLETED")
assert not transition("ACCEPTED","COMPLETED") and not transition("FAILED","RUNNING")
assert all("COMPLETED" not in allowed or state=="VERIFYING" for state,allowed in legal.items())

# Resource and compatibility invariants are explicit host/core logic—not implied by JSON Schema.
def within(used,limit):
 return all(used[k]<=limit[lk] for k,lk in [
 ("wall_ms","max_wall_ms"),("cpu_ms","max_cpu_ms"),("peak_rss_mib","max_peak_rss_mib"),("output_tokens","max_output_tokens"),("steps","max_steps")])
assert within(USAGE,BUDGET) and not within(dict(USAGE,steps=9),BUDGET)
def reuse_ok(handle,reference_fingerprint,now_utc):
 return handle["compatibility_fingerprint"]==reference_fingerprint and handle["lease_expiry_utc"]>now_utc
assert reuse_ok(sample["MemoryHandle"],"sha256:test","2026-11-16T14:00:00Z")
assert not reuse_ok(sample["MemoryHandle"],"sha256:other","2026-11-16T14:00:00Z")
assert not reuse_ok(sample["MemoryHandle"],"sha256:test","2026-11-18T14:00:00Z")

# Check all twelve requirements are explicitly addressed by at least one reference section.
alignment=json.loads((ROOT/'CAPABILITY_IDS.json').read_text())
arch=(ROOT/'DEC_CRA_REFERENCE_ARCHITECTURE_FA.md').read_text()
assert len(alignment['capabilities'])==12
for term in ["Decision Engine","Compute Allocator","Expert Manager","Memory Manager","Collaboration Engine","Verification","Tool Boundary","Unified","Ecosystem","Hybrid","RQ-01"]:
 assert term in arch,term
for name in ["VALIDATION_PLAN.md","ADR-002-REFERENCE-ARCHITECTURE.md"]:
 assert (ROOT/name).is_file()
(ROOT/'SYNTHETIC_CONTRACT_EXAMPLES.json').write_text(json.dumps(positive,ensure_ascii=False,indent=2)+"\n")
result={
 "schema":"dec-cra-qa-v1",
 "status":"PASS",
 "evidence":"E1 synthetic contract and invariant checks only; NOT end-to-end cognitive/model tests",
 "positive_contract_cases":len(positive),
 "negative_contract_cases":len(negative),
 "state_transitions_checked":4,
 "budget_assertions_checked":2,
 "memory_compatibility_checked":3,
 "aligned_capabilities":len(alignment['capabilities']),
 "checks":["JSON Schema 2020-12 valid","12 positive fixtures accepted","8 negative fixtures rejected",
           "state-machine transitions","budget ceilings","memory lease/fingerprint compatibility",
           "reference docs present","12 capability mapping present"]
}
(ROOT/'QA_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print("QA PASS",json.dumps(result,ensure_ascii=False))
