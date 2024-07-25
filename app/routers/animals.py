from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from app.data import open_files, animals
from app.keyboards.animals import build_animals_keyboard, build_anim_action_keyboard
from app.forms.aniamls import AniamlsForm



animals_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
    if message.from_user.is_bot:
        await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
    else:
        await message.answer(text=text, reply_markup=keyboard, **kwargs)


@animals_router.message(F.text == "Список тварин на лікуванні")
async def show_sick_animals(message : Message, state: FSMContext):
    animals = open_files.get_animals()
    keyboard = build_animals_keyboard(animals)
    text = "Список тварин:"
    return await edit_or_answer(message=message, text=text, keyboard=keyboard)


@animals_router.callback_query(F.data.startswith("animal_"))
async def animal_actions(call_back: CallbackQuery, state: FSMContext):
    animal = call_back.data.split("_")[-1]
    keyboard = build_anim_action_keyboard(animal)
    return await edit_or_answer(
        message=call_back.message,
        text=animal,
        keyboard=keyboard
        )


@animals_router.message(F.text == "Записати тварину на лікування")
async def add_animal(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AniamlsForm.name)
    await message.answer(text="Вкажіть ім'я тварини:")


@animals_router.message(AniamlsForm.name)
async def add_animal_action(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = animals.add_animal(data.get("name"))
    await message.answer(text=msg)


@animals_router.callback_query(F.data.startswith("cure_the_animal_"))
async def cure_animal(call_back: CallbackQuery, state: FSMContext):
    animal = call_back.data.split("_")[-1]
    msg = animals.cure_animal(animal)
    await call_back.message.answer(text=msg)


@animals_router.callback_query(F.data.startswith("remove_animal_"))
async def remove_animal(call_back: CallbackQuery, state: FSMContext):
    animal = call_back.data.split("_")[-1]
    msg = animals.remove_animal(animal)
    await call_back.message.answer(text=msg)


@animals_router.message(F.text == "Список вилікуваних тварин")
async def show_cured_animals(message: Message, state: FSMContext):
    cured_animals = open_files.get_cured_animals()
    text = ""

    for i, animal in enumerate(cured_animals, start=1):
        text += f"{i}. {animal}\n"
        
    await message.answer(text=text)












