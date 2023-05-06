from turtle import Screen#Screen class is extracted from turtle module
from carcreation import createcars#createcars class is extracted from carcreation module
from playerturtle import player#player class is extracted from playerturtle module
from carlevel import level#level class is extracted from carlevel module
import time#time module
s=Screen()#s is a object of Screen class
s.setup(width=600,height=600)#using setup method,the height and width of the Screen object s is set
s.bgcolor("white")#using bgcolor method of Screen class whose object is s,the background color is set to white
s.title("Turtleroadcrossing")#the title of the Screen object of which s is a class is set to "Turtleroadcrossing"
s.tracer(0)#now any changes in Screen object whose s is an object is stopped,by using tracer method 
c=createcars()#c is a object of createcars class
p=player()#p is a object of player class
l=level()#l is a object of level class
is_on=True
s.listen()#now listen method of s object is invoked to listen to any keyboard press events
s.onkey(p.move_player,"Up")#as soon as Up key is pressed from keyboard the move_player method of p object is called
# s.update()
while is_on:
    time.sleep(0.1)#this loop will create cars after every 0.1 seconds,this update after every 0.1 second delay allows the cars to be created at a much lesser pace and
    #the use of random randint module in creation of cars within createcars() module ensures that the entire screen across y-axis is not filled with cars
    s.update()#then update the changes
    c.create_cars()#now create_cars method of c object is called to create a rectangualr shape turtle object and place that in an array
    c.move()#and then every object present in the list car_len is moved by ome places
    for caru in c.car_len:#then this for loop loops through every item of car_len list
        if caru.distance(p)<20:#if the distance between any car object and player object is less than 20
            l.game_stop()#then game_stop method of l object is called
            is_on=False#and while loop is exited
    if p.y_extent():#secondly when this condition holds true
        p.initial()#then initial method of p object is called
        l.increment_score()#increment_score method of l object is called
        c.increment_speed()#increment_speed method of c object is called



s.exitonclick()#the screen will get exited when any button on the keyboard is clicked