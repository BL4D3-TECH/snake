#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : BL4D3
# Created Date: 10/07/2022
# version ='1.1'
# ---------------------------------------------------------------------------
"""tipical snake game"""
# ---------------------------------------------------------------------------
# Import: turtle, time, random
# ---------------------------------------------------------------------------
import turtle
import time
import random

while True:
    #ventana
    wn = turtle.Screen()
    wn.title('Snake')
    wn.bgcolor('black')
    wn.setup(width = 600, height = 600)
    wn.tracer(0)

    #serpiente
    snake = turtle.Turtle()
    snake.speed('fast')
    snake.shape("square")
    snake.color('#123F12')
    snake.penup()
    snake.goto(0, 0)
    snake.direction = 'stop'

    #lapiz
    lapiz = turtle.Turtle()
    lapiz.speed(0)
    lapiz.penup()
    lapiz.ht()
    lapiz.color('red')
    lapiz.goto(0, 0)

    #manzanas
    apple = turtle.Turtle()
    apple.shape('circle')
    apple.color('red')
    apple.penup()
    #funcion de movimiento apple
    def applemov():
        apple.goto(x, y)
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    applemov()
    #funciones de movimiento snake
    def up():
        snake.direction = 'up'
    def down():
        snake.direction = 'down'
    def izda():
        snake.direction = 'izquierda'
    def dcha():
        snake.direction = 'derecha'
    def move():
        if snake.direction == 'up':
            y = snake.ycor()
            snake.sety(y + 20)
        elif snake.direction == 'down':
            y = snake.ycor()
            snake.sety(y - 20)
        elif snake.direction == 'izquierda':
            x = snake.xcor()
            snake.setx(x - 20)
        elif snake.direction == 'derecha':
            x = snake.xcor()
            snake.setx(x + 20)

    segmentos = []

    #score
    score = 0

    #funciones segmentos
    def new_s():
        segmento = turtle.Turtle()
        segmento.shape('square')
        segmento.color('green')
        segmento.penup()
        segmentos.append(segmento)

    #bucle principal
    while True:
        wn.update()
        if snake.distance(apple) < 20:
            apple.ht()
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            applemov()
            apple.st()
            new_s()
            score += 1
        total_seg = len(segmentos)
        for i in range(total_seg -1, 0, -1):
            x = segmentos[i - 1].xcor()
            y = segmentos[i - 1].ycor()
            segmentos[i].setx(x)
            segmentos[i].sety(y)
        if total_seg > 0:
            x = snake.xcor()
            y = snake.ycor()
            segmentos[0].goto(x, y)
        wn.listen()
        wn.onkeypress(up, 'Up')
        wn.onkeypress(down, 'Down')
        wn.onkeypress(izda, 'Left')
        wn.onkeypress(dcha, 'Right')
        move()
        time.sleep(0.1)
        for _ in segmentos:
            if snake.distance(_) < 20:
                snake.sety(320)
        if snake.ycor() < -280 or snake.ycor() > 280:
            snake.ht()
            for o in segmentos:
                o.ht()
            apple.ht()
            lapiz.color('red')
            lapiz.goto(0, 0)
            lapiz.write('GAME OVER', align = 'center', font = ('coursair', 50))
            lapiz.goto(0, -50)
            lapiz.color('red')
            lapiz.write('espere...', align = 'center', font = ('coursair', 25))
            time.sleep(1)
            wn.clear()
            break
        elif snake.xcor() < -280 or snake.xcor() > 280:
            snake.ht()
            for o in segmentos:
                o.ht()
            apple.ht()
            lapiz.color('red')
            lapiz.goto(0, 0)
            lapiz.write('GAME OVER', align = 'center', font = ('coursair', 50))
            lapiz.goto(0, -50)
            lapiz.color('red')
            lapiz.write('espere...', align = 'center', font = ('coursair', 25))
            time.sleep(1)
            wn.clear()
            break
        lapiz.goto(0, 255)
        lapiz.color('#000000')
        lapiz.write(f'score = {score - 1}', align = 'center', font = ('coursair', 24, 'normal'))
        lapiz.color('#ffffff')
        lapiz.write(f'score = {score}', align = 'center', font = ('coursair', 24, 'normal'))