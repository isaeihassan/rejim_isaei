import telebot from telebot import types

TOKEN = "7639099981:AAEZDr8_6uRDOCi0M75tzHbBjDqu5ptxin4 " bot = telebot.TeleBot(TOKEN)

ذخیره اطلاعات کاربران

user_data = {}

def calculate_bmi(weight, height): height_m = height / 100 # تبدیل سانتی‌متر به متر return round(weight / (height_m ** 2), 2)

@bot.message_handler(commands=['start']) def send_welcome(message): chat_id = message.chat.id user_data[chat_id] = {} bot.send_message(chat_id, "سلام! لطفاً سن خود را وارد کنید:") bot.register_next_step_handler(message, process_age)

def process_age(message): chat_id = message.chat.id try: user_data[chat_id]['age'] = int(message.text) bot.send_message(chat_id, "جنسیت خود را انتخاب کنید:", reply_markup=gender_markup()) except ValueError: bot.send_message(chat_id, "لطفاً عدد معتبر وارد کنید.") bot.register_next_step_handler(message, process_age)

def gender_markup(): markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) markup.add("مرد", "زن") return markup

@bot.message_handler(func=lambda message: message.text in ["مرد", "زن"]) def process_gender(message): chat_id = message.chat.id user_data[chat_id]['gender'] = message.text bot.send_message(chat_id, "وزن خود را به کیلوگرم وارد کنید:") bot.register_next_step_handler(message, process_weight)

def process_weight(message): chat_id = message.chat.id try: user_data[chat_id]['weight'] = float(message.text) bot.send_message(chat_id, "قد خود را به سانتی‌متر وارد کنید:") bot.register_next_step_handler(message, process_height) except ValueError: bot.send_message(chat_id, "لطفاً وزن معتبر وارد کنید.") bot.register_next_step_handler(message, process_weight)

def process_height(message): chat_id = message.chat.id try: user_data[chat_id]['height'] = float(message.text) bmi = calculate_bmi(user_data[chat_id]['weight'], user_data[chat_id]['height']) user_data[chat_id]['bmi'] = bmi bot.send_message(chat_id, f"شاخص توده بدنی (BMI) شما: {bmi}") suggest_diet_and_exercise(chat_id, bmi) except ValueError: bot.send_message(chat_id, "لطفاً عدد معتبر وارد کنید.") bot.register_next_step_handler(message, process_height)

def suggest_diet_and_exercise(chat_id, bmi): if bmi < 18.5: diet_plan = "شما کمبود وزن دارید. توصیه می‌شود غذاهای پرکالری و مقوی مصرف کنید." exercise_plan = "تمرینات قدرتی برای افزایش وزن توصیه می‌شود." elif 18.5 <= bmi < 25: diet_plan = "وزن شما نرمال است. رژیم غذایی متعادل را حفظ کنید." exercise_plan = "ورزش‌های متعادل مثل پیاده‌روی و شنا توصیه می‌شود." else: diet_plan = "شما اضافه وزن دارید. مصرف کربوهیدرات و چربی را کاهش دهید." exercise_plan = "تمرینات هوازی مانند دویدن و دوچرخه‌سواری مناسب شماست."

bot.send_message(chat_id, f"📌 رژیم غذایی پیشنهادی: 

{diet_plan}") bot.send_message(chat_id, f"💪 برنامه ورزشی پیشنهادی: {exercise_plan}")

bot.polling()

