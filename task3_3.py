def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск з {source} на {target}: {n}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістити диск з {source} на {target}: {n}")
    hanoi(n - 1, auxiliary, target, source)

def main():
    n = int(input("Введіть кількість дисків: "))
    source = 'A'
    auxiliary = 'B'
    target = 'C'
    initial_state = {source: list(range(n, 0, -1)), auxiliary: [], target: []}
    print(f"Початковий стан: {initial_state}")
    hanoi(n, source, target, auxiliary)
    final_state = {source: [], auxiliary: [], target: list(range(n, 0, -1))}
    print(f"Кінцевий стан: {final_state}")

if __name__ == "__main__":
    main()