from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="BREAK", fg=RED)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = int(reps/2)
        for _ in range(work_session):
            marks += "✓"
            label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="PINK")


label = Label(text="Timer", fg="GREEN", font=(FONT_NAME, 50), bg="PINK")
label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg="PINK", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(row=2, column=2)


check_marks = Label(fg="GREEN", bg="PINK")
check_marks.grid(column=1, row=3)

window.mainloop()
