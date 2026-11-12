---
doc_id: DEC-DOC-019
language: en
title: "Post-load LFM3-1.7B and LFM2.5-1.2B-Thinking general bilingual screening"
version: 0.1.0
date: 2026-11-12
evidence_level: E1
publication_status: public-research-draft
---

# Post-load LFM3-1.7B and LFM2.5-1.2B-Thinking general bilingual screening

**Outcome:** Both official Liquid AI GGUF models were retrieved with verified full SHA256, fully loaded, explicitly warmed and run on the same ten Persian and ten English non-specialist questions. Each model produced 20 successful HTTP responses, but **valid final-answer completion differs sharply** and they must not be treated as equally scored DEC base models.

## 1. Method and settings

Each candidate ran in an isolated localhost llama.cpp 0.9.0-dev server with four CPU threads and one request at a time; services were closed afterward. The pre-frozen general question set was reused without specialist content, tool calls, or LDI access. Loading and a successful chat warm-up were completed before any measured question. LFM3 ran with temperature=0.1, top_k=50, repetition_penalty=1.1, thinking off and a 128-token answer cap. LFM2.5 Thinking ran with temperature=0.05, top_k=50, repetition_penalty=1.05, auto reasoning and a 512-token total completion cap. Settings derive from vendor model cards, but full template/parser compliance is not yet independently established.

## 2. Operational outcomes; no accuracy ranking

| Model | Language | HTTP 200 | Empty final answer | Length cap | Post-warmup median latency | Reasoning characters |
|---|---|---:|---:|---:|---:|---:|
| LFM3-1.7B-Q4_K_M | fa | 10/10 | 0/10 | 3/10 | 4656.6 ms | 0 |
| LFM3-1.7B-Q4_K_M | en | 10/10 | 0/10 | 1/10 | 1361.5 ms | 0 |
| LFM2.5-1.2B-Thinking-Q4_K_M | fa | 10/10 | 9/10 | 9/10 | 25780.5 ms | 17460 |
| LFM2.5-1.2B-Thinking-Q4_K_M | en | 10/10 | 5/10 | 5/10 | 24306.0 ms | 18450 |

## 3. Separating reasoning from final answers

For LFM2.5 Thinking, nine Persian and five English tasks out of ten per language had **no final-answer content**, because the 512-token completion budget was exhausted during reasoning. These are not independently judged wrong semantic answers; they were **ungradable final outputs** under this configuration. LFM3 produced nonempty content on all requests, but 3 Persian and 1 English requests hit the 128-token cap, and some raw end-of-thinking tags appeared in message content despite reasoning=off, warranting chat-template/parser review.

### Separate reasoning-budget diagnostic

A supplementary two-case LFM2.5 Thinking probe applied reasoning-budget=128 with max_tokens=384. The English output became long and the Persian task still hit the total cap, so merely limiting reasoning did not guarantee concise final answers. This tiny runtime diagnostic is not a language-performance benchmark.

## 4. Recorded final outputs, abbreviated

| Model | Case | Final output (200 chars max) | Finish reason |
|---|---|---|---|
| LFM3-1.7B-Q4_K_M | FA-01-ARITH | 3 Because each basket has 4 apples, and there are 5 baskets:   Total apples = 5 × 4 = 20.   If you take away 3 apples (not per basket but total), then remaining = 20 - 3 = 17? Wait, the question says … | length |
| LFM3-1.7B-Q4_K_M | EN-01-ARITH | We start with 5 baskets and each basket contains 4 apples.   Total apples = 5 × 4 = 20 apples.    Three apples are taken away: 20 - 3 = 17 apples remain.    Thus, the answer is 17.    17 | stop |
| LFM3-1.7B-Q4_K_M | FA-02-TIME | We need to find the arrival time of the bus if it departs at 14:35 and arrives 50 minutes later.  Add 50 minutes to 14:35:  - Current time: 14:35 - Add 50 minutes:   - From 14:35, adding 15 minutes ge… | length |
| LFM3-1.7B-Q4_K_M | EN-02-TIME | We need to find the arrival time when a bus leaves at 14:35 and arrives 50 minutes later.  Start time: 14:35  Add 50 minutes:  - From 14:35, add 15 minutes to get to 14:50. - Then we have 35 minutes l… | length |
| LFM3-1.7B-Q4_K_M | FA-03-READ | سه‌شنبه سارا روز سه‌شنبه به پارک رفت. | stop |
| LFM3-1.7B-Q4_K_M | EN-03-READ | Tuesday</think>Tuesday | stop |
| LFM3-1.7B-Q4_K_M | FA-04-ORDER | رضا  پویا  مناسب نیازی نیست که توضیح دهم؛ فقط نام بگو.   بلندترین فرد، طبق داده‌ها، **رضا کوتاه‌تر** است و **پویا کوتاه‌تر** است. اما سوال شما: **بلندترین فرد کیست؟**  این یک جزئیات تکمیلی نیست؛ بلندی… | length |
| LFM3-1.7B-Q4_K_M | EN-04-ORDER | Pouya  Since Pouya is taller than Reza, and Reza is taller than Mina, the order from tallest to shortest is Pouya > Reza > Mina. Thus, Pouya is the tallest.  \boxed{Pouya} | stop |
| LFM3-1.7B-Q4_K_M | FA-05-CATEGORY | هویج | stop |
| LFM3-1.7B-Q4_K_M | EN-05-CATEGORY | Carrot | stop |
| LFM3-1.7B-Q4_K_M | FA-06-FORMAT | روز خوش | stop |
| LFM3-1.7B-Q4_K_M | EN-06-FORMAT | Good day | stop |
| LFM3-1.7B-Q4_K_M | FA-07-ANTONYM | بلند (بِلَدُن) در زبان فارسی به معنای بلند، بلندگیر، بلندپایه یا بلندکننده است. | stop |
| LFM3-1.7B-Q4_K_M | EN-07-ANTONYM | short | stop |
| LFM3-1.7B-Q4_K_M | FA-08-GRAMMAR | «من دیروز به مدرسه می‌روم.» این جمله در زمینه زمان فعل صحیح است، زیرا عبارت «دیروز» نشان‌دهنده زمان گذشته (پشت‌گذاری) است و رفتن به مدرسه در یک رویداد گذشته بیان شده است. | stop |
| LFM3-1.7B-Q4_K_M | EN-08-GRAMMAR | Yesterday I went to school. | stop |
| LFM3-1.7B-Q4_K_M | FA-09-SUMMARY | نایض صبح نان خرید، به خانه برگشت و با خانواده صبحانه خورد.</think>نایض خرید نان، به خانه برگشت و صبحانه با خانواده خورد. | stop |
| LFM3-1.7B-Q4_K_M | EN-09-SUMMARY | Neda bought bread in the morning, then returned home to eat breakfast with her family. | stop |
| LFM3-1.7B-Q4_K_M | FA-10-PRACTICAL | اولین کار ساده این است که ظرف‌ها را بشویید و سپس لبه‌ها و پاورت‌ها را پاک کنید تا آب از داخل بیرون باز نماند. | stop |
| LFM3-1.7B-Q4_K_M | EN-10-PRACTICAL | To avoid wasting water, turn off the kitchen tap immediately when you finish washing dishes. | stop |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-01-ARITH |   8  \boxed{8} | stop |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-01-ARITH |   17  \boxed{17} | stop |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-02-TIME | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-02-TIME | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-03-READ | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-03-READ |   Tuesday    \boxed{Tuesday} | stop |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-04-ORDER | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-04-ORDER | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-05-CATEGORY | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-05-CATEGORY |   carrot   Wait, but let me make sure. The question lists apple, banana, carrot, grape. Among these, carrot is a vegetable (root vegetable), while the others are fruits. So the answer is carrot. Yeah,… | stop |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-06-FORMAT | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-06-FORMAT | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-07-ANTONYM | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-07-ANTONYM | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-08-GRAMMAR | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-08-GRAMMAR |   Yesterday I went to school. | stop |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-09-SUMMARY | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-09-SUMMARY | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | FA-10-PRACTICAL | (empty / خالی) | length |
| LFM2.5-1.2B-Thinking-Q4_K_M | EN-10-PRACTICAL |   Turn off the tap immediately after finishing dish washing to prevent water waste. | stop |

## 5. Validity bounds and next action

E1 only establishes local execution feasibility and limited final-output behavior. Missing final answers in a thinking model do not prove linguistic incapacity. Timings are not directly comparable with No-think 128-token runs. Next, explicitly validate reasoning budgets, template/stop-token handling and native HF output before acceptance; tools, instruction compliance, Persian proficiency and DEC architecture remain separate gates. Both Liquid AI model families are subject to the LFM Open License v1.0, which requires a proper commercial derivative review. No third-party weights are redistributed on GitHub.

### Source links / منابع رسمی

- [Official LFM3-1.7B-GGUF model card](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF)
- [Official LFM2.5-1.2B-Thinking model card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)
- [Official llama.cpp reasoning budget and template options](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

- [Machine-readable data for 40 requests and runtime settings](../../research/benchmarks/dec-liquid-warmloaded-fa-en-v1.json)
