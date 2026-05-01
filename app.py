import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔥 BOT TOKEN (to‘g‘ridan-to‘g‘ri yozilgan, .env YO‘Q)
TOKEN = "8678686066:AAEXzJx57VHBDEizKipY7CxQ0UmSXCBq40U"

# 🔐 faqat ruxsat berilgan userlar
ALLOWED_USERS = [123456789]  # o'zingizni telegram ID yozasiz

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


# ---------------- START MENU ----------------
def main_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        types.InlineKeyboardButton("👨 Dadam", callback_data="dad"),
        types.InlineKeyboardButton("👩 Onam", callback_data="mom"),
    )
    keyboard.add(
        types.InlineKeyboardButton("👤 Men", callback_data="me"),
        types.InlineKeyboardButton("👦 Akam", callback_data="bro"),
    )
    keyboard.add(
        types.InlineKeyboardButton("👶 Ukam", callback_data="little"),
    )

    return keyboard


# ---------------- BACK BUTTON ----------------
def back_button():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back")
    )
    return keyboard


# ---------------- START ----------------
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.from_user.id not in ALLOWED_USERS:
        await message.answer("⛔ Sizga ruxsat yo‘q")
        return

    await message.answer(
        "👋 Salom! Tanlang:",
        reply_markup=main_menu()
    )


# ---------------- CALLBACK HANDLER ----------------
@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):

    data = call.data

    if data == "back":
        await call.message.edit_text(
            "👋 Asosiy menu:",
            reply_markup=main_menu()
        )

    elif data == "dad":
        await call.message.edit_text(
            "👨 Dadam:\n\n"
            "📛 Ism: Rustam\n"
            "📱 Telefon: +998901234567\n"
            "📧 Email: dad@gmail.com\n"
            "💳 Karta: 8600 3483 2873 1234\n"
            "🏠 Adres: Toshkent, Chilonzor",
            reply_markup=back_button()
        )

    elif data == "mom":
        await call.message.edit_text(
            "👩 Onam:\n\n"
            "📛 Ism: Gulnora\n"
            "📱 Telefon: +998931112233\n"
            "📧 Email: mom@gmail.com\n"
            "💳 Karta: 8600 3994 3828 5678\n"
            "🏠 Adres: Toshkent, Yunusobod",
            reply_markup=back_button()
        )

    elif data == "me":
        await call.message.edit_text(
            "👤 Men:\n\n"
            "📛 Ism: Muslima\n"
            "📱 Telefon: +998990001122\n"
            "📧 Email: me@gmail.com\n"
            "💳 Karta: 8600 3432 9763 0001\n"
            "🏠 Adres: Toshkent",
            reply_markup=back_button()
        )

    elif data == "bro":
        await call.message.edit_text(
            "👦 Akam:\n\n"
            "📛 Ism: Aziz\n"
            "📱 Telefon: +998911234567\n"
            "📧 Email: bro@gmail.com\n"
            "💳 Karta: 8600 4783 4298 2222\n"
            "🏠 Adres: Samarqand",
            reply_markup=back_button()
        )

    elif data == "little":
        await call.message.edit_text(
            "👶 Ukam:\n\n"
            "📛 Ism: Ali\n"
            "📱 Telefon: +998933334444\n"
            "📧 Email: little@gmail.com\n"
            "💳 Karta: 8600 3245 4232 3333\n"
            "🏠 Adres: Buxoro",
            reply_markup=back_button()
        )


# ---------------- RUN ----------------
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
