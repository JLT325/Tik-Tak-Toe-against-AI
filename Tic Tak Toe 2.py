import turtle
import time
import random


row1 = ["Y","Y","Y"]
row2 = ["Y","Y","Y"]
row3 = ["Y","Y","Y"]
column1 = ["Y","Y","Y"]
column2 = ["Y","Y","Y"]
column3 = ["Y","Y","Y"]
diagonal1 = ["Y","Y","Y"]
diagonal2 = ["Y","Y","Y"]
 
boxesFilled = 0
 
screen = turtle.Screen()
screen.setup(600,600)
screen.setworldcoordinates(0, 0, 600, 600)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.forward(595)
turtle.penup()
turtle.goto(0, 400)
turtle.pendown()
turtle.forward(595)
turtle.penup()
turtle.goto(200, 595)
turtle.pendown()
turtle.right(90)
turtle.forward(595)
turtle.penup()
turtle.goto(400, 595)
turtle.pendown()
turtle.forward(595)
def DrawX1():
    global boxesFilled
    turtle.penup()
    turtle.goto(75, 450)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row1[0] = "X"
    column1[0] = "X"
    diagonal1[0] = "X"
    boxesFilled += 1
def DrawX2():
    global boxesFilled
    turtle.penup()
    turtle.goto(270, 450)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row1[1] = "X"
    column2[1] = "X"
    boxesFilled += 1
def DrawX3():
    global boxesFilled
    turtle.penup()
    turtle.goto(485, 450)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row1[2] = "X"
    column3[0] = "X"
    diagonal2[0] = "X"
    boxesFilled += 1
def DrawX4():
    global boxesFilled
    turtle.penup()
    turtle.goto(75, 250)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row2[0] = "X"
    column1[1] = "X"
    boxesFilled += 1
def DrawX5():
    global boxesFilled
    turtle.penup()
    turtle.goto(270, 250)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row2[1] = "X"
    column2[1] ="X"
    diagonal1[1] = "X"
    diagonal2[1] = "X"
    boxesFilled += 1
def DrawX6():
    global boxesFilled
    turtle.penup()
    turtle.goto(485, 250)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row2[2] = "X"
    column3[1] = "X"
    boxesFilled += 1
def DrawX7():
    global boxesFilled
    turtle.penup()
    turtle.goto(75, 50)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row3[0] = "X"
    column1[2] = "X"
    diagonal2[2] = "X"
    boxesFilled += 1
def DrawX8():
    global boxesFilled
    turtle.penup()
    turtle.goto(270, 50)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row3[1] = "X"
    column2[2] = "X"
    boxesFilled += 1
def DrawX9():
    global boxesFilled
    turtle.penup()
    turtle.goto(485, 50)
    turtle.pendown()
    turtle.write("X", move=False, align='left', font=('Arial', 50, 'normal'))
    row3[2] = "X"
    column3[2] = "X"
    diagonal1[2] = "X"
    boxesFilled += 1
 
def DrawO1():
    global boxesFilled
    turtle.penup()
    turtle.goto(75, 450)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row1[0] = "O"
    column1[0] = "O"
    diagonal1[0] = "O"
    boxesFilled +=1
def DrawO2():
    global boxesFilled
    turtle.penup()
    turtle.goto(270, 450)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row1[1] = "O"
    column2[0] = "O"
    boxesFilled += 1
def DrawO3():
    global boxesFilled
    turtle.penup()
    turtle.goto(485, 450)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row1[2] = "O"
    column3[0] = "O"
    diagonal2[0] = "O"
    boxesFilled += 1
def DrawO4():
    global boxesFilled
    turtle.penup()
    turtle.goto(75, 250)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row2[0] = "O"
    column1[1] = "O"
    boxesFilled += 1
def DrawO5():
    global boxesFilled
    turtle.penup()
    turtle.goto(270, 250)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row2[1] = "O"
    column2[1] = "O"
    diagonal1[1] = "O"
    diagonal2[1] = "O"
    boxesFilled += 1
def DrawO6():
    global boxesFilled
    turtle.penup()
    turtle.goto(485, 250)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row2[2] = "O"
    column3[1] = "O"
    boxesFilled += 1
def DrawO7():
    global boxesFilled
    turtle.penup()
    turtle.goto(75, 50)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row3[0] = "O"
    column1[2] = "O"
    diagonal2[2] = "O"
    boxesFilled += 1
def DrawO8():
    global boxesFilled
    turtle.penup()
    turtle.goto(270, 50)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row3[1] = "O"
    column2[2] = "O"
    boxesFilled += 1
def DrawO9():
    global boxesFilled
    turtle.penup()
    turtle.goto(485, 50)
    turtle.pendown()
    turtle.write("O", move=False, align='left', font=('Arial', 50, 'normal'))
    row3[2] = "O"
    column3[2] = "O"
    diagonal1[2] = "O"
    boxesFilled += 1
 
letter = input("Type X to be X, type, O to be O")
if letter == "X":
    computerLetter = "O"
else:
    computerLetter = "X"
 
 
userTurn = 0
 
def randomAINumber():
    #for X's
    computerPosition = random.randint(1, 9)
    if computerPosition == 1 and row1[0] == "Y" and computerLetter == "X":
        DrawX1()
        return 1
    if computerPosition == 2 and row1[1] == "Y" and computerLetter == "X":
        DrawX2()
        return 1
    if computerPosition == 3 and row1[2] == "Y" and computerLetter == "X":
        DrawX3()
        return 1
    if computerPosition == 4 and row2[0] == "Y" and computerLetter == "X":
        DrawX4()
        return 1
    if computerPosition == 5 and row2[1] == "Y" and computerLetter == "X":
        DrawX5()
        return 1
    if computerPosition == 6 and row2[2] == "Y" and computerLetter == "X":
        DrawX6()
        return 1
    if computerPosition == 7 and row3[0] == "Y" and computerLetter == "X":
        DrawX7()
        return 1
    if computerPosition == 8 and row3[1] == "Y" and computerLetter == "X":
        DrawX8()
        return 1
    if computerPosition == 9 and row3[2] == "Y" and computerLetter == "X":
        DrawX9()
        return 1
    #for O's
    if computerPosition == 1 and row1[0] == "Y" and computerLetter == "O":
        DrawO1()
        return 1
    if computerPosition == 2 and row1[1] == "Y" and computerLetter == "O":
        DrawO2()
        return 1
    if computerPosition == 3 and row1[2] == "Y" and computerLetter == "O":
        DrawO3()
        return 1
    if computerPosition == 4 and row2[0] == "Y" and computerLetter == "O":
        DrawO4()
        return 1
    if computerPosition == 5 and row2[1] == "Y" and computerLetter == "O":
        DrawO5()
        return 1
    if computerPosition == 6 and row2[2] == "Y" and computerLetter == "O":
        DrawO6()
        return 1
    if computerPosition == 7 and row3[0] == "Y" and computerLetter == "O":
        DrawO7()
        return 1
    if computerPosition == 8 and row3[1] == "Y" and computerLetter == "O":
        DrawO8()
        return 1
    if computerPosition == 9 and row3[2] == "Y" and computerLetter == "O":
        DrawO9()
        return 1

def AI():
    if row2[1] == "Y" and computerLetter == "X":
        DrawX5()
    elif row2[1] == "Y" and computerLetter == "O":
        DrawO5()
    elif row1[0] == "X" and row1[1] == "X" and row1[2] == "Y" and computerLetter == "O":
        DrawO3()
        X = 1
        return 1
    elif row1[1] == "X" and row1[2] == "X" and row1[0] == "Y" and computerLetter == "O":
        DrawO1()
        X = 1
        return 1
    elif row2[0] == "X" and row2[1] == "X" and row2[2] == "Y" and computerLetter == "O":
        DrawO6()
        X = 1
        return 1
    elif row2[1] == "X" and row2[2] == "X" and row2[0] == "Y" and computerLetter == "O":
        DrawO4()
        X = 1
        return 1
    elif row3[0] == "X" and row3[1] == "X" and row3[2] == "Y"and computerLetter == "O":
        DrawO9()
        X = 1
        return 1
    elif row3[1] == "X" and row3[2] == "X" and row3[0] == "Y"and computerLetter == "O":
        DrawO7()
        X = 1
        return 1
    elif column1[0] == "X" and column1[1] == "X" and column1[2] == "Y" and computerLetter == "O":
        DrawO7()
        X = 1
        return 1
    elif column1[1] == "X" and column1[2] == "X" and column1[0] == "Y" and computerLetter == "O":
        DrawO1()
        X = 1
        return 1
    elif column2[0] == "X" and column2[1] == "X" and column2[2] == "Y" and computerLetter == "O":
        DrawO8()
        X = 1
        return 1
    elif column2[1] == "X" and column2[2] == "X" and column2[0] == "Y" and computerLetter == "O":
        DrawO2()
        X = 1
        return 1
    elif column3[0] == "X" and column3[1] == "X" and column3[2] == "Y" and computerLetter == "O":
        DrawO9()
        X = 1
        return 1
    elif column3[1] == "X" and column3[2] == "X" and column3[0] == "Y" and computerLetter == "O":
        DrawO3()
        X = 1
        return 1
    elif diagonal1[0] == "X" and diagonal1[1] == "X" and diagonal1[2] == "Y" and computerLetter == "O":
        DrawO9()
        X = 1
        return 1
    elif diagonal1[1] == "X" and diagonal1[2] == "X" and diagonal1[0] == "Y" and computerLetter == "O":
        DrawO1()
        X = 1
        return 1
    elif diagonal2[2] == "X" and diagonal2[1] == "X" and diagonal2[0] == "Y" and computerLetter == "O":
        DrawO3()
        X = 1
        return 1
    elif diagonal2[1] == "X" and diagonal2[0] == "X" and diagonal2[2] == "Y" and computerLetter == "O":
        DrawO7()
        X = 1
        return 1
    #O's after here
    elif row1[0] == "O" and row1[1] == "O" and row1[2] == "Y" and computerLetter == "X":
        DrawX3()
        X = 1
        return 1
    elif row1[1] == "O" and row1[2] == "O" and row1[0] == "Y" and computerLetter == "X":
        DrawX1()
        X = 1
        return 1
    elif row2[0] == "O" and row2[1] == "O" and row2[2] == "Y" and computerLetter == "X":
        DrawX6()
        X = 1
        return 1
    elif row2[1] == "O" and row2[2] == "O" and row2[0] == "Y" and computerLetter == "X":
        DrawX4()
        X = 1
        return 1
    elif row3[0] == "O" and row3[1] == "O" and row3[2] == "Y" and computerLetter == "X":
        DrawX9()
        X = 1
        return 1
    elif row3[1] == "O" and row3[2] == "O" and row3[0] == "Y" and computerLetter == "X":
        DrawX7()
        X = 1
        return 1
    elif column1[0] == "O" and column1[1] == "O" and column1[2] == "Y" and computerLetter == "X":
        DrawX7()
        X = 1
        return 1
    elif column1[1] == "O" and column1[2] == "O" and column1[0] == "Y" and computerLetter == "X":
        DrawX1()
        X = 1
        return 1
    elif column2[0] == "O" and column2[1] == "O" and column2[2] == "Y" and computerLetter == "X":
        DrawX8()
        X = 1
        return 1
    elif column2[1] == "O" and column2[2] == "O" and column2[0] == "Y" and computerLetter == "X":
        DrawX2()
        X = 1
        return 1
    elif column3[0] == "O" and column3[1] == "O" and column3[2] == "Y" and computerLetter == "X":
        DrawX9()
        X = 1
        return 1
    elif column3[1] == "O" and column3[2] == "O" and column3[0] == "Y" and computerLetter == "X":
        DrawX3()
        X = 1
        return 1
    elif diagonal1[0] == "O" and diagonal1[1] == "O" and diagonal1[2] == "Y" and computerLetter == "X":
        DrawX9()
        X = 1
        return 1
    elif diagonal1[1] == "O" and diagonal1[2] == "O" and diagonal1[0] == "Y" and computerLetter == "X":
        DrawX1()
        X = 1
        return 1
    elif diagonal2[2] == "O" and diagonal2[1] == "O" and diagonal2[2] == "Y" and computerLetter == "X":
        DrawX3()
        X = 1
        return 1
    elif diagonal2[1] == "O" and diagonal2[0] == "O" and diagonal2[0] == "Y" and computerLetter == "X":
        DrawX7()
        X = 1    
        return 1
    else:
        did_Draw = 0
        while did_Draw != 1:
            did_Draw = randomAINumber()
            return 1

   
 
def outcome():
    global X
    if row1[0] == "X" and row1[1] == "X" and row1[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif row1[0] == "O" and row1[1] == "O" and row1[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif column1[0] == "X" and column1[1] == "X" and column1[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column2[0] == "X" and column2[1] == "X" and column2[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column3[0] == "X" and column3[1] == "X" and column3[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif column1[0] == "O" and column1[1] == "O" and column1[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column2[0] == "O" and column2[1] == "O" and column2[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column3[0] == "O" and column3[1] == "O" and column3[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif diagonal1[0] == "X" and diagonal1[1] == "X" and diagonal1[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif diagonal2[0] == "X" and diagonal2[1] == "X" and diagonal2[2] == "X" and letter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif diagonal1[0] == "O" and diagonal1[1] == "O" and diagonal1[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif diagonal2[0] == "O" and diagonal2[1] == "O" and diagonal2[2] == "O" and letter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("You Win!", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    #After this the if statments are for loosing
    elif row1[0] == "X" and row1[1] == "X" and row1[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif row1[0] == "O" and row1[1] == "O" and row1[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif column1[0] == "X" and column1[1] == "X" and column1[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column2[0] == "X" and column2[1] == "X" and column2[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column3[0] == "X" and column3[1] == "X" and column3[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif column1[0] == "O" and column1[1] == "O" and column1[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column2[0] == "O" and column2[1] == "O" and column2[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif column3[0] == "O" and column3[1] == "O" and column3[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif diagonal1[0] == "X" and diagonal1[1] == "X" and diagonal1[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif diagonal2[0] == "X" and diagonal2[1] == "X" and diagonal2[2] == "X" and computerLetter == "X":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
    elif diagonal1[0] == "O" and diagonal1[1] == "O" and diagonal1[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    elif diagonal2[0] == "O" and diagonal2[1] == "O" and diagonal2[2] == "O" and computerLetter == "O":
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(85, 300)
        turtle.pendown()
        turtle.write("You Lose :(", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
    # If tie
    elif boxesFilled == 9:
        time.sleep(1)
        turtle.clearscreen()
        turtle.penup()
        turtle.goto(150, 300)
        turtle.pendown()
        turtle.write("It's a tie", move=False, align='left', font=('Arial', 100, 'normal'))
        X = 1
 
 
 
       
   
X = outcome()
while X != 1:
    position = input("Choose a box to put your letter in")
    userTurn += 1
    if position == "1" and row1[0] == "Y":
        if letter == "X":
            DrawX1()
            row1[0] = "X"
            column1[0] = "X"
            diagonal1[0] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO1()
            row1[0] = "O"
            column1[0] = "O"
            diagonal1[0] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "2" and row1[1] == "Y":
        if letter == "X":
            DrawX2()
            row1[1] = "X"
            column2[0] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO2()
            row1[1] = "O"
            column2[0] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "3" and row1[2] == "Y":
        if letter == "X":
            DrawX3()
            row1[2] = "X"
            column3[0] = "X"
            diagonal2[0] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO3()
            row1[2] = "O"
            column3[0] = "O"
            diagonal2[0] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "4" and row2[0] == "Y":
        if letter == "X":
            DrawX4()
            row2[0] = "X"
            column1[1] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO4()
            row2[0] = "O"
            column1[1] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "5" and row2[1] == "Y":
        if letter == "X":
            DrawX5()
            row2[1] = "X"
            column2[1] = "X"
            diagonal1[1] = "X"
            diagonal2[1] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO5()
            row2[1] = "O"
            column2[1] = "O"
            diagonal1[1] = "O"
            diagonal2[1] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "6" and row2[2] == "Y":
        if letter == "X":
            DrawX6()
            row2[2] = "X"
            column3[1] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO6()
            row2[2] = "O"
            column3[1] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "7" and row3[0] == "Y":
        if letter == "X":
            DrawX7()
            row3[0] = "X"
            column1[2] = "X"
            diagonal2[2] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO7()
            row3[0] = "O"
            column1[2] = "O"
            diagonal2[2] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "8" and row3[1] == "Y":
        if letter == "X":
            DrawX8()
            row3[1] = "X"
            column2[2] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO8()
            row3[1] = "O"
            column2[2] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    if position == "9" and row3[2] == "Y":
        if letter == "X":
            DrawX9()
            row3[2] = "X"
            column3[2] = "X"
            diagonal1[2] = "X"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
        else:
            DrawO9()
            row3[2] = "O"
            column3[2] = "O"
            diagonal1[2] = "O"
            time.sleep(5)
            outcome()
            if X != 1:
                AI()
    outcome()
exit = input("press any key to exit")