---
doc_id: DEC-DOC-019
language: fa
title: "آزمون اولیه LFM3-1.7B و LFM2.5-1.2B-Thinking پس از بارگذاری کامل"
version: 0.1.0
date: 2026-11-12
evidence_level: E1
publication_status: public-research-draft
---

# آزمون اولیه LFM3-1.7B و LFM2.5-1.2B-Thinking پس از بارگذاری کامل

**نتیجه:** هر دو مدل رسمی Liquid AI با فایل GGUF دارای SHA-256 تأییدشده در محیط CPU بارگذاری، Warm-up و با همان ۱۰ سؤال عمومی فارسی و ۱۰ سؤال عمومی انگلیسی اجرا شدند. هر مدل ۲۰ پاسخ HTTP 200 داشت، اما **عملکرد پاسخ نهایی دو مدل قابل مقایسه هم‌ارز نیست** و هیچ مدل پایه DEC انتخاب نشده است.

## 1. روش و پیکربندی

برای هر وزن یک سرویس مجزای localhost با llama.cpp 0.9.0-dev، چهار Thread و یک درخواست همزمان راه‌اندازی و پس از آزمون بسته شد. پرسش‌ها از مجموعه ازپیش‌تثبیت‌شده قبلی با هش یکسان و بدون هیچ سؤال تخصصی، LDI یا استفاده از ابزار برداشته شدند. هر دو مدل پیش از شروع آزمون به‌طور کامل بارگذاری و با درخواست Warm-up آماده شدند. LFM3 با temperature=0.1، top_k=50، repetition_penalty=1.1، Thinking غیرفعال و ۱۲۸ توکن خروجی اجرا شد. LFM2.5-Thinking با temperature=0.05، top_k=50، repetition_penalty=1.05 و سقف ۵۱۲ توکن و Reasoning خودکار اجرا شد. توصیه تنظیمات از منابع رسمی اخذ شده است، اما قالب و Parser فعلی هنوز از نظر تطابق صددرصد تأیید نشده است.

## 2. نتایج عملیاتی، بدون امتیاز صحت

| مدل | زبان | HTTP 200 | پاسخ نهایی خالی | اتمام با سقف توکن | میانه زمان پس از Warm-up | تعداد کاراکتر بخش Reasoning |
|---|---|---:|---:|---:|---:|---:|
| LFM3-1.7B-Q4_K_M | fa | 10/10 | 0/10 | 3/10 | 4656.6 ms | 0 |
| LFM3-1.7B-Q4_K_M | en | 10/10 | 0/10 | 1/10 | 1361.5 ms | 0 |
| LFM2.5-1.2B-Thinking-Q4_K_M | fa | 10/10 | 9/10 | 9/10 | 25780.5 ms | 17460 |
| LFM2.5-1.2B-Thinking-Q4_K_M | en | 10/10 | 5/10 | 5/10 | 24306.0 ms | 18450 |

## 3. اهمیت تفکیک Thinking و پاسخ نهایی

در LFM2.5-Thinking، نه مورد فارسی و پنج مورد انگلیسی از ده سؤال هر زبان **فاقد پاسخ نهایی** بودند: سقف ۵۱۲ توکن پیش از پایان بخش استدلال مصرف شد. این موارد را نباید به‌عنوان پاسخ معنایی غلط امتیاز داد؛ آن‌ها خروجی نهایی قابل داوری ندارند. در LFM3 پاسخ نهایی خالی نبود، اما سه مورد فارسی و یک مورد انگلیسی با سقف ۱۲۸ توکن پایان یافتند و در برخی متن‌ها توکن پایان Thinking ظاهر شد، حتی با reasoning=off. این قرینه‌ای برای بررسی سازگاری Chat Template و Parser است.

### آزمون تکمیلی بودجه تفکر

در یک آزمون دوپرسشی جداگانه، پرچم reasoning-budget=128 همراه سقف ۳۸۴ توکن روی LFM2.5-Thinking آزمایش شد. خروجی انگلیسی طولانی بود و پاسخ فارسی باز هم با سقف خروجی تمام شد؛ پس صرف تعیین این بودجه، تضمین‌کننده پاسخ نهایی کوتاه نبود. این یک بررسی فنی محدود است و مبنای رتبه‌بندی زبان محسوب نمی‌شود.

## 4. خروجی‌های نهایی ثبت‌شده، به‌صورت خلاصه

| مدل | شناسه سؤال | پاسخ نهایی (حداکثر ۲۰۰ نویسه) | وضعیت پایان |
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

## 5. محدودیت‌ها و تصمیم بعدی

شواهد E1 فقط امکان اجرای مدل و مشاهده وضعیت خروجی را نشان می‌دهند. نبود پاسخ نهایی در Thinking به معنای ضعف قطعی زبان مدل نیست. مقایسه زمان با مدل‌های No-think و ۱۲۸توکنی منصفانه نیست؛ آزمون بعدی باید Budget کنترل‌شده Thinking، تنظیم Stop Tokens، Chat Template اصلی و پاسخ نهایی را جداگانه راستی‌آزمایی کند. ارزیابی Tool Calling، پیروی از دستور، کیفیت فارسی و انتخاب هسته به Gate مستقل نیاز دارد. مجوز LFM Open License v1.0 برای هر دو خانواده باید پیش از هر مشتق تجاری بررسی شود. وزن‌های شخص ثالث در GitHub منتشر نشده‌اند.

### Source links / منابع رسمی

- [Official LFM3-1.7B-GGUF model card](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF)
- [Official LFM2.5-1.2B-Thinking model card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)
- [Official llama.cpp reasoning budget and template options](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

- [داده ماشین‌خوان ۴۰ درخواست و شواهد نسخه و تنظیمات](../../research/benchmarks/dec-liquid-warmloaded-fa-en-v1.json)
