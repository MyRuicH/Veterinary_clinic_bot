from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from app.data import open_files, animals, reviews
from app.keyboards.animals import build_animals_keyboard, build_anim_action_keyboard
from app.forms.aniamls import AniamlsForm
from app.forms.reviews import ReviewsForm


review_router = Router()


@review_router.message(F.text == "Показати список відгуків")
async def show_reviews(message: Message, state: FSMContext):
    reviews = open_files.get_reviews()
    msg = ""
    if reviews:
        for i, review in enumerate(reviews, start=1):
            msg += f"{i}. {review}\n"

        await message.answer(text=msg)
    else:
        msg = "Список відгуків пустий"
        await message.answer(text=msg)

@review_router.message(F.text == "Додати відгук")
async def add_reivew(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ReviewsForm.review)
    await message.answer(text="Напишіть свій відгук:")


@review_router.message(ReviewsForm.review)
async def add_review_action(message: Message, state: FSMContext):
    data = await state.update_data(review=message.text)
    await state.clear()
    msg = reviews.add_review(data.get("review"))
    await message.answer(text=msg)



