import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S State game")
image = "blank_states_img.gif"
screen.addshape(image)  # Any-image file
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    user_answer = screen.textinput(f"{len(guessed_state)}/50 state", "guess states name").title()

    if user_answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("read.csv")
        break
    if user_answer in all_states:
        guessed_state.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)

