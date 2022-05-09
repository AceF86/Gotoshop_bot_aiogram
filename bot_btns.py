from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

btnSilpo = KeyboardButton('Ужгород')
btnpr = KeyboardButton('Перечин')
mainMenu = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(btnSilpo).row(btnpr)
)

btnMain = KeyboardButton('🔙Назат')
main = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(btnMain)
)

mainbutton = InlineKeyboardButton('🔙Назат', callback_data='cancel')
button2 = InlineKeyboardButton('Молочні продукти', callback_data='dairyProducts')
button3 = InlineKeyboardButton('Випічка', callback_data='baking')
button5 = InlineKeyboardButton('Цукерки, мармелад, шоколад', callback_data='sweets')
button6 = InlineKeyboardButton('Алкогольні напої', callback_data='alcohol')
button7 = InlineKeyboardButton("М'ясо", callback_data='meat')
button8 = InlineKeyboardButton('Риба та морепродукти', callback_data='fish')
button9 = InlineKeyboardButton('Пиво', callback_data='beer')
button10 = InlineKeyboardButton('Вино, Шампанське', callback_data='wine')
button11 = InlineKeyboardButton('Бренді (Коньяк)', callback_data='brandy')
button12 = InlineKeyboardButton('Фрукти та овочі', callback_data='fruits')
button14 = InlineKeyboardButton('Масло, спред, маргарин', callback_data='butter')
button15 = InlineKeyboardButton('Йогурт, закваски, безмолочні десерти', callback_data='yogurt')
button16 = InlineKeyboardButton("Твердий сир і (м'який) сир", callback_data='sir')
button17 = InlineKeyboardButton("Ковбасні вироби, сосиски, паштети м'ясні", callback_data='kovbas')
button18 = InlineKeyboardButton("Пироги, торти, десерти, тістечка", callback_data='cakes')
button19 = InlineKeyboardButton("Печиво, пряники, вафлі", callback_data='pechivo')
button20 = InlineKeyboardButton("Крупа", callback_data='groats')
inline_button = InlineKeyboardMarkup().add(button12,button3)\
    .add(button17).add(button7,button20).add(button8)\
    .add(button2).add(button15).add(button14).add(button16).add(button19)\
    .add(button5).add(button18).add(button6,button11)\
    .add(button10,button9).add(mainbutton)


markup_silpo = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('🔙Назат', callback_data='silpo'),
)

but1 = InlineKeyboardButton('Сільпо', callback_data='silpo')
but2 = InlineKeyboardButton('АТБ', callback_data='atb')
but3 = InlineKeyboardButton('Вопак', callback_data='vopak')
but4 = InlineKeyboardButton('Велмарт', callback_data='velmart')
inline_b = InlineKeyboardMarkup().add(but1,but2).add(but3,but4)

mainbutton = InlineKeyboardButton('🔙Назат', callback_data='cancel')
button1 = InlineKeyboardButton('Харчові продукти', callback_data='products')
button2 = InlineKeyboardButton('Солодкі продукти', callback_data='products2')
button3 = InlineKeyboardButton('Алкогольні напої', callback_data='alcohol_pr')
button4 = InlineKeyboardButton("М'ясо", callback_data='meat_pr')
button5 = InlineKeyboardButton('Молочні продукти', callback_data='milk')
button6 = InlineKeyboardButton('Побутова хімія', callback_data='ximia')
button7 = InlineKeyboardButton('Кава, кавозамінники, цикорій', callback_data='kava')

inline_butpr = InlineKeyboardMarkup().add(button1,button2)\
    .add(button3,button4).add(button5,button6).add(button7).add(mainbutton)

markup_perechin = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('🔙Назат.', callback_data='perechin'),
)

btnMain = KeyboardButton('🔙Назат.')
main2 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(btnMain)
)

but1 = InlineKeyboardButton('Амбар Маркет', callback_data='ambar')
but2 = InlineKeyboardButton('Копійочка', callback_data='kipi')
inline_p = InlineKeyboardMarkup().add(but1,but2)

but1 = InlineKeyboardButton('Амбар Маркет', callback_data='ambar')

inline_p2 = InlineKeyboardMarkup().add(but1)