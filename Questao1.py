import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
    # A traffic light is a kind of state machine with three states,
    # Green, Orange, Red. We number these states 0, 1, 2
    # When the machine changes state, we change tess' position and
    # her fillcolor.
    # This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2


    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

    # Bind the event handler to the space key.


def change_to_red():
    tess.fillcolor("red")

def change_to_green():
    tess.fillcolor("green")

def change_to_blue():
    tess.fillcolor("blue")

def aumentar_pen_width():
    auxiliar = tess.shapesize()
    if auxiliar[0] < 20:
        tess.shapesize(stretch_wid=auxiliar[0] + 1)
def diminuir_pen_width():
    auxiliar = tess.shapesize()
    if auxiliar[0] > 1:
        tess.shapesize(stretch_wid=auxiliar[0] - 1)

def change_shape():
    tess.shape("turtle")

def change_background_to_green():
    wn.bgcolor("green")



wn.onkey(advance_state_machine, "space")
wn.onkey(change_to_red, "r")
wn.onkey(change_to_green, "g")
wn.onkey(change_to_blue, "b")
wn.onkey(aumentar_pen_width, "plus")
wn.onkey(diminuir_pen_width, "minus")
wn.onkey(change_shape, "s")
wn.onkey(change_background_to_green, "p")


wn.listen()  # Listen for events
wn.mainloop()

