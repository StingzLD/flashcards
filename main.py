from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP -------------------------------------- #
# WINDOW
window = Tk()
window.title("German Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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
known_btn = Button(image=known_btn_img, highlightthickness=0, command="")
known_btn.grid(column=1, row=1)
# Unknown answer
unknown_btn_img = PhotoImage(file="img/wrong.png")
unknown_btn = Button(image=unknown_btn_img, highlightthickness=0, command="")
unknown_btn.grid(column=0, row=1)

window.mainloop()
