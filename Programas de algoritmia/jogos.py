def jogos():
    min = 24
    mingame = 0
    max = 0
    maxgame = 0
    sum = 0
    for n in range(20):
        start = int(input("Quando começa o jogo? \r\n"))
        end = int(input("Quando acaba o jogo? \r\n"))
        dur = ((24 + end) - start) % 24
        if dur == 0:
            dur = 24
        if dur > max:
            max = dur
            maxgame = n
        if dur < min:
            min = dur
            mingame  = n
        sum += dur
    sum /= 20
    print(f"O jogo que durou mais foi o numero {maxgame} e durou {max} horas,"
          f"O jogo que durou menos foi o numero {mingame} e durou {min} horas,"
          f"Os jogos demoraram em media: {sum}")


if __name__ == "__main__":
    jogos()