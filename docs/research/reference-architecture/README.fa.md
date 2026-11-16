# معماری مرجع شناختی DEC — نسخهٔ ۱ (راهنمای فارسی)

این بخش شامل طراحی **مستقل از فناوری** برای پنج قابلیت شناختی DEC و مقایسهٔ مدل یکپارچه، اکوسیستم و معماری ترکیبی است. معادل‌های فارسی و انگلیسی باید از نظر دامنه، بخش‌ها، جداول و ادعاهای مبتنی بر شواهد هم‌ارز باشند؛ وجود نام فایل فارسی به‌تنهایی کافی نیست.

| موضوع | فارسی | انگلیسی |
|---|---|---|
| معماری کامل | [معماری مرجع](DEC_CRA_REFERENCE_ARCHITECTURE_FA.md) | [Full reference architecture](DEC_CRA_REFERENCE_ARCHITECTURE_EN.md) |
| برنامهٔ اعتبارسنجی | [برنامهٔ آزمون](VALIDATION_PLAN_FA.md) | [Validation plan](VALIDATION_PLAN.md) |
| تصمیم معماری | [ADR-002 فارسی](ADR-002-REFERENCE-ARCHITECTURE_FA.md) | [ADR-002 English](ADR-002-REFERENCE-ARCHITECTURE.md) |
| نمای کوتاه انگلیسی | — | [خلاصهٔ انگلیسی](REFERENCE_ARCHITECTURE_EN.md) |

**خروجی‌های مشترک ماشینی (ترجمه‌ناپذیر از نظر کلیدها):** [JSON Schema قراردادها](CONTRACTS.json)، [نمونه‌های مصنوعی](SYNTHETIC_CONTRACT_EXAMPLES.json)، [ردیابی نیازمندی‌ها](CAPABILITY_IDS.json)، [نتیجهٔ QA](QA_RESULTS.json) و [ابزار آزمون](validate_reference.py).

**روش اجرا:** Python 3 و بستهٔ `jsonschema>=4.18` لازم است. دستور `python3 validate_reference.py` اعتبار ساختار و نمونه‌های مصنوعی را بررسی می‌کند، **نه عملکرد واقعی مدل**.

در اسناد فارسی، نام مدل‌ها، Schema، نام فیلد، API، شناسه‌های پژوهشی و قطعات کد به همان شکل اصلی حفظ می‌شوند؛ شرح مفهومی، منطق تصمیم، جداول و عنوان‌ها باید فارسی باشند.
