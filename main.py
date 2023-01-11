from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)

    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_back_img)


def known_card():
    words_to_learn.remove(current_card)
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- DATA IMPORT------------------------------------ #
try:
    # Import data from CSV
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Create dictionary from original list of words
    word_list = pandas.read_csv("data/german-frequency-words-1-1000.csv")
    words_to_learn = word_list.to_dict(orient="records")
else:
    # Create dictionary from data
    words_to_learn = data.to_dict(orient="records")


# ---------------------------- UI SETUP -------------------------------------- #
# WINDOW
window = Tk()
window.title("German Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# TIMER
flip_timer = window.after(3000, func=flip_card)

# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="img/card_front.png")
card_back_img = PhotoImage(file="img/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 125, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
# Known answer
known_btn_img = PhotoImage(file="img/right.png")
known_btn = Button(image=known_btn_img, highlightthickness=0, command=known_card)
known_btn.grid(column=1, row=1)
# Unknown answer
unknown_btn_img = PhotoImage(file="img/wrong.png")
unknown_btn = Button(image=unknown_btn_img, highlightthickness=0, command=next_card)
unknown_btn.grid(column=0, row=1)

next_card()

window.mainloop()
