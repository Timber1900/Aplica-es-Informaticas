def soma():
    n = int(input("Quantos números queres somar?\r\n"))
    sum = 0
    sumpos = 0
    count = 0
    min = 0
    max = 0
    for i in range(n):
        number = int(input("Dá-me um número\r\n"))
        if i == 1:
            min = number
            max = number
        if number < min:
            min = number
        if number > max:
            max = number
        sum += number
        if number >= 0:
            sumpos += number
        else:
            count += 1
    print(f"A soma de todos os números é: {sum}, \r\n"
          f"A soma de todos os números positivos é: {sumpos}, \r\n"
          f"O maior número lido é: {max}, \r\n"
          f"O menor número lido é: {min}, e houveram {count} números negativos.")


if __name__ == '__main__':
    soma()

