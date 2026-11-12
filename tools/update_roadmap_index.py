#!/usr/bin/env python3
"""Update bilingual index/changelog after generating the versioned roadmap."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
replacements=[
("README.md","## Research stages","## Full scientific and delivery roadmap\n\n[Detailed roadmap (English)](docs/en/roadmap.md) and [Persian roadmap](docs/fa/roadmap.md) track **35 packages linked to 39 earlier research tasks**, eight decision gates, twelve risks, reproducible acceptance criteria, and provisional effort. The shared [machine-readable plan](research/roadmap.json) generates both versions. This is E0 planning, not implementation.\n\n## Research stages"),
("README.fa.md","## مراحل پژوهش","## رودمپ تفصیلی علمی و اجرایی\n\n[رودمپ کامل فارسی](docs/fa/roadmap.md) و [نسخه انگلیسی](docs/en/roadmap.md) شامل **۳۵ بسته کاری مرتبط با ۳۹ اقدام قبلی**، هشت دروازه تصمیم، دوازده ریسک، خروجی‌ها، معیارهای پذیرش و برآورد منابع است. [مرجع ماشین‌خوان](research/roadmap.json) هر دو نسخه را تولید می‌کند. این برنامه E0 است، نه نتیجه اجرای DEC.\n\n## مراحل پژوهش"),
("CHANGELOG.md","## 0.1.0","## 0.2.0 — 2026-11-12\n\n- Detailed English/Persian roadmap: 35 work packages, mapped to 39 historical task identifiers, phased dependencies, provisional effort, outputs, acceptance tests, 8 gates and 12 risks.\n- Single bilingual JSON roadmap source, reproducible renderer and roadmap integrity validation in CI.\n- All cognitive experiments and implementation remain planned or deferred (E0).\n\n## 0.1.0"),
("CHANGELOG.fa.md","## 0.1.0","## 0.2.0 — ۲۰۲۶-۱۱-۱۲\n\n- افزودن رودمپ فارسی/انگلیسی با ۳۵ بسته کاری، نگاشت ۳۹ اقدام قبلی، پیش‌نیاز، برآورد، خروجی و معیار پذیرش و هشت گیت و دوازده ریسک.\n- منبع JSON واحد، تولیدکننده دوزبانه و کنترل ارتباط‌ها در CI.\n- تمام آزمایش‌ها هنوز برنامه‌ریزی‌شده یا معوق و دارای شواهد E0 هستند.\n\n## 0.1.0"),
(".github/workflows/docs-validation.yml","      - name: Validate public research dossiers","      - name: Verify generated bilingual roadmap matches JSON source\n        run: |\n          python tools/render_roadmap.py\n          git diff --exit-code -- docs/en/roadmap.md docs/fa/roadmap.md\n      - name: Validate public research dossiers"),
]
for name,needle,new in replacements:
    p=ROOT/name
    original=p.read_text(encoding="utf-8")
    if original.count(needle)!=1:
        raise RuntimeError(f"expected exactly one anchor in {name}, count={original.count(needle)}")
    p.write_text(original.replace(needle,new,1),encoding="utf-8",newline="\n")
    print(f"Updated {name}")
