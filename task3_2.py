import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    # Введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна та вивіду
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Сніжинка Коха")

    # Створення об'єкту черепашки
    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість

    # Позиціонування черепашки
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, level, 300)
        t.right(120)

    # Закриття вікна при кліку
    wn.exitonclick()

if __name__ == "__main__":
    main()