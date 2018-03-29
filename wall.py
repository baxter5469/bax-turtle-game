""" Mr. Riley's Wall class v1.20180310
3/10/2018

How to use this Wall class

1) from wall import *

2) Instanciate the screen. Like this:
    screen = Screen()

3) Instanciate a wall by passing screen, x, y, width, and height. Like this:
    mywall = Wall(screen,0,0,100,10)

4) Use the touching method to determine if another turtle is touching the wall.
  This method is overloaded (there are multiple ways to call it).
    EITHER like this:
      mywall.touching(myturtle)
    OR like this:
      mywall.touching(newx, newy)

5) The wall is a Turtle and can be rotated. Like this:
    EITHER like this:
        mywall.right(45)
    OR like this:
        mywall.setheading(10)

6) The wall is a Turtle and you can change the color. Like this:
    mywall.color("pink")

"""
from turtle import *
import math

class Wall(Turtle):
  def __init__(self,screen,x,y,width,height):
    Turtle.__init__(self)
    self.penup()
    self.goto(x,y)
    self.color('grey')
    self.x = x
    self.y = y
    self.width = float(width)
    self.height = float(height)
    screen.register_shape(str(width)+"x"+str(height),((-height/2,width/2),(height/2,width/2),(height/2,-width/2),(-height/2,-width/2)))
    self.shape(str(width)+"x"+str(height))
    self.right(0)
    
  # getx is a getter method. requires no arguments and returns the x coordinate of the center of the wall as an int.
  def getx(self):
    return self.x
  
  # gety is a getter method. requires no arguments and returns the y coordinate of the center of the wall as an int.
  def gety(self):
    return self.y
  
  # setx is a setter method. requires 1 argument, the new x location.
  def setx(self,x):
    self.x = x
      
  # sety is a setter method. requires 1 argument, the new y location.
  def sety(self,y):
    self.y = y
    
  # touching is a getter method. requires 1 or 2 arguments, either 1 Turtle object or 2 coordinates. returns true or false.
  def touching(self,otherturtle,yloc=None):
    """
    Returns True if another turtle or a point (x,y) is touching the wall.
    This method is overloaded (there are multiple ways to call it)
      EITHER:
        mywall.touching(player1)
      OR:
        mywall.touching(newx, newy)
    """
    # if only one argument was given
    if yloc==None:
      checkx = otherturtle.xcor()
      checky = otherturtle.ycor()
    else: # if two arguments were given
      checkx = otherturtle
      checky = yloc
    # Only do these complex calculation if you are within range of the wall
    if self.distance(checkx,checky) <= math.sqrt(self.width/2 * self.width/2 + self.height/2 * self.height/2):
      # Don't bother with calculating rotation if there is no rotation
      if self.heading == 0:
        return self.x-self.width/2.0 < checkx < self.x+self.width/2.0 and self.y-self.height/2.0 < checky < self.y+self.height/2.0
      else:
        # Rotate point checkx,checky clockwise by a given angle around a given origin.
        # The angle should be given in radians.
        angle = math.radians(self.heading()*-1)
        rotatedx = self.x + math.cos(angle) * (checkx - self.x) - math.sin(angle) * (checky - self.y)
        rotatedy = self.y + math.sin(angle) * (checkx - self.x) + math.cos(angle) * (checky - self.y)
        return self.x-self.width/2.0 < rotatedx < self.x+self.width/2.0 and self.y-self.height/2.0 < rotatedy < self.y+self.height/2.0
    return False