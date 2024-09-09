import random

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 11)

def movimento_humano(tabuleiro):
    while True:
        try:
            linha = int(input('Escolha a linha (0, 1, 2): '))
            coluna = int(input('Escolha a coluna (0, 1, 2): '))
            if tabuleiro[linha][coluna] == '   ':
                return linha, coluna
            else:
                print('Essa posição já está ocupada. Tente novamente.')
        except (ValueError, IndexError):
            print('Entrada inválida. Utilize apenas números entre 0 e 2.')

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    if (tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador) or \
       (tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[i][j] != '   ' for i in range(3) for j in range(3))

def movimento_bot(tabuleiro, jogador):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '   ':
                tabuleiro[i][j] = jogador
                if verificar_vitoria(tabuleiro, jogador):
                    tabuleiro[i][j] = '   '
                    return i, j
                tabuleiro[i][j] = '   '

    movimentos_disponiveis = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == '   ']
    return random.choice(movimentos_disponiveis)

tabuleiro = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   ']
]

player = ' X '
bot = ' O '

while True:
    if player == ' X ':
        print(f'Vez do jogador {player.upper()}')
        exibir_tabuleiro(tabuleiro)
        x, y = movimento_humano(tabuleiro)
        tabuleiro[x][y] = player

        if verificar_vitoria(tabuleiro, player):
            exibir_tabuleiro(tabuleiro)
            print(f'Jogador {player.upper()} venceu!')
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('Empate!')
            break

        player = bot
    else:
        print(f'Vez do bot {player.upper()}')
        x, y = movimento_bot(tabuleiro, player)
        tabuleiro[x][y] = player

        if verificar_vitoria(tabuleiro, player):
            exibir_tabuleiro(tabuleiro)
            print(f'Bot {player.upper()} venceu!')
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('Empate!')
            break

        player = ' X '
