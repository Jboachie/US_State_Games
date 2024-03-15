import turtle
import pandas
from state_names import Statenames
state = Statenames()
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
answer_guesses = []
turtle.shape(image)
game_is_on = True
data = pandas.read_csv("50_states.csv")
allstates = data.state.to_list()
while game_is_on:
    answer_state = screen.textinput(title = f"{len(answer_guesses)}/50 States correct", prompt= "What's another state name? (type 'exit' to quit)")
    answer = answer_state.title()
    if answer == 'Exit':
        game_is_on = False
        df = pandas.DataFrame(allstates)
        df.to_csv("states_to_learn.csv")
    for country in allstates:
        if answer == country:
            answer_guesses.append(answer)
            allstates.remove(answer)
            answercor = data[data.state == answer]
            row_number = data.index[data["state"] == answer][0]
            xcor = answercor.x[row_number]
            ycor = answercor.y[row_number]
            state.state_name(answer, xcor, ycor)
        elif len(answer_guesses) > 50:
            game_is_on = False


























