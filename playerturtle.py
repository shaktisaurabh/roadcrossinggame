from turtle import Turtle#from turtle module Turtle class is imported
y_max=280
class player(Turtle):#Turtle is the superclass of player class
    def __init__(self):
        super().__init__()#this initializes every attribute and method of Turtle class to player class
        self.shape('turtle')#now its shape is set to turtle with method shape of Turtle class
        self.penup()#pen is up so that a line is not drawn when the turtle moves forward
        # self.goto(0,-280)
        self.setheading(90)#setheadinng method is used to set direction of Turtle object to north
        self.initial()
    def initial(self):#initial position of Turtle object which it goes to everytime it crosses a level
        self.goto(0,-280)
    def move_player(self):#to move forward
        self.forward(10)
    def y_extent(self):#every time the turtle object goes beyond the position 280 on y-axis,the y_extent method returns True
        if  self.ycor()>y_max:
            return True
        else:
            return False
    

