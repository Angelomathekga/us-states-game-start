import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

# Get the list of states
all_states = df["state"].tolist()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Whats another states name?").title()
    if answer_state == "Exit" :
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in all_states:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = df[df["state"] == answer_state]
            t.goto(int(state_data["x"]),int(state_data["y"]))
            t.write(answer_state)
        


turtle.mainloop()




