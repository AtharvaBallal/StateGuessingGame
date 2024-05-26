import turtle
import pandas

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("State Guessing Game")
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:

    answer_state = screen.textinput(f"{len(guessed_state)}/50 States Correct", "What is the state name:").title()
    missing_state = []
    for state in all_state:
        if state not in guessed_state:
            missing_state.append(state)

    pandas.DataFrame(missing_state).to_csv("State to Learn.csv")

    if answer_state == "Exit":
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        tuk = turtle.Turtle()
        tuk.hideturtle()
        tuk.penup()
        state_data = data[data.state == answer_state]
        tuk.goto(int(state_data.x), int(state_data.y))
        tuk.write(answer_state)


turtle.mainloop()
