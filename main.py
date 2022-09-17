# Projeto Game Quiz para conclusão da disciplina de Programação I - Python
# da Universidade Federal Ruaral de Pernambuco - UFRPE
# Aluno: Jefferson Romano
# Data: 16-09-2022
# Versão: 0.1

# imports libs
import random
from replit import audio



# Lista de variáveis
listaDePerguntas = []
listaDePerguntasRS = []
perguntas = {}

def limparPerguntas():
  perguntas.clear()
  return perguntas
  
def adicionarPergunta():
  pergunta = input('Digite a pergunta seguida de ponto de interrogação (?):')
  alternativa1 = input('Digite o texto da alternativa a): ')
  alternativa2 = input('Digite o texto da alternativa b): ')
  alternativa3 = input('Digite o texto da alternativa c): ')
  alternativaCorreta = input('Digite a letra da alternativa correta: ')
  nivelPergunta = input('Qual o nível da pergunta? Digite: f=fácil, m=médio e d=difícil: ')

  line = pergunta + "|" + alternativa1 + "|" + alternativa2 + "|" + alternativa3 + "|" + alternativaCorreta + "|" + nivelPergunta + "\n"
  # Abrir arquivo para inclusão
  with open("base-de-perguntas-e-respostas.txt", 'a') as f:
    f.write(line)

  carregarPerguntas()

def carregarPerguntas(nivel = 'f'):
  
  # Lendo as perguntas de um arquivo externo. As perguntas e respostas estão separadas
  # pelo caractere | (pipe)
  with open("base-de-perguntas-e-respostas.txt", encoding='utf-8') as f:
    # Criando um array com os dados de uma linha e quebrando em valores com a função split
    listaDePerguntas = [line.split("|") for line in f]
    #print(listaDePerguntas)
    
    listaPorNivel = [x for x in listaDePerguntas if x[5].strip() == nivel]
    
    #print(listaPorNivel)
    
    # Sorteando perguntas
    listaDePerguntasRS = random.sample(listaPorNivel, len(listaPorNivel))

  # Criar um contador para identificar a sequência das questões no dicionário "perguntas"
  count = 1
  
  # Alimentando o dicionário
  for x in listaDePerguntasRS:
    # Criando a chave com numeração para cada pergunta.
    # Usando a função strip() para remover espaços em branco antes e depois do valor, 
    #pois na comparação com a resposta do usuário (linha 55) dá falha
    perguntas['Pergunta ' + str(count)] = {
        'pergunta': x[0],
        'respostas': {
            'a': x[1].strip(),
            'b': x[2].strip(),
            'c': x[3].strip()
        },
        'respostaCerta': x[4].strip(),
        'nivel': x[5].strip()
    }
    count += 1
  #return print(perguntas)
  return perguntas

def jogar():

  source = audio.play_file('epic_battle_music_1-6275.mp3')

  print('\nIniciando partida!\n')
  nivel = input('Qual o nível de dificuldade desejado?\n(f=fácil, m=médio e d=difícil): ')
  
  perguntas = carregarPerguntas(nivel)
  
  # Apresentação do programa ao usuário
  print(
    '\nBem-vindo ao Quiz Rural!!!\nResponda as perguntas e ganhe pontos!\nO objetivo é ficar entre os primeiros no ranking geral!\nVamos nessa!'
  )

  # Identificando o jogador
  nomeJogador = input('Digite seu nome: ')
  
  totalAcertos = 0
  contador = 0

  # Utilzando um for para percorrrer as perguntas e suas respectivas respostas, 
  #onde pk se refere a chave da pergunta e pv ao valor da pergunta dentro do dicionário "perguntas"
  #print(perguntas)
  for pk, pv in perguntas.items():
    #print(len(perguntas))
    #print(contador)
    
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
  
    contador += 1
    # Gravando o ranking da partida
    if contador == len(perguntas):
      # Percentual de acertos
      #percentualAcertos = totalAcertos / qtdPerguntas * 100
      #print("\nPercentual de acerto: {:.2f}%".format(percentualAcertos))
      line = nomeJogador+'|'+str(totalAcertos)+'\n'
      with open("ranking-jogadores.txt", 'a+') as r:
        # r.write(nomeJogador)
        # r.write('|')
        # r.write(str(totalAcertos))
        # r.write('\n')
        r.writelines(line)
      limparPerguntas()
      jogar()

# Exibir menu de opções
print('Seja bem-vindo! Qual das opções a seguir você deseja realizar?\n\n')
print('1 - Adicionar pergunta ao banco de perguntas')
print('2 - Remover pergunta do banco de perguntas')
print('3 - Alterar pergunta do banco de perguntas')
print('4 - Buscar uma pergunta no banco de perguntas')
print('5 - Jogar')
print('0 - Encerrar o programa')

opcao = int(input('Digite o número da opção desejada: '))

if  opcao == 5:
  jogar()