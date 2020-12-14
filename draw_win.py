import turtle


def draw():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-300, -300, 300, 300)
    t.color('deep pink')
    style = ('Courier', 60, 'italic')
    t.write('You Win!!', font=style, align='center')
    turtle.hideturtle()
    wn.exitonclick()


def main():
    draw()


if __name__ == "__main__":
    main()
