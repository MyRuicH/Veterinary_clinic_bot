from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тварин на лікуванні")
    builder.button(text="Записати тварину на лікування")
    builder.button(text="Список вилікуваних тварин")
    
    builder.adjust(1)
    return builder.as_markup()


