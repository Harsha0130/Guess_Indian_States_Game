import turtle

screen = turtle.Screen()
screen.title("Guess_Indian_States_Game")
image = "map.gif"
screen.addshape(image)
screen.setup(600,715)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()