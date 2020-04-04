import turtle
import sys

game = turtle.Turtle()
game.hideturtle()
game.width(5)
game.speed(0)
game.pencolor("white")

draw = turtle.Turtle()
draw.hideturtle()
draw.width(5)
draw.speed(0)
draw.pencolor("yellow")

board = turtle.Screen()
board.bgcolor("dark green")


positions = {"centre":[0,0],"right":[90,0],"left":[-90,0],"top":[0,90],"bottom":[0,-90],"top right":[90,90],"top left":[-90,90],"bottom left":[-90,-90],"bottom right":[90,-90]}
perm_pos = {"centre":[0,0],"right":[90,0],"left":[-90,0],"top":[0,90],"bottom":[0,-90],"top right":[90,90],"top left":[-90,90],"bottom left":[-90,-90],"bottom right":[90,-90]}
win_pos = {"centre":"1","right":"2","left":"3","top":"4","bottom":"5","top right":"6","top left":"7","bottom left":"8","bottom right":"9"}

def draw_line(x,y,h):
    draw.up()
    draw.setpos(x,y)
    draw.down()
    draw.seth(h)
    draw.fd(270)

def draw_diagonal(x,y,h):
    draw.up()
    draw.setpos(x,y)
    draw.down()
    draw.seth(h)
    draw.fd(353)

def set_up_game():
    draw_line(-45,135,270)
    draw_line(45,135,270)
    draw_line(-135,45,0)
    draw_line(-135,-45, 0)
    draw.up()
    draw.setpos(0, 0)
    draw.down()

def draw_x():
    game.seth(315)
    game.fd(40)
    game.bk(80)
    game.fd(40)
    game.seth(45)
    game.fd(40)
    game.bk(80)

def draw_o():
    game.up()
    game.setpos(game.xcor() + 25,game.ycor() - 25)
    game.down()
    game.circle(35)

def check_win():
    if win_pos["top left"] == win_pos["top"] == win_pos["top right"] or win_pos["left"] == win_pos["centre"] == win_pos["right"] or win_pos["bottom left"] == win_pos["bottom"] == win_pos["bottom right"] or win_pos["top left"] == win_pos["left"] == win_pos["bottom left"] or win_pos["top"] == win_pos["centre"] == win_pos["bottom"] or win_pos["top right"] == win_pos["right"] == win_pos["bottom right"] or win_pos["top left"] == win_pos["centre"] == win_pos["bottom right"] or win_pos["top right"] == win_pos["centre"] == win_pos["bottom left"]:
        return True
    else:
        return False

set_up_game()
count = 0
win = False
win_player = ""

while win is False:
    if count % 2 == 0:
        pos = input("Input position for x: ")
    else:
        pos = input("Input position for o: ")

    if pos == "end":
        exit()

    if pos in positions:
        xcor = positions[pos][0]
        ycor = positions[pos][1]
        game.up()
        game.setpos(xcor,ycor)
        game.down()
        if count % 2 == 0:
            draw_x()
            win_pos[pos] = "x"
        else:
            draw_o()
            win_pos[pos] = "o"
        count = count + 1
        del positions[pos]
    else:
        print("Position not valid or already filled!")
        pass

    win = check_win()

    if len(positions) == 0:
        break

draw.width(3)
draw.pencolor("orange")

if win is True:
    if win_pos["top left"] == win_pos["top"] == win_pos["top right"] == "x":
        draw_line(perm_pos["top left"][0] - 45, perm_pos["top left"][1], 0)
    elif win_pos["left"] == win_pos["centre"] == win_pos["right"] == "x":
        draw_line(perm_pos["left"][0] - 45, perm_pos["left"][1], 0)
    elif win_pos["bottom left"] == win_pos["bottom"] == win_pos["bottom right"] == "x":
        draw_line(perm_pos["bottom left"][0] - 45, perm_pos["bottom left"][1], 0)
    elif win_pos["top left"] == win_pos["left"] == win_pos["bottom left"] == "x":
        draw_line(perm_pos["top left"][0], perm_pos["top left"][1] + 45, 270)
    elif win_pos["top"] == win_pos["centre"] == win_pos["bottom"] == "x":
        draw_line(perm_pos["top"][0], perm_pos["top"][1] + 45, 270)
    elif win_pos["top right"] == win_pos["right"] == win_pos["bottom right"] == "x":
        draw_line(perm_pos["top right"][0], perm_pos["top right"][1] + 45, 270)
    elif win_pos["top left"] == win_pos["centre"] == win_pos["bottom right"] == "x":
        draw_diagonal(perm_pos["top left"][0] - 35, perm_pos["top left"][1] + 35, 315)
    elif win_pos["top right"] == win_pos["centre"] == win_pos["bottom left"] == "x":
        draw_diagonal(perm_pos["top right"][0] + 35, perm_pos["top right"][1] + 35, 225)

    if win_pos["top left"] == win_pos["top"] == win_pos["top right"] == "o":
        draw_line(perm_pos["top left"][0] - 45, perm_pos["top left"][1], 0)
    elif win_pos["left"] == win_pos["centre"] == win_pos["right"] == "o":
        draw_line(perm_pos["left"][0] - 45, perm_pos["left"][1], 0)
    elif win_pos["bottom left"] == win_pos["bottom"] == win_pos["bottom right"] == "o":
        draw_line(perm_pos["bottom left"][0] - 45, perm_pos["bottom left"][1], 0)
    elif win_pos["top left"] == win_pos["left"] == win_pos["bottom left"] == "o":
        draw_line(perm_pos["top left"][0], perm_pos["top left"][1] + 45, 270)
    elif win_pos["top"] == win_pos["centre"] == win_pos["bottom"] == "o":
        draw_line(perm_pos["top"][0], perm_pos["top"][1] + 45, 270)
    elif win_pos["top right"] == win_pos["right"] == win_pos["bottom right"] == "o":
        draw_line(perm_pos["top right"][0], perm_pos["top right"][1] + 45, 270)
    elif win_pos["top left"] == win_pos["centre"] == win_pos["bottom right"] == "o":
        draw_diagonal(perm_pos["top left"][0] - 35, perm_pos["top left"][1] + 35, 315)
    elif win_pos["top right"] == win_pos["centre"] == win_pos["bottom left"] == "o":
        draw_diagonal(perm_pos["top right"][0] + 35, perm_pos["top right"][1] + 35, 225)

    if count % 2 == 0:
        win_player = "o"
    else:
        win_player = "x"
    print("Game over! Winner is %s!" % win_player)
else:
    print("Game over! No winner!")

turtle.mainloop()
