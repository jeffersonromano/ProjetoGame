# Projeto Game Quiz para conclusão da disciplina de Programação I - Python
# da Universidade Federal Ruaral de Pernambuco - UFRPE
# Aluno: Jefferson Romano
# Data: 16-09-2022
# Versão: 0.1

# libs

# Apresentação do programa ao usuário
print(
    '\nBem-vindo ao Quiz Rural!!!\nResponda as perguntas e ganhe pontos! O objetivo é ficar entre os primeiros no ranking geral!\nVamos nessa!'
)


#nomeJogador = input('Digite seu nome: ')
# Lendo as perguntas de um arquivo externo. As perguntas e respostas estão separadas
# pelo caractere | (pipe)
with open("base-de-perguntas-e-respostas.txt", encoding='utf-8') as f:
    # Criando um array com os dados de uma linha e quebrando em valores com a função split
    listaDePerguntas = [line.split("|") for line in f]

# Criar um contador para identificar a ordem da questão no dicionário "perguntas"
count = 1
perguntas = {}

# Incrementando o dicionário
for x in listaDePerguntas:
    # Criando a chave com numeração para cada pergunta.
    # Usando a função strip() para remover espaços em branco antes e depois do valor, pois na comparação com a resposta do usuário (linha 55) dá falha
    perguntas['Pergunta ' + str(count)] = {
        'pergunta': x[0],
        'respostas': {
            'a': x[1].strip(),
            'b': x[2].strip(),
            'c': x[3].strip()
        },
        'respostaCerta': x[4].strip()
    }
    count += 1

# Variável para contabilizar os acertos
totalAcertos = 0

# Utilzando um for para percorrrer as perguntas e suas respectivas respostas, onde pk se refere a chave da pergunta e pv ao valor da pergunta dentro do dicionário "perguntas"
for pk, pv in perguntas.items():
  # Listando a pergunta
  print(f'\n{pk}: {pv["pergunta"]}\n')
  print(pv['respostaCerta'])
  # listando as respostas da pergunta
  for rk, rv in pv['respostas'].items():
    print(f'{rk}){rv}')

  # Obtendo a resposta do usuário em cada pergunta
  respostaUsuario = input('\nDigite a letra correspondente a sua resposta: ')

  #print(type(pv['respostaCerta']))
  #print(type(respostaUsuario))

  # verificando se o usuário acertou ou não e dando feedback imediato
  if respostaUsuario.lower() == pv['respostaCerta']:
    totalAcertos += 1
    print("Aaaaaaacertou, miseravi!!!")
  else:
    print("Êeeeeeerrou!!! Que merda hein?! Sabia não :(")

pontosDaRodada = 0
PerguntasPorRodada = 5
contador = 0
