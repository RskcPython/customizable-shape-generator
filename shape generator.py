import turtle
screen = turtle.Screen()
#VARIABLES:
sides = 4
# only if sides == 4
rectangleDimY = 0
rectangleDimX = 0

sizeScale = 1
boldness = 1
pointOfOrigin = 0, 0
color = "black"
bgColor = "white"
dotsPerSide = 0
#:VARIABLES
screen.bgcolor(bgColor)
turtle.pensize(boldness)
turtle.pencolor(color)
turtle.color(color)
turtle.penup()
turtle.goto(pointOfOrigin)
turtle.pendown()
counterA = 0
for x in range(sides):
    if dotsPerSide == 0:
        if rectangleDimX == 0 and rectangleDimY == 0:
            turtle.pendown()
            turtle.forward(sizeScale*400/sides)
            turtle.right(360/sides)
        elif counterA == 0:
            turtle.pendown()
            turtle.forward(sizeScale*rectangleDimX)
            turtle.right(360/sides)
            counterA = 1
        else:
            turtle.pendown
            turtle.forward(sizeScale*rectangleDimY)
            turtle.right(360/sides)
            counterA = 0
    elif dotsPerSide > 0:
        if rectangleDimX == 0 and rectangleDimY == 0:
            for x in range(dotsPerSide):
                turtle.pendown()
                turtle.forward(sizeScale*200/sides/dotsPerSide)
                turtle.penup()
                turtle.forward(sizeScale*200/sides/dotsPerSide)
            turtle.right(360/sides)
        elif counterA == 0:
            for x in range(dotsPerSide):
                turtle.pendown()
                turtle.forward(sizeScale/2*rectangleDimX/dotsPerSide)
                turtle.penup()
                turtle.forward(sizeScale/2*rectangleDimX/dotsPerSide)
            turtle.right(360/sides)
            counterA = 1
        else:
            for x in range(dotsPerSide):
                turtle.pendown()
                turtle.forward(sizeScale/2*rectangleDimY/dotsPerSide)
                turtle.penup()
                turtle.forward(sizeScale/2*rectangleDimY/dotsPerSide)
            turtle.right(360/sides)     
            counterA = 0
turtle.hideturtle()
screen.mainloop()