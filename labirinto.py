# Definindo o labirinto
import heapq


labirinto = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' ', ' '],
    [' ', 'Cat', ' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', 'B']
]

# Posições iniciais
pos_cat = (3, 1)  # Posição do "Cat" no labirinto
pos_bolacha = (5, 6)  # Posição da "Bolacha"

# Movimentos possíveis: cima, baixo, esquerda, direita
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direcoes = ['cima', 'baixo', 'esquerda', 'direita']

# Função para verificar se a posição está dentro dos limites do labirinto
def dentro_do_labirinto(pos, labirinto):
    return 0 <= pos[0] < len(labirinto) and 0 <= pos[1] < len(labirinto[0])

# Função heurística: distância de Manhattan
def heuristica(pos_atual, pos_bolacha):
    return abs(pos_atual[0] - pos_bolacha[0]) + abs(pos_atual[1] - pos_bolacha[1])

# Implementação do algoritmo A* com verificação de obstáculos
def a_star(labirinto, pos_cat, pos_bolacha):
    # Fila de prioridade para os nós a serem explorados (f = g + h)
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, pos_cat, []))  # (f, posição, caminho percorrido)

    # Conjunto para armazenar posições já visitadas
    visitados = set()

    # G - dicionário para armazenar o custo do caminho até cada posição
    g = {pos_cat: 0}

    while fila_prioridade:
        # Pega o nó com o menor f
        _, pos_atual, caminho = heapq.heappop(fila_prioridade)

        # Verifica se chegamos na bolacha
        if pos_atual == pos_bolacha:
            print(f"O 'Cat' encontrou a 'bolacha' em {len(caminho)} movimentos!")
            print(f"Movimentos realizados: {caminho}")
            return True

        # Marca como visitado
        if pos_atual in visitados:
            continue
        visitados.add(pos_atual)

        # Explora os vizinhos
        for i, movimento in enumerate(movimentos):
            nova_posicao = (pos_atual[0] + movimento[0], pos_atual[1] + movimento[1])

            # Verifica se a nova posição é válida e não contém um obstáculo
            if dentro_do_labirinto(nova_posicao, labirinto) and nova_posicao not in visitados:
                if labirinto[nova_posicao[0]][nova_posicao[1]] != 'X':  # Checa obstáculo
                    # Calcula o custo g(novo) e o valor f = g + h
                    g_nova = g[pos_atual] + 1
                    h = heuristica(nova_posicao, pos_bolacha)
                    f_nova = g_nova + h

                    # Adiciona à fila de prioridade
                    heapq.heappush(fila_prioridade, (f_nova, nova_posicao, caminho + [direcoes[i]]))
                    g[nova_posicao] = g_nova

    print("O 'Cat' não conseguiu encontrar a 'bolacha'.")
    return False

# Executa a busca
a_star(labirinto, pos_cat, pos_bolacha)