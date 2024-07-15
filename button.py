from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_button():
    design = [
        [
            KeyboardButton(text=("Filial 📍")),
            KeyboardButton(text=("Start ✅"))
        ],
        [
            KeyboardButton(text=("Admin 👨🏻‍💻")),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, one_time_keyboard=True, resize_keyboard=True)


def start_button():
    design = [
        [
            KeyboardButton(text=("Woman 🧍‍♀️")),
            KeyboardButton(text=("Men 🧍‍♂️"))
        ],
        [
            KeyboardButton(text=("🔙 back")),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, one_time_keyboard=True, resize_keyboard=True)


def woman_button():
    design = [
        [
            KeyboardButton(text=("1-oy")),
            KeyboardButton(text=("2-oy"))
        ],
        [
            KeyboardButton(text=("3-oy")),
            KeyboardButton(text=("4-oy"))
        ],
        [
            KeyboardButton(text=("🔙 back")),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, one_time_keyboard=True, resize_keyboard=True)


def man_button():
    design = [
        [
            KeyboardButton(text=("1-oy")),
            KeyboardButton(text=("2-oy"))
        ],
        [
            KeyboardButton(text=("3-oy")),
            KeyboardButton(text=("4-oy"))
        ],
        [
            KeyboardButton(text=("🔙 back")),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, one_time_keyboard=True, resize_keyboard=True)

def hafta_button():
    design = [
        [
            KeyboardButton(text=("dushanba")),
            KeyboardButton(text=("seshanba")),
            KeyboardButton(text=("chorshanba"))
        ],
        [
            KeyboardButton(text=("payshanba")),
            KeyboardButton(text=("juma")),
            KeyboardButton(text=("shanba"))
        ],
        [
            KeyboardButton(text=("🔙 back")),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, one_time_keyboard=True, resize_keyboard=True)
