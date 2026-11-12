---
doc_id: DEC-DOC-020
language: fa
title: "ارزیابی صرفاً انگلیسی مدل‌ها: پیروی از دستور و فراخوانی واقعی ابزار"
version: 0.1.0
date: 2026-11-12
evidence_level: E1
publication_status: public-research-draft
---

# ارزیابی صرفاً انگلیسی مدل‌ها: پیروی از دستور و فراخوانی واقعی ابزار

**محدوده جدید به درخواست مالک:** تمام پرسش‌های فارسی از آزمون انتخاب مدل کنار گذاشته شده‌اند. پنج مدل روی مجموعه ثابت **۱۲ سؤال عمومی انگلیسیِ پیروی از دستور + ۱۲ سناریوی انگلیسی Tool Calling**، پس از بارگذاری کامل و Warm-up، بررسی شده‌اند. ابزارها واقعی از نظر پروتکل و اجرای تابع بوده‌اند، اما داده آن‌ها **کاملاً مصنوعی** بوده است. هیچ مدل نهایی DEC انتخاب نشده است.

## 1. پروتکل اجرا و کنترل شرایط

وزن‌های GGUF با SHA-256 تأیید شده‌اند. هر مدل در یک سرور محلی جداگانه با llama.cpp نسخه 0.9.0-dev، با Context برابر 4096، چهار Thread و یک درخواست همزمان بارگذاری شد. پس از پاسخ سلامت و Warm-up موفق، سؤال‌ها فرستاده شدند. LFM3 ابتدا به‌تنهایی اجرا شد و چهار مدل دیگر همزمان روی Portهای جداگانه و با Nice پایین‌تر اجرا شدند؛ **بنابراین مقایسه زمانی بین مدل‌ها معتبر نیست**. تنظیمات Sampling سازگار با هر مدل در فایل JSON ثبت شده‌اند. هیچ داده LDI، سرویس عملیاتی یا ابزار خارجی واقعی استفاده نشده است.

## 2. معیار دقیق Tool Calling

برای موفقیت Tool Calling صرف تولید JSON، XML یا توضیح درباره ابزار کافی نیست: باید فیلد ساختاریافته API با نام `tool_calls` ایجاد شود؛ نام ابزار، تعداد فراخوانی‌ها و **تمام آرگومان‌های نوع‌دار** با قرارداد سناریو تطبیق کنند؛ Harness تابع مصنوعی را اجرا و نتیجه را با نقش `tool` به مدل بازگرداند؛ مدل نیز پاسخ نهایی مطابق داده ابزار بسازد. دو آزمون منفی نیز برای سنجش **عدم فراخوانی ابزار در زمان غیرضروری** وجود دارند.

## 3. نتایج تجمیعی

| مدل | رعایت دقیق دستور | ابزار (امتیاز اولیه) | ابزار (بازبینی معیار) | ۱۰ سناریوی نیازمند ابزار | ۲ سناریوی بدون ابزار | کل از ۲۴ |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-3B-Q4 | 11/12 | 11/12 | 11/12 | 10/10 | 1/2 | 22/24 |
| MiniCPM5-1B-Q4 | 8/12 | 8/12 | 9/12 | 8/10 | 1/2 | 17/24 |
| Qwen3.5-0.8B-Q4 | 9/12 | 9/12 | 9/12 | 9/10 | 0/2 | 18/24 |
| LFM3-1.7B-Q4 | 9/12 | 11/12 | 11/12 | 10/10 | 1/2 | 20/24 |
| LFM2.5-1.2B-Thinking-Q4 | 6/12 | 9/12 | 9/12 | 9/10 | 0/2 | 15/24 |

پس از بازبینی خروجی‌ها مشخص شد نسخه اولیه Harness، تکرار **نام شهر، کالا یا شناسه سفارش** را در متن نهایی الزام کرده بود، در حالی که خود درخواست فقط دما، مقدار موجودی یا وضعیت را می‌خواست. در نسخه `v1.1` این الزام غیرضروری فقط از معیار صحت پاسخ نهایی حذف شده است؛ **سؤالات، خروجی مدل‌ها، انتخاب ابزار و اعتبار آرگومان‌ها تغییر نکرده‌اند**. هر دو امتیاز اولیه و بازبینی‌شده حفظ شده‌اند. چون اصلاح معیار پس از مشاهده پاسخ‌ها انجام شده، این نتیجه نباید آزمون کور یا از پیش ثبت‌شده قلمداد شود.

## 4. جزئیات پرسش‌ها و پاسخ‌های مرجع

| شناسه | نوع | دستور یا سؤال انگلیسی | مرجع یا ابزار مورد انتظار |
|---|---|---|---|
| I01 | instruction | Reply with exactly these two words, without punctuation: Good morning | Good morning |
| I02 | instruction | There are 6 boxes holding 4 pens each. Three pens are removed. Give only the remaining number. | 21 |
| I03 | instruction | A train leaves at 09:45 and arrives 35 minutes later. Reply with the arrival time only in HH:MM 24-hour format. | 10:20 |
| I04 | instruction | Nora visited the library on Monday and the museum on Friday. On which day did she visit the museum? Give only the weekday. | Friday |
| I05 | instruction | Ada is older than Ben. Ben is older than Cal. Who is youngest? Give just the name. | Cal |
| I06 | instruction | From piano, violin, carrot and flute, choose the vegetable. Return one lowercase word. | carrot |
| I07 | instruction | Return valid JSON only, with exactly two keys in this order: "color" set to "blue", and "count" set to the integer 3. No markdown. | {'color': 'blue', 'count': 3} |
| I08 | instruction | Convert 'quiet river' to uppercase. Output only the transformed text. | QUIET RIVER |
| I09 | instruction | Correct the grammar and return only the corrected sentence: 'Yesterday she go to the park.' | Yesterday she went to the park. |
| I10 | instruction | Sort these words alphabetically. Return a comma-separated list and nothing else: pear, apple, banana | apple, banana, pear |
| I11 | instruction | Write exactly three lowercase words, separated by single spaces, naming the three primary colors of light in this order: red then green then blue. | red green blue |
| I12 | instruction | Reply on one line only. Write the exact string 'OK-17' with no extra spaces, quotes or explanation. | OK-17 |
| T01 | tool | Use the available weather tool to check the simulated current weather in Oslo. Report the condition and temperature in one sentence. | [{'name': 'get_city_weather', 'args': {'city': 'Oslo'}}] |
| T02 | tool | Use the inventory tool to check whether the simulated store has blue notebook units in stock. Report the quantity. | [{'name': 'get_store_stock', 'args': {'item': 'blue notebook'}}] |
| T03 | tool | Check the simulated delivery status of order ORD-104 using the order tool. Give the status and delivery weekday. | [{'name': 'lookup_delivery', 'args': {'order_id': 'ORD-104'}}] |
| T04 | tool | Use the total calculator tool to calculate the price for seven items costing 6 currency units each. Return the total. | [{'name': 'calculate_total', 'args': {'unit_price': 6, 'quantity': 7}}] |
| T05 | tool | Use the conversion tool to convert 3 kilograms to grams. State the numerical result and unit. | [{'name': 'convert_units', 'args': {'value': 3, 'from_unit': 'kg', 'to_unit': 'g'}}] |
| T06 | tool | Use the available weather tool to check the simulated current weather in Amsterdam. Report the condition and temperature. | [{'name': 'get_city_weather', 'args': {'city': 'Amsterdam'}}] |
| T07 | tool | Look up the simulated store inventory for red mug using the stock tool. Tell me if it is available. | [{'name': 'get_store_stock', 'args': {'item': 'red mug'}}] |
| T08 | tool | Use the delivery tool to check simulated order ORD-220. Report its status and expected arrival weekday. | [{'name': 'lookup_delivery', 'args': {'order_id': 'ORD-220'}}] |
| T09 | tool | Without using any tools, reply with exactly these words: No lookup required |  |
| T10 | tool | Do not use tools. Write the word 'orange' backwards, lowercase, with no punctuation. |  |
| T11 | tool | The simulated shop sells a blue notebook for 4.5 currency units. Use the tools to check inventory and calculate the total for 3 notebooks. Tell me how many are in stock and the price for 3. | [{'name': 'get_store_stock', 'args': {'item': 'blue notebook'}}, {'name': 'calculate_total', 'args': {'unit_price': 4.5, 'quantity': 3}}] |
| T12 | tool | Use the weather tool for both Oslo and Amsterdam in this simulated dataset. Compare their temperatures and say which city is colder. | [{'name': 'get_city_weather', 'args': {'city': 'Oslo'}}, {'name': 'get_city_weather', 'args': {'city': 'Amsterdam'}}] |

## 5. نتایج هر سؤال به تفکیک مدل

### Qwen2.5-3B-Q4

**Weight SHA-256:** `5ee4f07cdb9beadbbb293e85803c569b01bd37ed059d2715faa7bb405f31caa6`
**Raw evidence SHA-256:** `09b62005b54d4dd51fd8bb4016d69d8b31a32eb433bfd1ad46657861e46664e9`

| شناسه | نتیجه اولیه | نتیجه پس از بازبینی | فراخوانی ساختاریافته | خروجی نهایی (نمونه) |
|---|---|---|---:|---|
| I01 | قبول | قبول | 0 | Good morning |
| I02 | رد | رد | 0 | 15 |
| I03 | قبول | قبول | 0 | 10:20 |
| I04 | قبول | قبول | 0 | Friday |
| I05 | قبول | قبول | 0 | Cal |
| I06 | قبول | قبول | 0 | carrot |
| I07 | قبول | قبول | 0 | {"color": "blue", "count": 3} |
| I08 | قبول | قبول | 0 | QUIET RIVER |
| I09 | قبول | قبول | 0 | Yesterday she went to the park. |
| I10 | قبول | قبول | 0 | apple, banana, pear |
| I11 | قبول | قبول | 0 | red green blue |
| I12 | قبول | قبول | 0 | OK-17 |
| T01 | قبول | قبول | 1 | The simulated current weather in Oslo is cloudy with a temperature of 4 degrees Celsius. |
| T02 | قبول | قبول | 1 | The simulated store has 7 units of blue notebook in stock. |
| T03 | قبول | قبول | 1 | The order ORD-104 has been delivered and the delivery was made on Wednesday. |
| T04 | قبول | قبول | 1 | The total price for seven items costing 6 currency units each is 42.0. |
| T05 | قبول | قبول | 1 | The conversion result is 3000 grams. |
| T06 | قبول | قبول | 1 | The current weather in Amsterdam is rainy with a temperature of 11°C. |
| T07 | قبول | قبول | 1 | The red mug is not available in the store as the inventory quantity is 0. |
| T08 | قبول | قبول | 1 | The order ORD-220 is currently in transit and is expected to arrive on a Friday. |
| T09 | قبول | قبول | 0 | No lookup required |
| T10 | رد | رد | 0 | uqeroc |
| T11 | قبول | قبول | 2 | The blue notebook is in stock and there are 7 of them. The total price for 3 blue notebooks is 13.5 currency units. |
| T12 | قبول | قبول | 2 | The temperature in Oslo is 4°C and it's cloudy, while Amsterdam's temperature is 11°C and it's rainy. Therefore, Oslo is colder than Amsterdam. |

### MiniCPM5-1B-Q4

**Weight SHA-256:** `81b64d05a23b17b34c475f42b3e72fbde62d4b92cc34541f7a8031d0752deafa`
**Raw evidence SHA-256:** `40d08805762ad687c5ab06d9cf2e9d14865f3a30b72771665cf051d603d378e5`

| شناسه | نتیجه اولیه | نتیجه پس از بازبینی | فراخوانی ساختاریافته | خروجی نهایی (نمونه) |
|---|---|---|---:|---|
| I01 | قبول | قبول | 0 | Good morning |
| I02 | رد | رد | 0 | 3 |
| I03 | رد | رد | 0 | 19:35 |
| I04 | رد | رد | 0 | Tuesday |
| I05 | قبول | قبول | 0 | Cal |
| I06 | قبول | قبول | 0 | carrot |
| I07 | رد | رد | 0 | ```json {"color": "blue", "count": 3} ``` |
| I08 | قبول | قبول | 0 | QUIET RIVER |
| I09 | قبول | قبول | 0 | Yesterday she went to the park. |
| I10 | قبول | قبول | 0 | apple, banana, pear |
| I11 | قبول | قبول | 0 | red green blue |
| I12 | قبول | قبول | 0 | OK-17 |
| T01 | قبول | قبول | 1 | I have the information from the get_city_weather function call and can report the current weather conditions in Oslo.  The current weather in Oslo is: clou… |
| T02 | قبول | قبول | 1 | The simulated store has 7 blue notebook units in stock.  The question asked for the quantity of blue notebook, so I will use get_store_stock tool and repor… |
| T03 | قبول | قبول | 1 | The order with ID ORD-104 has been delivered on Wednesday. The total cost of the order is $100, which includes 2 unit prices of $50 each totaling $100.  Th… |
| T04 | قبول | قبول | 1 | The total calculated using the provided unit price and quantity is 42.00 currency units.  The total for the seven items costing 6 currency units each is 42… |
| T05 | قبول | قبول | 1 | The numerical result of converting 3 kilograms to grams is 3000.0 grams.  The unit for converting 3 kilograms to grams is "g". |
| T06 | رد | قبول | 1 | I have the information from the get_city_weather function call for Amsterdam's simulated current weather.  The current conditions in Amsterdam are: rain, a… |
| T07 | رد | رد | 2 | I will call the get_store_stock function with the item "mug" to check its inventory.  The simulated store inventory for a red mug is not available. |
| T08 | قبول | قبول | 1 | The simulated order ORD-220 is currently in transit and is expected to arrive on Friday.  - Order ID: ORD-220 - Status: In Transit - Expected Arrival Weekd… |
| T09 | قبول | قبول | 0 | No lookup required |
| T10 | رد | رد | 0 | orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange o… |
| T11 | رد | رد | 4 | The user requested two pieces of information: the inventory quantity for the blue notebook and the total price for 3 notebooks. I have obtained this inform… |
| T12 | قبول | قبول | 2 | I will use the get_city_weather tool to retrieve the current weather for Oslo and Amsterdam, then compare the temperature data to determine which city is c… |

### Qwen3.5-0.8B-Q4

**Weight SHA-256:** `bd258782e35f7f458f8aced1adc053e6e92e89bc735ba3be89d38a06121dc517`
**Raw evidence SHA-256:** `0da2fc0e64df7fc19ca4753f818ab56da43999067b6acf947036321ecd7f9ca4`

| شناسه | نتیجه اولیه | نتیجه پس از بازبینی | فراخوانی ساختاریافته | خروجی نهایی (نمونه) |
|---|---|---|---:|---|
| I01 | قبول | قبول | 0 | Good morning |
| I02 | رد | رد | 0 | 4 |
| I03 | رد | رد | 0 | 13:45 |
| I04 | قبول | قبول | 0 | Friday |
| I05 | رد | رد | 0 | Ben |
| I06 | قبول | قبول | 0 | carrot |
| I07 | قبول | قبول | 0 | {"color": "blue", "count": 3} |
| I08 | قبول | قبول | 0 | QUIET RIVER |
| I09 | قبول | قبول | 0 | Yesterday she went to the park. |
| I10 | قبول | قبول | 0 | apple, banana, pear |
| I11 | قبول | قبول | 0 | red green blue |
| I12 | قبول | قبول | 0 | OK-17 |
| T01 | رد | قبول | 1 | Cloudy at 4°C. |
| T02 | قبول | قبول | 1 | The simulated store has **7** blue notebook units in stock. |
| T03 | قبول | قبول | 1 | Order ORD-104 has a status of **delivered** on the delivery weekday of **Wednesday**. |
| T04 | قبول | قبول | 1 | The total price for seven items costing 6 currency units each is **42**. |
| T05 | قبول | قبول | 1 | The conversion of 3 kilograms to grams is **3000** grams. |
| T06 | قبول | قبول | 1 | The simulated current weather in Amsterdam is **rainy** at **11°C**. |
| T07 | قبول | قبول | 1 | The simulated store inventory for red mug shows a quantity of 0, indicating it is not currently available. |
| T08 | قبول | قبول | 1 | Order ORD-220 is currently **in transit**. It is scheduled to arrive on **Friday**. |
| T09 | رد | رد | 0 | I cannot use tools to fulfill this request. I can help with things that require tools like looking up delivery statuses, checking store stock, and getting… |
| T10 | رد | رد | 0 | gnoarlo |
| T11 | قبول | رد | 2 | Here are the results for the blue notebook: *   **In stock:** 7 notebooks *   **Total price for 3 notebooks:** $13.50 |
| T12 | قبول | قبول | 2 | **Oslo:** 4°C (Cloudy)   **Amsterdam:** 11°C (Rainy)  Comparing their temperatures: Oslo is colder (4°C) than Amsterdam (11°C). |

### LFM3-1.7B-Q4

**Weight SHA-256:** `3793e1e6e2266919d6e015287221b41100175a98eddaba92e111aed3b05c93c4`
**Raw evidence SHA-256:** `901276294c45c5f2d5b4f5438c350f7cb3ddea6308b7b9dc7197f1b9ab0ea96f`

| شناسه | نتیجه اولیه | نتیجه پس از بازبینی | فراخوانی ساختاریافته | خروجی نهایی (نمونه) |
|---|---|---|---:|---|
| I01 | قبول | قبول | 0 | Good morning |
| I02 | رد | رد | 0 | The total number of pens is $6 \times 4 = 24$. After removing 3 pens, the remaining number is $24 - 3 = 21$.  21 |
| I03 | رد | رد | 0 | 09:50  Let's verify: Start time 09:45, add 35 minutes. - 09:45 + 6 min = 10:00 - Remaining 29 min after that? Wait, let's do it properly.  From 09:45, addi… |
| I04 | قبول | قبول | 0 | Friday |
| I05 | رد | رد | 0 | Cal is the youngest.  Ben > Cal, and Ada > Ben, so the order from oldest to youngest is Ada > Ben > Cal. Thus, Cal is the youngest.</think>Cal |
| I06 | قبول | قبول | 0 | carrot |
| I07 | قبول | قبول | 0 | {   "color": "blue",   "count": 3 } |
| I08 | قبول | قبول | 0 | QUIET RIVER |
| I09 | قبول | قبول | 0 | Yesterday she went to the park. |
| I10 | قبول | قبول | 0 | apple, banana, pear |
| I11 | قبول | قبول | 0 | red green blue |
| I12 | قبول | قبول | 0 | OK-17 |
| T01 | قبول | قبول | 1 | The current weather in Oslo is cloudy with a temperature of 4 °C. |
| T02 | قبول | قبول | 1 | The simulated store currently has **7** units of "blue notebook" in stock. |
| T03 | قبول | قبول | 1 | The order **ORD-104** has a status of **delivered**, and it was delivered on **Wednesday**. |
| T04 | قبول | قبول | 1 | The total price for seven items at 6 currency units each is **42**. |
| T05 | قبول | قبول | 1 | The conversion result is **3000 grams**. |
| T06 | قبول | قبول | 1 | The current weather in Amsterdam is **rainy** with a temperature of **11°C**. |
| T07 | قبول | قبول | 1 | The simulated inventory for **red mug** shows a quantity of **0**, so it is **not available**. |
| T08 | قبول | قبول | 1 | The order **ORD-220** is currently **in transit**, and its expected arrival weekday is **Friday**. |
| T09 | قبول | قبول | 0 | No lookup required |
| T10 | رد | رد | 0 | orange |
| T11 | قبول | قبول | 2 | - Inventory for the **blue notebook**: **7** units in stock.   - Total price for **3 notebooks** at **4.5** each: **13.5** currency units. |
| T12 | قبول | قبول | 2 | Oslo: 4 °C (cloudy)   Amsterdam: 11 °C (rainy)  Since 4 °C is lower than 11 °C, **Oslo is colder** than Amsterdam. |

### LFM2.5-1.2B-Thinking-Q4

**Weight SHA-256:** `4a1e1824f71091f368137b6966094461019f6af3a5aadd96033bee59fc9eaeea`
**Raw evidence SHA-256:** `b42f8eda1739f5e12441da6f346ca732dbf9dc0b3e615f47748da162c7750251`

| شناسه | نتیجه اولیه | نتیجه پس از بازبینی | فراخوانی ساختاریافته | خروجی نهایی (نمونه) |
|---|---|---|---:|---|
| I01 | رد | رد | 0 |  |
| I02 | قبول | قبول | 0 |   21 |
| I03 | رد | رد | 0 |  |
| I04 | قبول | قبول | 0 |   Friday |
| I05 | قبول | قبول | 0 |   Cal |
| I06 | رد | رد | 0 |  |
| I07 | قبول | قبول | 0 |   {"color": "blue", "count": 3} |
| I08 | رد | رد | 0 |  |
| I09 | قبول | قبول | 0 |   Yesterday she went to the park. |
| I10 | رد | رد | 0 |  |
| I11 | رد | رد | 0 |  |
| I12 | قبول | قبول | 0 |   OK-17 |
| T01 | قبول | قبول | 1 |   The current weather in Oslo is cloudy with a temperature of 4°C. |
| T02 | قبول | قبول | 1 |   The store has 7 blue notebook units in stock. |
| T03 | قبول | قبول | 1 |   The order ORD-104 has a status of **delivered** with delivery on **Wednesday**. |
| T04 | قبول | قبول | 1 |   The total price for seven items at 6 currency units each is $42. |
| T05 | قبول | قبول | 1 |   The conversion of 3 kilograms to grams results in **3000 grams**. |
| T06 | قبول | قبول | 1 |   The simulated current weather in Amsterdam is **rainy** with a temperature of **11°C**. |
| T07 | قبول | قبول | 1 |   The simulated inventory for "red mug" shows 0 units available. It is currently unavailable. |
| T08 | قبول | قبول | 1 |   The order ORD-220 is currently **in transit** with an expected arrival on **Friday**. |
| T09 | رد | رد | 0 |  |
| T10 | رد | رد | 0 |   egnora |
| T11 | رد | رد | 1 |  |
| T12 | قبول | قبول | 2 |   Oslo has a temperature of 4°C, while Amsterdam is 11°C. Oslo is colder. |

## 6. محدودیت شواهد و تصمیم بعدی

این گزارش یک نمونه اولیه E1 و فقط یک اجرا برای هر سؤال است؛ ۱۲ سناریوی ابزار مصنوعی و ۱۲ دستور عمومی نمی‌توانند نماینده کیفیت تمامی کاربردهای واقعی Agent باشند. ارزیابی امتیازدهی از نوع خودکار و بازبینی پسینی است و به داوری مستقل، اجرای چند Seed، موارد مبهم و آزمون روی Runtime رسمیِ پیشنهادی هر سازنده نیاز دارد. MiniCPM5 برای Tool Calling در اسناد OpenBMB با Parser اختصاصی SGLang معرفی شده است، بنابراین تفاوت‌های مشاهده‌شده در llama.cpp نباید به‌صورت قطعی به وزن نسبت داده شوند. معماری DEC، آموزش LoRA، ارتباط نهفته و داده LDI در این مطالعه آزموده نشده‌اند. همه پرسش‌های این آزمون انگلیسی‌اند، هرچند مستندات مطابق سیاست انتشار پروژه دوزبانه هستند.

### Original sources / منابع اصلی

- [OpenBMB official MiniCPM5 tool calling documentation](https://openbmb.cn/docs/en/guides/minicpm-text/minicpm5-1b)
- [Liquid AI official LFM3-1.7B tool calling](https://huggingface.co/LiquidAI/LFM3-1.7B)
- [Liquid AI official LFM2.5-1.2B-Thinking tool use](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)
- [llama.cpp OpenAI-style functions and Jinja](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

- فایل ماشین‌خوان شامل تمام ۱۲۰ اجرای سؤال، پاسخ خام، JSON ابزار، نتایج اجرای تابع و هر دو معیار امتیازدهی:

  [research/benchmarks/dec-english-instruction-tools-v1.json](../../research/benchmarks/dec-english-instruction-tools-v1.json)
