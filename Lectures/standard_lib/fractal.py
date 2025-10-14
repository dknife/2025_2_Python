
import turtle as t
import math

def draw_branch(length, reduce_rate, angle, depth = 1) :

    if depth <= 0 :
        return

    # 현재 가지
    t.pendown()
    t.forward(length)
    t.penup()

    # 왼쪽 가지 호출
    t.left(angle)
    draw_branch(length * (1-reduce_rate), reduce_rate, angle, depth - 1)
    

    # 오른쪽 가지 호출
    t.right(angle + angle)
    draw_branch(length * (1-reduce_rate), reduce_rate, angle, depth - 1)
    
    # 돌아오기
    t.left(angle)
    t.backward(length)


#### 그림 그리기

t.setup(width = 800, height = 600)
t.speed(0)
t.tracer(0,0)
t.bgcolor('black')
t.pencolor('yellow')

t.penup()
t.goto(0, -200)
t.setheading(90)

draw_branch(50, 0.1, 15, depth=15)

t.done()

    

    
