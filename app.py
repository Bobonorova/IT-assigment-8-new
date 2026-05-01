import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔐 TOKEN (yangisini qo‘ying!)
TOKEN = "8678686066:AAGDspiKhcg8us0x6SRWk6Hq4yZ5Tg04ITM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


# ---------------- MENU ----------------
def main_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        types.InlineKeyboardButton("👨 Dadam", callback_data="dad"),
        types.InlineKeyboardButton("👩 Onam", callback_data="mom"),
    )
    keyboard.add(
        types.InlineKeyboardButton("👤 Men", callback_data="me"),
        types.InlineKeyboardButton("👨‍🦱 Akam", callback_data="bro"),
    )
    keyboard.add(
        types.InlineKeyboardButton("🧒 Ukam", callback_data="little"),
    )

    return keyboard


# ---------------- BACK ----------------
def back_button():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back")
    )


# ---------------- START ----------------
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "👋 Xush kelibsiz!\nKerakli bo‘limni tanlang:",
        reply_markup=main_menu()
    )


# ---------------- CALLBACK ----------------
@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    data = call.data

    pages = {
        "dad": "👨 Dadam:\n\n📛 Ism: Rustam\n📱 Telefon: +998901234567\n📧 Email: dad@gmail.com\n💳 Karta: 8600 **** **** 1234\n🏠 Adres: Toshkent, Chilonzor",

        "mom": "👩 Onam:\n\n📛 Ism: Gulnora\n📱 Telefon: +998931112233\n📧 Email: mom@gmail.com\n💳 Karta: 8600 **** **** 5678\n🏠 Adres: Toshkent, Yunusobod",

        "me": "👤 Men:\n\n📛 Ism: User\n📱 Telefon: +998990001122\n📧 Email: me@gmail.com\n💳 Karta: 8600 **** **** 0001\n🏠 Adres: Toshkent",

        "bro": "👨‍🦱 Akam:\n\n📛 Ism: Aziz\n📱 Telefon: +998911234567\n📧 Email: bro@gmail.com\n💳 Karta: 8600 **** **** 2222\n🏠 Adres: Samarqand",

        "little": "🧒 Ukam:\n\n📛 Ism: Ali\n📱 Telefon: +998933334444\n📧 Email: little@gmail.com\n💳 Karta: 8600 **** **** 3333\n🏠 Adres: Buxoro",
    }

    if data == "back":
        await call.message.edit_text(
            "👋 Asosiy menu:",
            reply_markup=main_menu()
        )
        return

    if data in pages:
        await call.message.edit_text(
            pages[data],
            reply_markup=back_button()
        )


# ---------------- RUN ----------------
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
