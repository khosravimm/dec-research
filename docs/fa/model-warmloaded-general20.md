---
doc_id: DEC-DOC-017
language: fa
title: "آزمون مجدد عمومی مدل‌ها؛ ۱۰ پرسش فارسی و ۱۰ پرسش انگلیسی پس از بارگذاری کامل"
version: 0.1.0
date: 2026-11-12
evidence_level: E1
publication_status: public-research-draft
---

# آزمون مجدد عمومی مدل‌ها؛ ۱۰ پرسش فارسی و ۱۰ پرسش انگلیسی پس از بارگذاری کامل

**نتیجه:** آزمایش قبلی دوپرسشی مبنای تصمیم نیست. در این جایگزین، هر یک از سه مدل دستورپذیر در ۲۰ مسئله عمومی و غیرتخصصی پاسخ داد. برای هر مدل، سرور اختصاصی یک بار مدل را به‌طور کامل بارگذاری کرد و پس از دریافت سلامت و اجرای Warm-up موفق، ۲۰ درخواست جداگانه ثبت شدند. **مدل پایه DEC انتخاب نشده است.**

## 1. پروتکل اجرا و محدودیت اعتبار

سؤالات قبل از اجرا در یک پرونده مستقل تثبیت شدند (SHA-256 در JSON). دو زبان هر کدام ده پرسش متناظر دارند و دسته‌ها شامل حساب ساده، زمان، فهم متن، منطق، دسته‌بندی روزمره، قالب خروجی، واژگان، ویرایش دستوری، خلاصه‌سازی و اقدام ساده روزمره است. هیچ سؤال تخصصی شبکه، امنیت، برنامه‌نویسی، پزشکی، حقوق یا مالی استفاده نشد. سرویس آزمایشگاهی جداگانه روی localhost اجرا و پس از آزمون بسته شد؛ مدل‌های سرویس‌دهنده دیگر و LDI تغییری نکردند. تنظیمات مشترک: ۴ Thread پردازشی، Context برابر ۲۰۴۸، Temperature صفر، Seed برابر ۴۲، سقف خروجی ۱۲۸ توکن، Thinking غیرفعال و یک درخواست همزمان. زمان هر پرسش از ارسال درخواست **پس از تکمیل بارگذاری و Warm-up** تا دریافت پاسخ اندازه‌گیری شد؛ زمان بارگذاری و Warm-up در زمان پاسخ درج نشده‌اند.

امتیاز **سخت‌گیرانه** فقط در صورت درستی معنا و رعایت قیدهای قالب (مثلاً «فقط نام») برابر یک است. امتیاز **محتوایی** خطای قالب را، اگر معنا درست باشد، جدا نشان می‌دهد. داوری این نسخه یک بررسی اولیه توسط دستیار است، نه داوری مستقل یا کور. به‌دلیل فقط یک نوبت اجرا، ده پرسش در هر زبان و تفاوت ظرفیت مدل‌ها، نتیجه رتبه‌بندی قطعی نیست. P95 با روش nearest-rank در نمونه ده‌تایی معادل بیشینه نمونه است.

## 2. نتیجه تجمیعی پاسخ‌ها

| مدل | صحیح فارسی | صحیح انگلیسی | صحیح کل | محتوایی فارسی/انگلیسی | میانه تأخیر فارسی/انگلیسی | اوج RAM فرایند |
|---|---:|---:|---:|---|---|---:|
| Qwen2.5-3B-Q4 | 3/10 | 10/10 | 13/20 | 3/10, 10/10 | 1633.7/968.5 ms | 3474.6 MB |
| MiniCPM5-1B-Q4 | 0/10 | 4/10 | 4/20 | 0/10, 6/10 | 5798.6/287.1 ms | 1209.8 MB |
| Qwen3.5-0.8B-Q4 | 4/10 | 7/10 | 11/20 | 4/10, 7/10 | 491.2/406.1 ms | 1724.3 MB |

| مدل | P95 فارسی | P95 انگلیسی | بارگذاری خارج از سنجش | Warm-up خارج از سنجش |
|---|---:|---:|---:|---:|
| Qwen2.5-3B-Q4 | 5625.1 ms | 3178.0 ms | 2018.4 ms | 817.8 ms |
| MiniCPM5-1B-Q4 | 6060.2 ms | 2275.4 ms | 1017.8 ms | 222.1 ms |
| Qwen3.5-0.8B-Q4 | 5763.3 ms | 1362.5 ms | 1004.1 ms | 214.4 ms |

## 3. ۲۰ سؤال و پاسخ مرجع از پیش تعیین‌شده

| شناسه | زبان | نوع | صورت سؤال | پاسخ مرجع |
|---|---|---|---|---|
| FA-01-ARITH | fa | حساب روزمره | پنج سبد داریم و در هر سبد چهار سیب است. اگر سه سیب برداریم، چند سیب باقی می‌ماند؟ فقط عدد را بنویس. | 17 |
| FA-02-TIME | fa | محاسبه زمان | اتوبوسی ساعت ۱۴:۳۵ حرکت می‌کند و ۵۰ دقیقه بعد می‌رسد. ساعت رسیدن چیست؟ فقط به شکل HH:MM جواب بده. | 15:25 |
| FA-03-READ | fa | فهم متن | سارا روز دوشنبه به کتابخانه رفت و روز سه‌شنبه به پارک رفت. سارا چه روزی به پارک رفت؟ فقط نام روز را بنویس. | سه‌شنبه |
| FA-04-ORDER | fa | استنتاج ساده | مینا از رضا کوتاه‌تر است و رضا از پویا کوتاه‌تر است. بلندترین فرد کیست؟ فقط نام را بنویس. | پویا |
| FA-05-CATEGORY | fa | طبقه‌بندی روزمره | از میان «سیب، موز، هویج، انگور» کدام مورد سبزی است؟ فقط نام آن را بنویس. | هویج |
| FA-06-FORMAT | fa | پیروی از قالب | بدون هیچ توضیح یا نشانه اضافی، دقیقاً این دو واژه را بنویس: روز خوش | روز خوش |
| FA-07-ANTONYM | fa | دانش واژگان | متضاد واژه «بلند» در معنی قد چیست؟ فقط یک واژه بنویس. | کوتاه |
| FA-08-GRAMMAR | fa | اصلاح جمله | این جمله را از نظر زمان فعل اصلاح کن؛ فقط جمله درست را بنویس: «من دیروز به مدرسه می‌روم.» | من دیروز به مدرسه رفتم. |
| FA-09-SUMMARY | fa | خلاصه‌سازی عمومی | ندا صبح نان خرید. سپس به خانه برگشت و همراه خانواده صبحانه خورد. این روایت را در یک جمله کوتاه خلاصه کن. | خرید نان و خوردن صبحانه با خانواده |
| FA-10-PRACTICAL | fa | استدلال روزمره | شیر آب آشپزخانه پس از شستن ظرف‌ها باز مانده است. برای جلوگیری از هدر رفتن آب، اولین کار ساده چیست؟ فقط یک جمله بگو. | بستن شیر آب |
| EN-01-ARITH | en | everyday arithmetic | We have five baskets with four apples in each. If three apples are taken away, how many apples remain? Answer with a number only. | 17 |
| EN-02-TIME | en | time calculation | A bus leaves at 14:35 and arrives 50 minutes later. At what time does it arrive? Reply only in HH:MM format. | 15:25 |
| EN-03-READ | en | reading comprehension | Sara went to the library on Monday and to the park on Tuesday. On which day did Sara visit the park? Give only the day name. | Tuesday |
| EN-04-ORDER | en | simple inference | Mina is shorter than Reza, and Reza is shorter than Pouya. Who is the tallest? Write only the name. | Pouya |
| EN-05-CATEGORY | en | everyday classification | Among apple, banana, carrot and grape, which is a vegetable? Write only its name. | carrot |
| EN-06-FORMAT | en | format compliance | Without any explanation or extra punctuation, write exactly these two words: Good day | Good day |
| EN-07-ANTONYM | en | vocabulary | What is the opposite of tall when describing a person's height? Write only one word. | short |
| EN-08-GRAMMAR | en | sentence correction | Correct the verb tense and return only the corrected sentence: 'Yesterday I go to school.' | Yesterday I went to school. |
| EN-09-SUMMARY | en | general summarization | Neda bought bread in the morning. Then she returned home and ate breakfast with her family. Summarize this in one short sentence. | buying bread and having breakfast with family |
| EN-10-PRACTICAL | en | everyday reasoning | The kitchen tap was left running after washing dishes. What is the first simple action to avoid wasting water? Answer in one sentence. | turn off the tap |

## 4. پاسخ‌های ثبت‌شده به تفکیک مدل

### Qwen2.5-3B-Q4

| شناسه | زبان | پاسخ مدل (خلاصه‌شده) | ارزیابی کامل | زمان پس از Warm-up |
|---|---|---|---|---:|
| FA-01-ARITH | fa | 7 | رد | 1265.6 ms |
| EN-01-ARITH | en | 17 | قبول | 931.5 ms |
| FA-02-TIME | fa | 19:35 | رد | 1827.8 ms |
| EN-02-TIME | en | 15:25 | قبول | 1427.1 ms |
| FA-03-READ | fa | سه‌شنبه | قبول | 1751.9 ms |
| EN-03-READ | en | Tuesday | قبول | 839.0 ms |
| FA-04-ORDER | fa | پویا | قبول | 1515.5 ms |
| EN-04-ORDER | en | Pouya | قبول | 1005.6 ms |
| FA-05-CATEGORY | fa | موز | رد | 1200.1 ms |
| EN-05-CATEGORY | en | Carrot | قبول | 800.7 ms |
| FA-06-FORMAT | fa | روز خوش | قبول | 1461.0 ms |
| EN-06-FORMAT | en | Good day | قبول | 729.9 ms |
| FA-07-ANTONYM | fa | متوسفة | رد | 1254.7 ms |
| EN-07-ANTONYM | en | short | قبول | 702.6 ms |
| FA-08-GRAMMAR | fa | «من امروز به مدرسه می‌روم.» | رد | 3054.8 ms |
| EN-08-GRAMMAR | en | Yesterday I went to school. | قبول | 1351.9 ms |
| FA-09-SUMMARY | fa | خرید ندا صبح، سپس به خانه با خانواده صبحانه کرد. | رد | 4708.2 ms |
| EN-09-SUMMARY | en | Neda bought bread in the morning and had breakfast with her family later. | قبول | 2551.4 ms |
| FA-10-PRACTICAL | fa | برای جلوگیری از هدر رفتن آب، ابتدا تمام ظرف‌ها را باز کنید. | رد | 5625.1 ms |
| EN-10-PRACTICAL | en | The first simple action to avoid wasting water is to turn off the kitchen tap after washing dishes. | قبول | 3178.0 ms |

### MiniCPM5-1B-Q4

| شناسه | زبان | پاسخ مدل (خلاصه‌شده) | ارزیابی کامل | زمان پس از Warm-up |
|---|---|---|---|---:|
| FA-01-ARITH | fa | من اولین نظر اشداری که یک نظری در خوادی است، یک نظری در خوادی است، یک نظری در خوادی است، یک نظری در خوادی است، یک نظری د | رد | 5950.8 ms |
| EN-01-ARITH | en | 40 | رد | 232.0 ms |
| FA-02-TIME | fa | ابلختی بندینین استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی ا | رد | 5930.7 ms |
| EN-02-TIME | en | 15:50 | رد | 332.3 ms |
| FA-03-READ | fa | سارا روز دوشنبه به کتابخانه رفت و روز سه‌شنبه به پارک رفت. سارا چه روزی به پارک رفت؟ فقط نام روز را بنویس. | رد | 4806.6 ms |
| EN-03-READ | en | Tuesday | قبول | 242.0 ms |
| FA-04-ORDER | fa | استخدم نظر در جواد در حالی در حصوبی است. | رد | 2233.7 ms |
| EN-04-ORDER | en | The problem states that Mina is shorter than Reza, and Reza is shorter than Pouya. This establishes a chain of height: Mina < Reza < Pouya. Therefore, Pouya is the tallest.  \boxed{Pouya} | رد | 2275.4 ms |
| FA-05-CATEGORY | fa | میان سبزی استثبیز یکی نام است، یکی نام استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبی | رد | 5847.0 ms |
| EN-05-CATEGORY | en | Grape | رد | 240.5 ms |
| FA-06-FORMAT | fa | بینیا یکی دو واژه در خوش در آنهایی در آنهایی استخانی در آنهایی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی ا | رد | 5823.4 ms |
| EN-06-FORMAT | en | Good day | قبول | 235.2 ms |
| FA-07-ANTONYM | fa | The phrase "متضاد واژه «بلند»" is a grammatical error. The correct term is "متضاد واژه" (meaning "Mr. and Mrs."), and the word "بلند" (meaning "big") is not part of the correct phrase. The phrase "بلند" is not used in this context.  The correct phrase is "متضا… | رد | 5773.8 ms |
| EN-07-ANTONYM | en | short | قبول | 220.0 ms |
| FA-08-GRAMMAR | fa | اب استخدم نظر در جمیری درستی داری. استخدم نظر در جمیری درستی داری. | رد | 3395.6 ms |
| EN-08-GRAMMAR | en | The corrected sentence is: **"Yesterday I went to school."** | رد | 771.1 ms |
| FA-09-SUMMARY | fa | ندا صبح نان خرید. سپس به خانه برگشت و همراه خانواده صبحانه خورد. این روایت را در یک جمله کوتاه خلاصه کن. | رد | 4680.8 ms |
| EN-09-SUMMARY | en | Neda bought bread in the morning, then returned home to eat it with her family. | رد | 945.3 ms |
| FA-10-PRACTICAL | fa | من در جواب یک جمله بگو کردهایی که یک جمله بگو است، است، یک جمله بگو است، یک جمله بگو است، یک جمله بگو است، یک جمله بگو است،  | رد | 6060.2 ms |
| EN-10-PRACTICAL | en | The first simple action to avoid wasting water is to turn off the tap while washing dishes. | قبول | 951.2 ms |

### Qwen3.5-0.8B-Q4

| شناسه | زبان | پاسخ مدل (خلاصه‌شده) | ارزیابی کامل | زمان پس از Warm-up |
|---|---|---|---|---:|
| FA-01-ARITH | fa | ۱۵ | رد | 499.8 ms |
| EN-01-ARITH | en | 10 | رد | 373.0 ms |
| FA-02-TIME | fa | ۱۷:۴۵ | رد | 775.9 ms |
| EN-02-TIME | en | 14:85 | رد | 560.6 ms |
| FA-03-READ | fa | سه‌شنبه | قبول | 482.6 ms |
| EN-03-READ | en | Tuesday | قبول | 345.5 ms |
| FA-04-ORDER | fa | پویا | قبول | 450.0 ms |
| EN-04-ORDER | en | Pouya | قبول | 439.1 ms |
| FA-05-CATEGORY | fa | سیب | رد | 399.7 ms |
| EN-05-CATEGORY | en | carrot | قبول | 353.8 ms |
| FA-06-FORMAT | fa | روز خوش | قبول | 361.8 ms |
| EN-06-FORMAT | en | Good day | قبول | 345.7 ms |
| FA-07-ANTONYM | fa | آب | رد | 373.9 ms |
| EN-07-ANTONYM | en | short | قبول | 283.6 ms |
| FA-08-GRAMMAR | fa | این جمله را به صورت صحیح می‌نویسید:  **«من دیروز به مدرسه می‌روم.»**  **توضیح:** در این جمله، فعل **می‌روم** به معنای «می‌رود» است. این فعل به دلیل اینکه در زمان فعل (Present Simple) به صورت **بی‌تغیرونی** (invariable) استفاده می‌شود، پس نیازی به تغییر شکل یا… | رد | 5763.3 ms |
| EN-08-GRAMMAR | en | Yesterday I go to school. | رد | 517.5 ms |
| FA-09-SUMMARY | fa | با خرید نان و رفتن به خانه، خانواده صبحانه را با هم خوردند. | قبول | 1178.3 ms |
| EN-09-SUMMARY | en | Neda bought bread, returned home, and then ate breakfast with her family. | قبول | 1030.2 ms |
| FA-10-PRACTICAL | fa | شیر آب را با آب شسته‌شده ظرف‌ها مخلوط کنید. | رد | 1260.5 ms |
| EN-10-PRACTICAL | en | Turn off the tap immediately after the dishes are washed to stop the water from dripping back into the sink. | قبول | 1362.5 ms |

## 5. محدودیت‌ها و تصمیم

تمام ۶۰ درخواست HTTP موفق بودند؛ موفقیت HTTP به معنای صحت پاسخ نیست. شش پاسخ فارسی MiniCPM5 به سقف ۱۲۸ توکن رسیدند. سقف خروجی، شیوه قالب‌گذاری گفتگو و انتخاب مدل کوانتیزه می‌توانند بر کیفیت اثر بگذارند؛ لذا افت مشاهده‌شده قابل تعمیم به تمام گونه‌های یک خانواده مدل نیست. نسخه LFM3-1.7B-Base در مقایسه امتیازی قرار نگرفت، زیرا مدل پایه پیش‌آموزش‌دیده است نه یک مدل دستورپذیر هم‌ارز. انتخاب مدل، آموزش LoRA، آزمون شورای DEC یا سنجش نهفته از این مجموعه استنتاج نمی‌شود.

داده کامل سؤال/پاسخ/امتیاز برای بازبینی مستقل و بازتولید:

- [پرونده JSON کامل سؤال‌ها، پاسخ‌ها و امتیازها](../../research/benchmarks/dec-general-warmloaded-fa-en-v1.json)
- [غربالگری قبلی دوپرسشی، نامعتبر برای تصمیم زبانی](model-preflight.md)
