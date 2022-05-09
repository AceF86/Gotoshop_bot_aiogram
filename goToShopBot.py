import json
import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
import get_gotoshop
import bot_btns as nav
import asyncio



TOKEN = '2143038264:AAEcpzv7kTrDXWJ0jEIf_jhF4cjmkiYdhHc'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


class GetProducts(StatesGroup):
   dairy2 = State()

class GetProductsPr(StatesGroup):
   products = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
   await message.answer(
       "👋Доброго дня {0.first_name}! Gotoshop.ua Акції та знижки супермаркетів України"
       "\nВиберіть місто.".format(message.from_user),
       reply_markup=nav.mainMenu,
   )


@dp.message_handler()
async def bot_message(message: types.Message):

   if message.text == "Ужгород":
       await message.answer(
           "Список категорій товару."
           ,
           reply_markup=nav.inline_button,
       )
       await GetProducts.dairy2.set()

   elif message.text == "Перечин":
       await message.answer(
           "Список категорій товарів супермаркетів:\n" "-Амбар Маркет\n" "-Копійочка.",
           reply_markup=nav.inline_butpr,
       )
       await GetProductsPr.products.set()

   elif message.text == "🔙Назат":
       await message.answer("Список категорій товара.", reply_markup=nav.inline_button)
       await GetProducts.dairy2.set()

   elif message.text == "🔙Назат.":
       await message.answer("Список категорій товара.", reply_markup=nav.inline_butpr)
       await GetProductsPr.products.set()


@dp.callback_query_handler(text="silpo")
async def callback(callback_query: types.CallbackQuery):
   await callback_query.message.delete()
   await callback_query.message.answer(
       "Список категорій товара.", reply_markup=nav.inline_button
   )
   await callback_query.answer()


@dp.callback_query_handler(text="perechin")
async def callback(callback_query: types.CallbackQuery):
   await callback_query.message.delete()
   await callback_query.message.answer(
       "Список категорій товара.", reply_markup=nav.inline_butpr
   )
   await callback.answer()


@dp.callback_query_handler(
   text=[
       "products",
       "products2",
       "alcohol_pr",
       "meat_pr",
       "milk",
       "ximia",
       "kava",
   ], state=GetProductsPr.products
)
async def callback_pr(callback_query: types.CallbackQuery, state: FSMContext):
   global spisok2
   await callback_query.answer()
   if callback_query.data == "products":
      spisok2 = "gotoshop/produkts_pr.json"

   elif callback_query.data == "products2":
       spisok2 = "gotoshop/produkts2_pr.json"

   elif callback_query.data == "alcohol_pr":
       spisok2 = "gotoshop/alcohol_pr.json"

   elif callback_query.data == "meat_pr":
       spisok2 = "gotoshop/meet_pr.json"

   elif callback_query.data == "milk":
       spisok2 = "gotoshop/milk_pr.json"

   elif callback_query.data == "ximia":
       spisok2 = "gotoshop/ximia_pr.json"

   elif callback_query.data == "kava":
       spisok2 = "gotoshop/kava_pr.json"

   den = spisok2
   await state.update_data({"den": den})

   await callback_query.message.answer(
       "Виберіть супермаркет.", reply_markup=nav.inline_p
   )
   await callback_query.message.delete_reply_markup()

   await GetProductsPr.products.set()

@dp.callback_query_handler(state="*", text=["cancel"])
@dp.callback_query_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
   await callback_query.answer()
   if callback_query.data == "cancel":
       current_state = await state.get_state()
       if current_state is None:
           return
       await state.finish()
   await callback_query.message.delete_reply_markup()
   await callback_query.message.answer("OK👌", reply_markup=nav.mainMenu)


@dp.callback_query_handler(
   text=[
       "dairyProducts",
       "baking",
       "fruits",
       "sir",
       "sweets",
       "alcohol",
       "fish",
       "meat",
       "beer",
       "wine",
       "brandy",
       "butter",
       "yogurt",
       "kovbas",
       "sir",
       "cakes",
       "pechivo",
       "groats",
   ], state=GetProducts.dairy2
)
async def callback(callback_query: types.CallbackQuery, state: FSMContext):
   global spisok
   await callback_query.answer()
   if callback_query.data == "dairyProducts":
       spisok = "gotoshop/DairyProducts.json"

   elif callback_query.data == "baking":
       spisok = "gotoshop/Baking.json"

   elif callback_query.data == "sweets":
       spisok = "gotoshop/Sweets.json"

   elif callback_query.data == "alcohol":
       spisok = "gotoshop/Alcohol.json"

   elif callback_query.data == "fish":
       spisok = "gotoshop/Fish.json"

   elif callback_query.data == "meat":
       spisok = "gotoshop/Meat.json"

   elif callback_query.data == "beer":
       spisok = "gotoshop/Beer.json"

   elif callback_query.data == "wine":
       spisok = "gotoshop/Wine.json"

   elif callback_query.data == "brandy":
       spisok = "gotoshop/Brandy.json"

   elif callback_query.data == "fruits":
       spisok = "gotoshop/FruitsAndVegetables.json"

   elif callback_query.data == "butter":
       spisok = "gotoshop/ButterSpreadMargarine.json"

   elif callback_query.data == "yogurt":
       spisok = "gotoshop/YogurtAndMore.json"

   elif callback_query.data == "sir":
       spisok = "gotoshop/Sir.json"

   elif callback_query.data == "kovbas":
       spisok = "gotoshop/Kovbas.json"

   elif callback_query.data == "cakes":
       spisok = "gotoshop/Cakes.json"

   elif callback_query.data == "pechivo":
       spisok = "gotoshop/Pechivo.json"

   elif callback_query.data == "groats":
       spisok = "gotoshop/Groats.json"

   den = spisok
   await state.update_data({"den": den})

   await callback_query.message.delete_reply_markup()
   await callback_query.message.answer(
       "Виберіть супермаркет.", reply_markup=nav.inline_b
   )

   await GetProducts.dairy2.set()


@dp.callback_query_handler(
   text=["silpo", "atb", "vopak", "velmart"], state=GetProducts.dairy2
)
async def read_dairy(callback_query: types.CallbackQuery, state: FSMContext):
   data = await state.get_data()
   den = data.get("den")

   with open(den, "r", encoding="utf-8") as f:
       file_content = f.read()
       data1 = json.loads(file_content)

       if callback_query.data == "silpo":
           a = "Сільпо"
           b = "<u>нова ціна:</u>"
           c = "<u>стара ціна:</u>"
           d = "грн."
           s = "%"

       elif callback_query.data == "atb":
           a = "АТБ"
           b = ""
           c = ""
           d = ""
           s = ""
       elif callback_query.data == "vopak":
           a = "Вопак"
           b = ""
           c = ""
           d = ""
           s = ""
       elif callback_query.data == "velmart":
           a = "Велмарт"
           b = ""
           c = ""
           d = ""
           s = ""
       await callback_query.answer()
       await callback_query.message.delete_reply_markup()

       flag = True
       for i in data1:
           if a in i["desc"]:
               info = (
                   f"Супермаркет {a} Ужгород\n"
                   f"<a href='{i['image336']['src']}'> </a>\n"
                   f"<strong><u>{i['discount_name']}</u></strong>.\n"
                   f"<strong>{i['date']}</strong>\n\n"
                   f"<i>{i['name']}</i>\n"
                   f"{b} {i['priceafter']} {d}\n"
                   f"{c} <s>{i['pricebefore']}</s> {d} {i['discount']}{s}\n"
               )

               await state.finish()
               await asyncio.sleep(1)
               await callback_query.message.answer(info, reply_markup=nav.main)

               flag = False

       if flag:
           await state.finish()
           await callback_query.message.answer(
               "Акцій по даній тематиці не має.", reply_markup=nav.markup_silpo
           )

@dp.callback_query_handler(text=["ambar", "kipi"], state=GetProductsPr.products)
async def read_produkts2(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    den = data.get("den")

    with open(den, "r", encoding="utf-8") as f:
       file_content = f.read()
       data1 = json.loads(file_content)

       if callback_query.data == "ambar":
           a = "Амбар Маркет"
       elif callback_query.data == "kipi":
           a = "Копійочка"

       await callback_query.answer()
       await callback_query.message.delete_reply_markup()

       flag = True
       for i in data1:
           if a in i["desc"]:
               info = (
                   f"Супермаркет {a} місто Перечин\n"
                   f"<a href='{i['image336']['src']}'> </a>\n"
                   f"<strong><u>{i['discount_name']}</u></strong>.\n"
                   f"<strong>{i['date']}</strong>\n\n"
                   f"<i>{i['name']}</i>\n"
               )
               await state.finish()
               await asyncio.sleep(1)
               await callback_query.message.answer(info, reply_markup=nav.main2)

               flag = False

       if flag:
           await state.finish()
           await callback_query.message.answer(
               "Акцій по даній тематиці не має.", reply_markup=nav.markup_perechin
           )


async def news_every_minute():
    hours = 60 * 60
    admin_id = "552974553"
    while True:
        try:
            get_gotoshop.main()
            text = 'Обновився'
        except Exception as ex:
            text = f'Не обновився {ex}'
        await bot.send_message(chat_id=admin_id, text=text)
        await asyncio.sleep(4 * hours)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        pass

