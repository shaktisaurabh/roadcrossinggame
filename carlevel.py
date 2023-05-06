from turtle import Turtle
class level(Turtle):#Turtle is superclass here too
    def __init__(self):
        super().__init__()#this helps the level class take up all the attributes and methods of the Turtle class
        self.color('black')#the color of Turtle object is set to black using the method color
        self.level=1#the level attribute is set to 1 
        self.penup()#pen is held up now so that a line is not drawn behind while Turtle object moves ahead
        self.hideturtle()#now Turtle object itself is hidden
        self.goto(-280,250)#and the Turtle is now set at a particular position -280 at x-axis and 250 at y-axis
        self.update_score()
    def update_score(self):
        self.clear()#now the turtle object is cleared first,this is done so that the incremented level doesnot get written over the previous one
        #and it gets cleared before being written again
        self.write(f"Level:{self.level}",align="center",font=("Courier",24,"normal"))#this is how we write
    def game_stop(self):
        self.goto(0,0)#when game stops the below gets written on position 0,0
        self.write("Game over",align="center",font=("Courier",24,"normal"))
    def increment_score(self):
        self.level+=1#level is increased by 1 each time
        self.update_score()#and this function is called every time