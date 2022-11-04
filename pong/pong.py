import turtle
import time
import datetime
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer

# score
score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(+350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dk = 5
ball.dy = -5


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0 Player B: 0", align="center",
          font=("Courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dk)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dk += -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dk += -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dk *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dk *= -1

    if(paddle_a.ycor() > 245):
        paddle_a.sety(255)

    if(paddle_a.ycor() < -245):
        paddle_a.sety(-255)

    if(paddle_b.ycor() > 245):
        paddle_b.sety(255)

    if(paddle_b.ycor() < -245):
        paddle_b.sety(-255)

    if(score_a == 1 or score_b == 1):
        if(score_a):
            pen.clear()
            pen.write("Player A is the winner", align="center",
                      font=("Courier", 24, "normal"))
            score_a = 0
            score_b = 0
            total_seconds = 5
            while total_seconds > 0:
                timer = datetime.timedelta(seconds=total_seconds)
                time.sleep(1)
                total_seconds -= 1
                pen.clear()
                pen.write('Ready Round 2', align="center",
                          font=("Courier", 24, "normal"))
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            ball.dk = 7
            ball.dy = -7
            ball.goto(0, 0)
        if(score_b):
            pen.clear()
            pen.write("Player B is the winner", align="center",
                      font=("Courier", 24, "normal"))
            score_a = 0
            score_b = 0
            total_seconds = 5
            while total_seconds > 0:
                timer = datetime.timedelta(seconds=total_seconds)
                time.sleep(1)
                total_seconds -= 1
            pen.clear()
            pen.write('Ready Round 2', align="center",
                      font=("Courier", 24, "normal"))
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            ball.goto(0, 0)
