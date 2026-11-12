---
doc_id: DEC-DOC-017
language: en
title: "Revised general-purpose model evaluation: 10 Persian and 10 English questions after full model load"
version: 0.1.0
date: 2026-11-12
evidence_level: E1
publication_status: public-research-draft
---

# Revised general-purpose model evaluation: 10 Persian and 10 English questions after full model load

**Outcome:** The preceding two-question screening is not an accepted decision basis. In this replacement, each of three instruction-following models answered 20 general, non-specialist questions. For each model an isolated server loaded the model once, returned healthy status, completed a warm-up chat request, and only then processed 20 independent questions. **No DEC backbone is selected.**

## 1. Execution protocol and validity bounds

The bilingual question set was frozen before execution (SHA-256 in JSON). Each language has ten parallel general-life tasks: arithmetic, time, comprehension, simple ordering, everyday classification, strict formatting, vocabulary, grammar, summarization and a practical household action. No specialist networking, cybersecurity, programming, medicine, law or finance questions were included. An isolated localhost inference server was started and stopped for each candidate, without changing production model services or LDI. Common settings: four CPU threads, context length 2048, temperature zero, seed 42, output cap 128 tokens, thinking disabled, and one parallel request. Each per-item time measures **only the post-load/post-warm-up request**, excluding model load and the explicit warm-up.

**Strict success** requires both correct meaning and adherence to explicit output-format constraints (e.g. 'name only'). **Semantic success** separately counts answers that are correct in meaning but violated formatting. Grading is a first-pass assistant review, not blind or independent adjudication. The single run, ten questions per language and different model sizes preclude any generalizable winner claim. Nearest-rank P95 with n=10 equals the observed maximum.

## 2. Aggregate answer results

| Model | Persian strict | English strict | Total strict | Semantic FA/EN | Median latency FA/EN | Peak process RSS |
|---|---:|---:|---:|---|---|---:|
| Qwen2.5-3B-Q4 | 3/10 | 10/10 | 13/20 | 3/10, 10/10 | 1633.7/968.5 ms | 3474.6 MB |
| MiniCPM5-1B-Q4 | 0/10 | 4/10 | 4/20 | 0/10, 6/10 | 5798.6/287.1 ms | 1209.8 MB |
| Qwen3.5-0.8B-Q4 | 4/10 | 7/10 | 11/20 | 4/10, 7/10 | 491.2/406.1 ms | 1724.3 MB |

| Model | P95 FA | P95 EN | Excluded preload | Excluded warmup |
|---|---:|---:|---:|---:|
| Qwen2.5-3B-Q4 | 5625.1 ms | 3178.0 ms | 2018.4 ms | 817.8 ms |
| MiniCPM5-1B-Q4 | 6060.2 ms | 2275.4 ms | 1017.8 ms | 222.1 ms |
| Qwen3.5-0.8B-Q4 | 5763.3 ms | 1362.5 ms | 1004.1 ms | 214.4 ms |

## 3. Frozen 20 general questions and reference answers

| ID | Language | Category | Question | Reference |
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

## 4. Recorded responses by model

### Qwen2.5-3B-Q4

| ID | Language | Model output (abbreviated) | Strict review | Post-warm-up latency |
|---|---|---|---|---:|
| FA-01-ARITH | fa | 7 | Fail | 1265.6 ms |
| EN-01-ARITH | en | 17 | Pass | 931.5 ms |
| FA-02-TIME | fa | 19:35 | Fail | 1827.8 ms |
| EN-02-TIME | en | 15:25 | Pass | 1427.1 ms |
| FA-03-READ | fa | سه‌شنبه | Pass | 1751.9 ms |
| EN-03-READ | en | Tuesday | Pass | 839.0 ms |
| FA-04-ORDER | fa | پویا | Pass | 1515.5 ms |
| EN-04-ORDER | en | Pouya | Pass | 1005.6 ms |
| FA-05-CATEGORY | fa | موز | Fail | 1200.1 ms |
| EN-05-CATEGORY | en | Carrot | Pass | 800.7 ms |
| FA-06-FORMAT | fa | روز خوش | Pass | 1461.0 ms |
| EN-06-FORMAT | en | Good day | Pass | 729.9 ms |
| FA-07-ANTONYM | fa | متوسفة | Fail | 1254.7 ms |
| EN-07-ANTONYM | en | short | Pass | 702.6 ms |
| FA-08-GRAMMAR | fa | «من امروز به مدرسه می‌روم.» | Fail | 3054.8 ms |
| EN-08-GRAMMAR | en | Yesterday I went to school. | Pass | 1351.9 ms |
| FA-09-SUMMARY | fa | خرید ندا صبح، سپس به خانه با خانواده صبحانه کرد. | Fail | 4708.2 ms |
| EN-09-SUMMARY | en | Neda bought bread in the morning and had breakfast with her family later. | Pass | 2551.4 ms |
| FA-10-PRACTICAL | fa | برای جلوگیری از هدر رفتن آب، ابتدا تمام ظرف‌ها را باز کنید. | Fail | 5625.1 ms |
| EN-10-PRACTICAL | en | The first simple action to avoid wasting water is to turn off the kitchen tap after washing dishes. | Pass | 3178.0 ms |

### MiniCPM5-1B-Q4

| ID | Language | Model output (abbreviated) | Strict review | Post-warm-up latency |
|---|---|---|---|---:|
| FA-01-ARITH | fa | من اولین نظر اشداری که یک نظری در خوادی است، یک نظری در خوادی است، یک نظری در خوادی است، یک نظری در خوادی است، یک نظری د | Fail | 5950.8 ms |
| EN-01-ARITH | en | 40 | Fail | 232.0 ms |
| FA-02-TIME | fa | ابلختی بندینین استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی ا | Fail | 5930.7 ms |
| EN-02-TIME | en | 15:50 | Fail | 332.3 ms |
| FA-03-READ | fa | سارا روز دوشنبه به کتابخانه رفت و روز سه‌شنبه به پارک رفت. سارا چه روزی به پارک رفت؟ فقط نام روز را بنویس. | Fail | 4806.6 ms |
| EN-03-READ | en | Tuesday | Pass | 242.0 ms |
| FA-04-ORDER | fa | استخدم نظر در جواد در حالی در حصوبی است. | Fail | 2233.7 ms |
| EN-04-ORDER | en | The problem states that Mina is shorter than Reza, and Reza is shorter than Pouya. This establishes a chain of height: Mina < Reza < Pouya. Therefore, Pouya is the tallest.  \boxed{Pouya} | Fail | 2275.4 ms |
| FA-05-CATEGORY | fa | میان سبزی استثبیز یکی نام است، یکی نام استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبیز استثبی | Fail | 5847.0 ms |
| EN-05-CATEGORY | en | Grape | Fail | 240.5 ms |
| FA-06-FORMAT | fa | بینیا یکی دو واژه در خوش در آنهایی در آنهایی استخانی در آنهایی استخانی استخانی استخانی استخانی استخانی استخانی استخانی استخانی ا | Fail | 5823.4 ms |
| EN-06-FORMAT | en | Good day | Pass | 235.2 ms |
| FA-07-ANTONYM | fa | The phrase "متضاد واژه «بلند»" is a grammatical error. The correct term is "متضاد واژه" (meaning "Mr. and Mrs."), and the word "بلند" (meaning "big") is not part of the correct phrase. The phrase "بلند" is not used in this context.  The correct phrase is "متضا… | Fail | 5773.8 ms |
| EN-07-ANTONYM | en | short | Pass | 220.0 ms |
| FA-08-GRAMMAR | fa | اب استخدم نظر در جمیری درستی داری. استخدم نظر در جمیری درستی داری. | Fail | 3395.6 ms |
| EN-08-GRAMMAR | en | The corrected sentence is: **"Yesterday I went to school."** | Fail | 771.1 ms |
| FA-09-SUMMARY | fa | ندا صبح نان خرید. سپس به خانه برگشت و همراه خانواده صبحانه خورد. این روایت را در یک جمله کوتاه خلاصه کن. | Fail | 4680.8 ms |
| EN-09-SUMMARY | en | Neda bought bread in the morning, then returned home to eat it with her family. | Fail | 945.3 ms |
| FA-10-PRACTICAL | fa | من در جواب یک جمله بگو کردهایی که یک جمله بگو است، است، یک جمله بگو است، یک جمله بگو است، یک جمله بگو است، یک جمله بگو است،  | Fail | 6060.2 ms |
| EN-10-PRACTICAL | en | The first simple action to avoid wasting water is to turn off the tap while washing dishes. | Pass | 951.2 ms |

### Qwen3.5-0.8B-Q4

| ID | Language | Model output (abbreviated) | Strict review | Post-warm-up latency |
|---|---|---|---|---:|
| FA-01-ARITH | fa | ۱۵ | Fail | 499.8 ms |
| EN-01-ARITH | en | 10 | Fail | 373.0 ms |
| FA-02-TIME | fa | ۱۷:۴۵ | Fail | 775.9 ms |
| EN-02-TIME | en | 14:85 | Fail | 560.6 ms |
| FA-03-READ | fa | سه‌شنبه | Pass | 482.6 ms |
| EN-03-READ | en | Tuesday | Pass | 345.5 ms |
| FA-04-ORDER | fa | پویا | Pass | 450.0 ms |
| EN-04-ORDER | en | Pouya | Pass | 439.1 ms |
| FA-05-CATEGORY | fa | سیب | Fail | 399.7 ms |
| EN-05-CATEGORY | en | carrot | Pass | 353.8 ms |
| FA-06-FORMAT | fa | روز خوش | Pass | 361.8 ms |
| EN-06-FORMAT | en | Good day | Pass | 345.7 ms |
| FA-07-ANTONYM | fa | آب | Fail | 373.9 ms |
| EN-07-ANTONYM | en | short | Pass | 283.6 ms |
| FA-08-GRAMMAR | fa | این جمله را به صورت صحیح می‌نویسید:  **«من دیروز به مدرسه می‌روم.»**  **توضیح:** در این جمله، فعل **می‌روم** به معنای «می‌رود» است. این فعل به دلیل اینکه در زمان فعل (Present Simple) به صورت **بی‌تغیرونی** (invariable) استفاده می‌شود، پس نیازی به تغییر شکل یا… | Fail | 5763.3 ms |
| EN-08-GRAMMAR | en | Yesterday I go to school. | Fail | 517.5 ms |
| FA-09-SUMMARY | fa | با خرید نان و رفتن به خانه، خانواده صبحانه را با هم خوردند. | Pass | 1178.3 ms |
| EN-09-SUMMARY | en | Neda bought bread, returned home, and then ate breakfast with her family. | Pass | 1030.2 ms |
| FA-10-PRACTICAL | fa | شیر آب را با آب شسته‌شده ظرف‌ها مخلوط کنید. | Fail | 1260.5 ms |
| EN-10-PRACTICAL | en | Turn off the tap immediately after the dishes are washed to stop the water from dripping back into the sink. | Pass | 1362.5 ms |

## 5. Limits and decision

All 60 requests returned HTTP success, but HTTP success is not answer correctness. Six MiniCPM5 Persian responses exhausted the 128-token budget. Output caps, chat-template behavior and quantized checkpoints can affect outcomes; observed weaknesses cannot be generalized to every variant of a model family. LFM3-1.7B-Base was not scored because a pretrained Base model is not an equivalent instruction-following candidate. No conclusion about backbone selection, LoRA learning, DEC council or latent communication follows from this test.

Full machine-readable questions, responses, and first-pass judgments:

- [Full JSON dataset and first-pass scores](../../research/benchmarks/dec-general-warmloaded-fa-en-v1.json)
- [Earlier E1 model-only screening, superseded for language decision](model-preflight.md)
