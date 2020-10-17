import turtle as t
import random as r

playing = True

def up():
      t.setheading(90)
      t.forward(10)
def left():
      t.setheading(180)
      t.forward(10)
def down():
      t.setheading(270)
      t.forward(10)
def right():
      t.setheading(0)
      t.forward(10)
def space():
      t.clear()
def play():
      if playing:
            t.ontimer(play,100)
      if t.distance(ts) <12:
            x = r.randint(-230,230)
            y = r.randint(-230,230)
            ts.goto(x,y)


t.setup(500,500)
t.bgcolor("cyan")
t.shape("triangle")
t.color("blue")

#세모자 먹이
ts = t.Turtle()
ts.shape("turtle")
ts.color("green")
ts.up()
ts.goto(-100,150)



#컨트롤

t.onkeypress(up,"Up")
t.onkeypress(left,"Left")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(space,"space")

t.listen()
play()
