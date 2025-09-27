from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("Пополнить баланс➕", callback_data="add_money")], 
                                                       [InlineKeyboardButton("Снять деньги➖", callback_data="take_money")],
                                                       [InlineKeyboardButton("Удалить чеки", callback_data="rem_checks")],
                                                       [InlineKeyboardButton("Другое", callback_data="other")]])

wallets_keyboard_add = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("CryptoBot", callback_data="CryptoBot_adding")], 
                                                        [InlineKeyboardButton("Назад↩️", callback_data="back")]])

wallets_keyboard_take = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("CryptoBot", callback_data="CryptoBot_taking")], 
                                                        [InlineKeyboardButton("Назад↩️", callback_data="back")]])

add_money_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("USDT", callback_data="adding_USDT")],
                                                            [InlineKeyboardButton("TON", callback_data="adding_TON")],
                                                            [InlineKeyboardButton("Назад↩️", callback_data="add_money")]])

take_money_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("USDT", callback_data="taking_USDT")],
                                                            [InlineKeyboardButton("TON", callback_data="taking_TON")],
                                                              [InlineKeyboardButton("Назад↩️", callback_data="take_money")]])

admin_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("Рассылка", callback_data="ad")],
                       [InlineKeyboardButton("Назад↩️", callback_data="back")]])

cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("Отмена❌", callback_data='cancel')]])

ad_constuctor = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("Отправить📤", callback_data="Send_ad")],
                                                     [InlineKeyboardButton("Закрыть❌", callback_data='cancel_admin')],
                                                      [InlineKeyboardButton("Добавить кнопку🔘", callback_data="add_button")]])

