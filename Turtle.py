from turtle import Turtle, Screen
wn = Screen()
emma = Turtle()
emma.speed(10)

emma.right(90)
    
for _ in range(3):
    for _ in range(2):    
        emma.forward(50)

        for _ in range(3):
            emma.left(90)
            emma.forward(50)
            
        for _ in range(2):
            emma.right(120)
            emma.forward(50)

        for _ in range(3):
            emma.left(30)
            emma.forward(50)
            emma.right(120)
            emma.forward(50)
            
        emma.left(60)
    emma.left(60)

wn.exitonclick()