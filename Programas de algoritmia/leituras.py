def leituras():
    m = 10
    max = 0
    mmonth = 0
    while m <= 12:
        n = 1
        maxm = 0
        maxnome = ""
        while n <= 3:
            nome = input("Qual o nome do aluno?\r\n")
            num = int(input("Quantos livros leu?\r\n"))
            if num > maxm:
                maxm = num
                maxnome = nome
            n += 1
        if maxm > max:
            max = maxm
            mmonth = m
        print(f"O aluno que leu mais foi o/a {maxnome} e leu {maxm} livros.")
        m += 1
    print(f"No mês {mmonth} leu-se no máximo {max}  livros num mês por um aluno.")


if __name__ == "__main__":
    leituras()