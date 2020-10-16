def pesos():
    n = 1
    sum = 0
    while n <= 10 and sum <= 5000:
        peso = float(input("Quanto pesa o artigo? \r\n"))
        sum += peso
        n += 1
    sum /= (n - 1)
    print(f"A média dos pesos é: {sum}")


if __name__ == "__main__":
    pesos()
