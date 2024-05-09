import turtle

# Функція для рекурсивного малювання кривої Коха
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

# Функція для малювання фракталу «сніжинка Коха»
def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Запит рівня рекурсії у користувача
order = int(input("Введіть рівень рекурсії (мінімум 0): "))

# Малювання фракталу
draw_koch_curve(order)
