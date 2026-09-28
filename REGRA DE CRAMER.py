print('=== Regra de Cramer ===')

while True:
    try:
        linhas = int(input('Digite o número de linhas da matriz: '))
        colunas = int(input('Digite o número de colunas da matriz: '))

        if linhas <= 0 or colunas <= 0:
            print('\033[31mO número de linhas e colunas deve ser positivo. Tente novamente.\033[0m')
            continue

        if linhas != colunas:
            print('\033[31mA matriz deve ser quadrada. Tente novamente.\033[0m')
            continue

        break

    except ValueError:
        print('\033[31mEntrada inválida. Por favor, digite números inteiros.\033[0m')


n = linhas

print(f'Digite os elementos da matriz {n}x{n}:')
Matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        while True:
            try:
                elemento = float(input(f'Digite o elemento [{i+1}][{j+1}]: '))
                break

            except ValueError:
                print('\033[31mEntrada inválida. Digite um número.\033[0m')

        linha.append(elemento)

    Matriz.append(linha)

print('Digite os elementos dos termos independentes:')
b = []

for i in range(n):
    while True:
        try:
            elemento = float(input(f'Digite o elemento b[{i+1}]: '))
            break

        except ValueError:
            print('\033[31mEntrada inválida. Digite um número.\033[0m')

    b.append(elemento)

copia = [linha[:] for linha in Matriz]
d = 1.0

for coluna in range(n):

    if copia[coluna][coluna] == 0:
        for outra_linha in range(coluna + 1, n):
            if copia[outra_linha][coluna] != 0:
                copia[coluna], copia[outra_linha] = copia[outra_linha], copia[coluna]
                d *= -1
                break

    pivo = copia[coluna][coluna]

    if pivo == 0:
        d = 0
        break

    d *= pivo

    for outra_linha in range(coluna + 1, n):
        fator = copia[outra_linha][coluna] / pivo

        for j in range(coluna, n):
            copia[outra_linha][j] -= fator * copia[coluna][j]

print(f'\033[1m\nDeterminante da matriz:\033[0m {d}')

if d == 0:
    print('\033[31mA Regra de Cramer não pode ser aplicada, pois D = 0.\033[0m')

else:

    determinantes = []

    for coluna in range(n):

        copia = [linha[:] for linha in Matriz]

        for i in range(n):
            copia[i][coluna] = b[i]

        determinante = 1.0

        for coluna2 in range(n):

            if copia[coluna2][coluna2] == 0:
                for outra_linha in range(coluna2 + 1, n):
                    if copia[outra_linha][coluna2] != 0:
                        copia[coluna2], copia[outra_linha] = copia[outra_linha], copia[coluna2]
                        determinante *= -1
                        break

            pivo = copia[coluna2][coluna2]

            if pivo == 0:
                determinante = 0
                break

            determinante *= pivo

            for outra_linha in range(coluna2 + 1, n):
                fator = copia[outra_linha][coluna2] / pivo

                for j in range(coluna2, n):
                    copia[outra_linha][j] -= fator * copia[coluna2][j]

        determinantes.append(determinante)

    print('\033[36m\nDeterminantes:\033[0m')

    for i in range(n):
        print(f'\033[1mD{i + 1} = \033[0m {determinantes[i]}')

    print('\033[36m\nSolução do sistema:\033[0m')

    for i in range(n):
        resultado = determinantes[i] / d
        print(f'\033[1mx{i + 1} = \033[0m{resultado}')
        