'''
Turtle Game v4.0
Andrew Ault, 3/12/18
Player 1 = Arrow Keys (Kappa)
Player 2 = WASD (Mario)
Collect the coin together then go to the star to move on to the next level!
'''
from turtle import *
from random import *
from wall import *
guardmove = 1
joescore = 0
willscore = 0
turn_speed = 5
forward_speed = 7
speed = 1
screen = Screen()
screen.setup(400,400)
screen.tracer(0)
screen.bgpic("download.jpg")
#Wall Funct
mywall = Wall(screen,100,40,200,20)
# Second Wall
mywall1= Wall(screen,0,-25,150,20)
mywall1.right(90)
# Create Turtle Func
def MakeTurtle(mycolor,myshape,myx,myy,screen):
  temp = Turtle()
  screen.addshape(myshape)
  temp.penup()
  temp.color(mycolor)
  temp.shape(myshape)
  temp.goto(myx,myy)
  return temp
# joe is player 1 Arrows
joe = MakeTurtle("red","kappa.png",-100,-100,screen)
# will is player 2 WASD
will = MakeTurtle("orange","mario.png",-100,100,screen)
# bob is player 1 enemy
bob = MakeTurtle("blue","ghost.png",0,0,screen)
# bill is player 2 enemy
bill = MakeTurtle("yellow","dude.png",0,0,screen)
# goal is the green box
goal = MakeTurtle("green","goal.png",100,100,screen)
# coin is the gold circle on screen
coin = MakeTurtle("gold","circle",100,-100,screen)
# Guard Turtle
guard = MakeTurtle("lime","luigi.jpg",75,75,screen)
# writer is a var that will write score on screen
writer = Turtle()
# reset funct
def reset():
  global joecoins, willcoins, speed, forward_speed, turn_speed
  joecoins = 0
  willcoins = 0
  speed += 0.2
  forward_speed += 1
  turn_speed += 0.5
  joe.goto(-100,-100)
  will.goto(-100,100)
  bob.goto(0,0)
  bill.goto(0,0)
  goal.goto(100,100)
  coin.showturtle()
  coin.goto(randint(-100,100),randint(-100,100))
  screen.bgpic("grass.jpg")
# joe's coins
joecoins = 0
# will's coins
willcoins = 0
writer.penup()
writer.color("yellow")
# Write Score
def writescore():
  writer.clear()
  writer.hideturtle()
  writer.goto(-150,150)
  writer.write("Red Score:" + str(joescore))
  writer.goto(120,150)
  writer.write("Blue Score:" + str(willscore))

def left():
  joe.left(turn_speed) 

def right():
  joe.right(turn_speed)

def gofwd():
  joe.forward(forward_speed)

def wkey():
  will.forward(forward_speed)

def dkey():
  will.right(turn_speed)

def akey():
  will.left(turn_speed)

screen.bgpic("grass.jpg")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(gofwd, "Up")
screen.onkey(wkey, "W")
screen.onkey(dkey, "D")
screen.onkey(akey, "A")
screen.listen()
while True:
  writescore()
  screen.update()
  bob.forward(speed)
  bill.forward(speed)
  bob.setheading(bob.towards(joe.xcor(),joe.ycor()))
  bill.setheading(bill.towards(will.xcor(),will.ycor()))
  #Win for Joe or Will
  if joe.distance(goal) < 15 and joecoins > 0:
    screen.bgcolor("lime")
    reset()
  if will.distance(goal) < 15 and willcoins > 0:
    screen.bgcolor("lime")
    reset() 
  if joe.distance(bob) < 10:
    screen.bgcolor("crimson")
    print("You Lose!")
    break
  if will.distance(bob) < 10:
    screen.bgcolor("crimson")
    print("You Lose!")
    break
  if will.distance(bill) < 10:
    screen.bgcolor("crimson")
    print("You Lose!")
    break
  if joe.distance(bill) < 10:
    screen.bgcolor("crimson")
    print("You Lose!")
    break
  
  if joe.distance(guard) < 20:
    screen.bgcolor("crimson")
    print("You Lose")
    break
  if will.distance(guard) < 20:
    screen.bgcolor("crimson")
    print("You Lose")
    break
  if joe.ycor() > (200):
    joe.goto(joe.xcor(),-190)
  if joe.ycor() < (-200):
    joe.goto(joe.xcor(),180)
  if joe.xcor() > (200):
    joe.goto(-190, joe.ycor())
  if joe.xcor() < (-200):
    joe.goto(180,joe.ycor())
  if will.xcor() > (200):
    will.goto(-190, will.ycor())
  if will.xcor() < (-200):
    will.goto(180,will.ycor())
  if will.ycor() > (200):
    will.goto(will.xcor(),-190)
  if will.ycor() < (-200):
    will.goto(will.xcor(),180)
  # Guard Moving
  guard.forward(1*guardmove)
  if (guard.xcor() < 70):
    guardmove = 1
  if (guard.xcor() > 120):
    guardmove = -1
  #If touching wall
  if mywall.touching(joe): 
    joe.backward(5)
  if mywall.touching(will):
    will.backward(5)
  if mywall1.touching(joe): 
    joe.backward(5)
  if mywall1.touching(will):
    will.backward(5)
  # Collect Coin
  try:
    if joe.distance(coin) < 10:
      joecoins += 1
      joescore += 1
      coin.ht()
      coin.goto(500,500)
    if will.distance(coin) < 10:
      willcoins += 1
      willscore += 1
      coin.ht()
      coin.goto(500,500)
  except:
    pass