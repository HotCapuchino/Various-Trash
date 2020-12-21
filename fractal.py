import turtle
from tkinter import *
from tkinter.ttk import Combobox

fractals = {
    'Снежинка Коха': ["F--F--F", {"F": "F+F--F+F"}, 60],
    'Кристал': ["F+F+F+F", {"F": "FF+F++F+F"}, 90],
    'Фрактал Вичека': ["F-F-F-F", {"F": "F-F+F+F-F"}, 90],
    'Ковер Серпинского': ["YF", {"X": "YF+XF+Y", "Y": "XF-YF-X"}, 60],
    'Кривая Мура': ["LFL-F-LFL", {"L": "+RF-LFL-FR+", "R": "-LF+RFR+FL-"}, 90],
    'Крест': ["F+F+F+F", {"F": "F+FF++F+F"}, 90],
    'Решетка Серпинского': ["FXF--FF--FF", {"F": "FF", "X": "--FXF++FXF++FXF--"}, 60],
    'Кольца': ["F+F+F+F", {"F": "FF+F+F+F+F+F-F"}, 90],
    'Кривая Пеано-Госпера': ["FX", {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}, 60],
    'Кривая Серпинского': ["F+XF+F+XF", {"X": "XF-F+F-XF+F+XF-F+F-X"}, 90],
    'Анклеты Кришны': [" -X--X", {"X": "XFX--XFX"}, 45],
    'Кривая дракона': ["FX", {"X": "X+YF+", "Y": "-FX-Y"}, 90]
}


def createLSystem(iterations, axiom, rules):
    start_string = axiom
    if iterations == 0:
        return axiom
    end_string = ""
    for step in range(iterations):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def drawLSystem(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def drawFractal(axiom, rules, angle, iterations, length):
    screen.reset()
    mturtle = turtle.Turtle()
    mturtle.pensize(1)
    mturtle.speed(0)
    mturtle.penup()
    mturtle.pendown()
    mturtle.hideturtle()
    mturtle.color('white')
    inst = createLSystem(iterations, axiom, rules)
    drawLSystem(mturtle, inst, angle, length)


def determinateType():
    select_fractal = fractals.get(combobox.get())
    iteration = int(spin1.get())
    length = int(spin2.get())
    drawFractal(select_fractal[0], select_fractal[1], select_fractal[2], iteration, length)


window = Tk()
window.geometry("200x200")
window.title("Fractals")
window.resizable(False, False)
Label(window, text="Chose type:").pack()
combobox = Combobox(window, width=25)
combobox['values'] = ['Снежинка Коха', 'Кристал', 'Фрактал Вичека', 'Ковер Серпинского', 'Кривая Мура', 'Крест',
                      'Решетка Серпинского', 'Кольца', 'Кривая Пеано-Госпера', 'Кривая Серпинского',
                      'Анклеты Кришны', 'Кривая дракона']
combobox.current(0)
combobox.pack(pady=6)
frm1 = Frame(window)
Label(frm1, text="Iterations:").pack()
spin1 = Spinbox(frm1, from_=3, to=15, width=5)
spin1.pack()
frm1.pack()
frm2 = Frame(window)
Label(frm2, text="Size of pic:").pack()
spin2 = Spinbox(frm2, from_=3, to=15, width=5)
spin2.pack()
frm2.pack(pady=6)
Button(window, text="Draw", command=determinateType).pack(pady=10)
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(5 * WIDTH, 5 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)
window.mainloop()
