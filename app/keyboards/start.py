from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тварин на лікуванні")
    builder.button(text="Записати тварину на лікування")
    builder.button(text="Список вилікуваних тварин")
    builder.button(text="Показати список відгуків")
    builder.button(text="Додати відгук")

    
    builder.adjust(1)
    return builder.as_markup()


