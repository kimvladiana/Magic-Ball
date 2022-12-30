# Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее.
# Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
from random import choice
import time

answers = ['Бесспорно', 'Предрешено', 'Никаких\nсомнений', 'Определённо\nда', 'Можешь быть\nуверен\nв этом', 'Мне кажется \nда', 'Вероятнее\nвсего', 'Хорошие\nперспективы', 'Знаки говорят\nда', 'Да', 'Даже\nне думай', 'Мой ответ\nнет', 'По моим данным\nнет', 'Перспективы\nне очень\nхорошие', 'Весьма\nсомнительно', 'Пока неясно,\nпопробуй снова', 'Спроси\nпозже', 'Лучше\nне рассказывать', 'Сейчас\nнельзя\nпредсказать', 'Сконцентрируйся\nи спроси опять']

def choice_answer():        # функция для выбора ответа
    time.sleep(0.3)
    global ans_old
    ans_new = ans_old
    while ans_new == ans_old:   # чередование ответа
        ans_new = choice(answers)
    ans_old = ans_new
    canvas.itemconfig(answer, text=ans_old)

def on_restart():       # приветствие
    canvas.itemconfig(answer, text='Добро\nпожаловать!')

root = Tk()     # создание окна
root.title("Magic Ball")        # параметры окна
root.geometry('694x464+600+200')
root.resizable(0, 0)

canvas = Canvas(root, width=700, height=694, highlightthickness=0)  # класс canvas
canvas.pack()

img_obj1 = PhotoImage(file="img/theme.png")        # фон
canvas.create_image(0, 0, anchor=NW, image=img_obj1)

img_obj2 = PhotoImage(file="img/title.png")        # заголовок
canvas.create_image(1, 3, anchor=NW, image=img_obj2)

ans_old = 'Добро\nпожаловать!'      # ответы программы
answer = canvas.create_text(345, 350, text=ans_old, font=("Courier New", 30), fill='white', justify=CENTER, anchor=CENTER)

b1 = Button(root, text='ЗАДАЙ ВОПРОС И НАЖМИ', font=("Courier New", 20), command=choice_answer, bg='#9FEE00', bd=0)      # кнопка генерации нового ответа
b1.place(x=182, y=400, width=330, height=50)

root.mainloop()     # отображение окна и взаимодествие с пользователем