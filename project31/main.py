from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"  # Constant
current_card = {}  # To catch hold of a new value every time next_card() is called
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")  # To read CSV file in a variable
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")  # By using orient-records to convert each(french and english)as key and
# respective values


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # to cancel a window function with a variable
    current_card = random.choice(to_learn)  # Getting random choice from to_learn{dict}
    canvas.itemconfig(card_title, text="French", fill="black")  # change canvas(card_title)text to french(key)
    canvas.itemconfig(card_word, text=current_card["French"])  # change canvas(card_word)text to french[value of french]
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)  # To flip canvas/window after some time period and call the flip_function


def flip_card():
    canvas.itemconfig(card_title, text="English")   # change canvas(card_title)text to English(key)
    canvas.itemconfig(card_word, text=current_card["English"])  # change canvas(card_word)text to English[value of English]
    canvas.itemconfig(card_background, image=card_back_image)  # change background to green ny setting variable to card background


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Padding is used to insert the canvas with space from window
flip_timer = window.after(3000, func=flip_card)  # To flip canvas/window after some time period and call the flip_function


canvas = Canvas(width=800, height=526)  # To get space in the window
card_front_image = PhotoImage(file="./images/card_front.png")  # To open and store in the variable
card_back_image = PhotoImage(file="./images/card_back.png")  # To open and store in the variable
card_background = canvas.create_image(400, 263, image=card_front_image)  # To display image on the canvas
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # To create Text on the canvas with x-y loc
card_word = canvas.create_text(400, 263, text="", font=("Aerial", 60, "bold"))   # To create Text on the canvas with x-y loc
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # bg=remove unwanted Background color in the back,
# highlight thickness to remove thick line in the back
canvas.grid(columnspan=2)  # To increase the width of canvas with respect to right button and grid to display

# Button
cross_image = PhotoImage(file="./images/wrong.png")  # To open and store in the variable
unknown_button = Button(image=cross_image, command=next_card)  # To add button and image to the canvas
unknown_button.grid(row=1, column=0)  # grid to display with specified row and column

check_image = PhotoImage(file="./images/right.png")  # To open and store in the variable
right_button = Button(image=check_image, command=is_known)  # To add button and image to the canvas and to call fun
right_button.grid(row=1, column=1)  # grid to display with specified row and column

next_card()  # we call so that initially we get french(key) and value of french(french["key])

window.mainloop()
