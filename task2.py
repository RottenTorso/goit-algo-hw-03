import turtle
import argparse

def koch_snowflake(t, order, size):
    """
    Рекурсивна функція для малювання однієї сторони сніжинки Коха.
    
    t: об'єкт turtle
    order: рівень рекурсії
    size: довжина сторони
    """
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_snowflake(t, order-1, size)
        t.left(60)
        koch_snowflake(t, order-1, size)
        t.right(120)
        koch_snowflake(t, order-1, size)
        t.left(60)
        koch_snowflake(t, order-1, size)

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Малювання фракталу 'сніжинка Коха'.")
    parser.add_argument("order", type=int, help="Рівень рекурсії")
    args = parser.parse_args()

    order = args.order

    # Налаштування turtle
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-200, 100)  # Початкова позиція
    t.pendown()

    size = 400  # Розмір сніжинки

    # Малювання трьох сторін сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    turtle.done()  # Завершення малювання

if __name__ == "__main__":
    main()