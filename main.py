import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess_Indian_States_Game")
image = "map.gif"
screen.addshape(image)
screen.setup(600, 715)
turtle.shape(image)

# For reading the mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


data = pandas.read_csv("states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 28:
    answer = screen.textinput(f"{len(guessed_states)}/28 States Correct",
                              "What's another state name").title()
    # print(answer)

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

