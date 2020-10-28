def testes():
    n = int(input("Alunos na escola:\n"))
    n_masc = 0
    n_fem = 0
    sum_id = 0
    max_id = 0
    max_qt = 0
    i = 0
    while (n_masc + n_fem) < n / 2 and i < n:
        id = int(input("Idade? \n"))
        s = input("Sexo? \n")
        t = input("Resultado? \n")
        if t == "P":
            if id > max_id:
                max_id = id
                max_qt = 1
            elif id == max_id:
                max_qt += 1
            sum_id += id
            if s == "M":
                n_masc += 1
            else:
                n_fem += 1
        i += 1
    if (n_masc + n_fem) < n / 2:
        out = " tendo aberto a escola."
    else:
        out = " nao tendo aberto a escola."

    print(f"Foram testados positivos {n_masc} rapaze(s) e {n_fem} rapariga(s),{out} Em média os alunos que testaram "
          f"positivo tinham a idade de {sum_id / (n_masc + n_fem)}, tendo {max_qt} a idade do aluno mais velho que "
          f"testou posistivo.")


if __name__ == "__main__":
    testes()
