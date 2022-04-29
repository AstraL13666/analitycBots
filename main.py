from tokens import tok
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.dispatcher.filters import Text
from requests import get

import logging

# Импорт токена
tok_tg = tok

# Инициализация бота и диспатчера
logging.basicConfig(level=logging.INFO)

bot = Bot(token=tok_tg)
dp = Dispatcher(bot)


# Ловим команду старт/хелп
@dp.message_handler(commands=['start', 'help'])
async def send_start(message: types.Message):

    # Данный метод title делает текст-киберссылку - не забываем parse_mode='Markdown'
    title = '[Analytic Company](https://analyticco.ru/)'
    txt = ('\n'
           f'Добро пожаловать в телеграм-бот компании!\n\n'
           'Пожалуйста, выберите соответствующий раздел!\n\n'
           '⚠️ Данный бот не поддерживает прием и обработку смс, пожалуйста, используйте клавиатуру бота!'
           )

    text = title + txt
    txt_ver = '⚠️ Пожалуйста используйте актуальную версию Telegram'

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    but_info = 'О нас'
    but_geon = 'Адрес'
    but_serv = 'Услуги'
    but_cont = 'Контакты'

    markup.add(but_info, but_serv).row(but_geon, but_cont)

    await message.answer(text.format(message.from_user), disable_web_page_preview=True, reply_markup=markup,
                         parse_mode='Markdown')
    await message.answer(txt_ver.format(message.from_user), parse_mode='Markdown')


# ловим текст присланный пользователем
@dp.message_handler(Text(equals='О нас'))
async def mes_info(message: types.Message):
    title = '[Analytic Company](https://analyticco.ru/)'
    txt = ('\n'
           '*О нас*\n\n'
           'Наша компания занимается техническими испытаниями, исследованиями, анализами, а так же сертификацией '
           'продукции во многих пищевых и агрокультурных промышленностях!\n\n'
           )

    text = title + txt

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    but_info = '💠 О нас'
    but_geon = 'Адрес'
    but_serv = 'Услуги'
    but_cont = 'Контакты'

    markup.add(but_info, but_serv).row(but_geon, but_cont)

    # вытаскиваем фото из интернета
    url = 'https://cognitivepaper.com/userfiles/16/608_0.webp'
    photo = get(url)

    # bot.send_photo() - команда на отправку фото в тг
    await bot.send_photo(message.chat.id, caption=text, photo=photo.content, parse_mode='Markdown',
                         reply_markup=markup)


@dp.message_handler(Text(equals='Адрес'))
async def mes_adress(message: types.Message):
    title = '[Analytic Company](https://analyticco.ru/)'
    txt = ('\n'
           '*Адрес*\n\n'
           '20 мин от м. Тушинская\n'
           '15 мин от мцд Трикотажная\n\n'
           'Так же в меню появилась кнопка, чтобы было удобно построить маршрут 😁'
           )

    # инициализация адреса
    url = 'https://yandex.ru/maps/213/moscow/house/volokolamskoye_shosse_89/Z04YcgZgTEABQFtvfXRzeHxlYw==/?ll=37.410555%2C55.829067&z=16.71'

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    but_info = 'О нас'
    but_geon = '💠 Адрес'
    but_serv = 'Услуги'
    but_cont = 'Контакты'

    # инициализируем веб-приложение, удобнее чем venue
    but_geo = InlineKeyboardButton(text='Мы на Я.карте', web_app=WebAppInfo(url=url))

    markup.add(but_info, but_serv).row(but_geon, but_cont)

    # создал отдельно web-кнопку для просмотра адреса и построение маршрута
    markup.add(but_geo)

    await message.answer(title + txt, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)


@dp.message_handler(Text(equals='Услуги'))
async def mes_copp(message: types.Message):
    title = '[Analytic Company](https://analyticco.ru/)'
    txt = ('\n'
           '*Услуги*\n\n'
           'АНАЛИЗЫ:\n'
           '~ Продуктов питания\n'
           '~ Алкогольной продукции\n'
           '~ БАД и Спец. питания\n'
           '~ Воды\n'
           '~ Почвы\n'
           )

    forms_url = 'https://forms.yandex.ru/cloud/626702c4c8cf4ae2e871ea4f/'
    url = 'https://avatars.mds.yandex.net/get-altay/933207/2a00000161bf5cf9558ca21e16e3e671ab9d/h300'
    photo = get(url)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    but_info = 'О нас'
    but_geon = 'Адрес'
    but_serv = '💠 Услуги'
    but_cont = 'Контакты'
    but_appn = InlineKeyboardButton(text='Заявка', web_app=WebAppInfo(url=forms_url))

    markup.add(but_info, but_serv).row(but_geon, but_cont).row(but_appn)

    await bot.send_photo(message.chat.id, caption=title + txt, photo=photo.content, parse_mode='Markdown',
                         reply_markup=markup)


@dp.message_handler(Text(equals='Контакты'))
async def mes_cont(message: types.Message):
    title = '[Analytic Company](https://analyticco.ru/)'
    txt = ('\n'
           '*Контакты*\n\n'
           '📱 +7 (925) 209 99 67\n'
           '☎️ +7 (499) 309 59 91\n'
           '🌐 [Наш сайт](https://analyticco.ru/)\n\n'
           
           # *жирный текст отправит бот* - и да, парс-мод: Маркдаун =)
           '*Вы так же можете оставить заявку на услугу:*\n\n'
           'Внизу появилась соответствующая кнопка!'
           )

    forms_url = 'https://forms.yandex.ru/cloud/626702c4c8cf4ae2e871ea4f/'

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    but_info = 'О нас'
    but_geon = 'Адрес'
    but_serv = 'Услуги'
    but_cont = '💠 Контакты'

    # Здесь веб-приложение заполнения Яндекс.форм
    but_appn = InlineKeyboardButton(text='Заявка', web_app=WebAppInfo(url=forms_url))

    markup.add(but_info, but_serv).row(but_geon, but_cont).row(but_appn)

    await message.answer(title + txt, disable_web_page_preview=True, parse_mode='Markdown', reply_markup=markup)


# простой метод удаление смс который прислал пользователь
@dp.message_handler()
async def mes_cont(message: types.Message):
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
