
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7937541676:AAHszg1nXpgR4w-0OuMkVDB6b75OpZgAEI8'
bot = telebot.TeleBot(API_TOKEN)

ADMIN_IDS = [5988557244, 6413963185]

welcome_text = """Καλωσόρισες στην AnchorBets! Στο γκρουπ που διαθέτω ανεβαίνουν σημεία τα οποία θα σε βοηθήσουν να βγάλεις το κάτι τις έξτρα

Μην απορήσεις με τα μτς — είναι λίγο περίεργα 😅

Η συνδρομή είναι στα **30€/μήνα**
Ολοκληρώνεις τη συναλλαγή και σε προσθέτω στην ομάδα!

Εθνική Τράπεζα:
GR2801103820000038200543569

Revolut:
@spyridon_p"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Yes ✅", callback_data="yes"),
        InlineKeyboardButton("No ❌", callback_data="no")
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"])
def handle_query(call):
    if call.data == "yes":
        for admin_id in ADMIN_IDS:
            bot.send_message(admin_id, f"Ο χρήστης @{call.from_user.username or call.from_user.first_name} πάτησε YES.")
        bot.answer_callback_query(call.id, "Ευχαριστούμε για την επιβεβαίωση!")
    else:
        bot.answer_callback_query(call.id, "Επέλεξες Όχι.")

bot.infinity_polling()
