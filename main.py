# Projeto Game Quiz para conclusão da disciplina de Programação I - Python
# da Universidade Federal Ruaral de Pernambuco - UFRPE
# Aluno: Jefferson Romano
# Data: 16-09-2022
# Versão: 0.1

# imports libs
import random
from replit import audio

# Criaando dicionário de perguntas
perguntas = {}

#----------------------------------------------------------#
# Função para limpar perguntas carregadas                  #
#----------------------------------------------------------#
def limparPerguntas():
  perguntas.clear()
  return perguntas
  
#----------------------------------------------------------#
# Função para adicionar uma pergunta                       #
#----------------------------------------------------------#
def adicionarPergunta():
  pergunta = input('Digite a pergunta seguida de ponto de interrogação (?):')
  alternativa1 = input('Digite o texto da alternativa a): ')
  alternativa2 = input('Digite o texto da alternativa b): ')
  alternativa3 = input('Digite o texto da alternativa c): ')
  alternativaCorreta = input('Digite a letra da alternativa correta: ')
  nivelPergunta = input('Qual o nível da pergunta? Digite (f=fácil, m=médio e d=difícil): ')

  line = "\n" + pergunta + "|" + alternativa1 + "|" + alternativa2 + "|" + alternativa3 + "|" + alternativaCorreta + "|" + nivelPergunta
  # Abrir arquivo para inclusão
  with open("base-de-perguntas-e-respostas.txt", 'a') as f:
    f.write(line)
  limparPerguntas()
  carregarPerguntas()
  
#----------------------------------------------------------#
# Função para remover uma pergunta                         #
#----------------------------------------------------------#
def removerPergunta():
  
  file = open("base-de-perguntas-e-respostas.txt", 'r')
  lines = file.readlines()
  file.close()

  contador = 1
  for line in lines:
    print(contador,line)
    contador+=1

  numeroLine = int(input('\nDigite o número da pergunta que deseja remover: '))
  
  del lines[numeroLine - 1]

  # Debug
  #print(lines)

  newFile = open("base-de-perguntas-e-respostas.txt", 'w+')
  
  for line in lines:
    newFile.write(line)
  
  newFile.close()

  # Debug
  #print(lines)
  
  limparPerguntas()
  carregarPerguntas()
  
#----------------------------------------------------------#
# Função para alterar uma pergunta                         #
#----------------------------------------------------------#
def alterarPergunta():
  
  file = open("base-de-perguntas-e-respostas.txt", 'r')
  lines = file.readlines()
  file.close()

  contador = 1
  for line in lines:
    print(contador,line)
    contador+=1

  numeroLine = int(input('\nDigite o número da pergunta que deseja alterar: '))
  
  listaDePerguntas = [line.split("|") for line in lines]
  print(listaDePerguntas[numeroLine - 1])
  #print('Qual informação gostaria de atualizar?\n')
  #lines[numeroLine - 1]
  pergunta = input('Digite a pergunta seguida de ponto de interrogação (?):')
  alternativa1 = input('Digite o texto da alternativa a): ')
  alternativa2 = input('Digite o texto da alternativa b): ')
  alternativa3 = input('Digite o texto da alternativa c): ')
  alternativaCorreta = input('Digite a letra da alternativa correta: ')
  nivelPergunta = input('Qual o nível da pergunta? Digite (f=fácil, m=médio e d=difícil): ')

  line = "\n" + pergunta + "|" + alternativa1 + "|" + alternativa2 + "|" + alternativa3 + "|" + alternativaCorreta + "|" + nivelPergunta
  # Abrir arquivo para inclusão
  with open("base-de-perguntas-e-respostas.txt", 'w+') as f:
    f.write(line)

#----------------------------------------------------------#
# Função para carregar perguntas                           #
#----------------------------------------------------------#
def carregarPerguntas(nivel = 'f'):

  # Lista de variáveis
  listaDePerguntas = []
  listaDePerguntasRS = []
  
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

#----------------------------------------------------------#
# Função para iniciar uma partida                          #
#----------------------------------------------------------#
def jogar(ativarRanking = False):

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
      #acertou = audio.play_file('correct-2-46134.mp3')
      print("Aaaaaaacertou, miseravi!!!")
    else:
      #errou = audio.play_file('negative_beeps-6008.mp3')
      print("Êeeeeeerrou!!! Que merda hein?! Sabia não :(")
  
    contador += 1
    # Gravando o ranking da partida
    if contador == len(perguntas):
      # Percentual de acertos
      #percentualAcertos = totalAcertos / qtdPerguntas * 100
      #print("\nPercentual de acerto: {:.2f}%".format(percentualAcertos))
      line = nomeJogador+'|'+str(totalAcertos)+'\n'

      # Separando ranking por nível, o nível fácil é o default
      if nivel == 'm': # médio
        arquivoRanking = 'ranking-jogadores-m.txt'
      elif nivel == 'd': # difícil
        arquivoRanking = 'ranking-jogadores-d.txt'
      else: # fácil
        arquivoRanking = 'ranking-jogadores.txt'
      
      with open(arquivoRanking, 'a+') as r:
        # r.write(nomeJogador)
        # r.write('|')
        # r.write(str(totalAcertos))
        # r.write('\n')
        r.writelines(line)
        
      limparPerguntas()
      if ativarRanking == False:
        jogar()
      else:
        listarRanking(nivel)

#----------------------------------------------------------#
# Função para exibir ranking                               #
#----------------------------------------------------------#      
def listarRanking(nivel = 'f'):

  # Separando ranking por nível, o nível fácil é o default
  if nivel == 'm': # médio
    arquivoRanking = 'ranking-jogadores-m.txt'
  elif nivel == 'd': # difícil
    arquivoRanking = 'ranking-jogadores-d.txt'
  else: # fácil
    arquivoRanking = 'ranking-jogadores.txt'
    
  with open(arquivoRanking, encoding='utf-8') as r:
    # Criando um array com os dados de uma linha e quebrando em valores com a função split
    ranking = [line.split("|") for line in r]
    
    def takeSecond(elem):
      return elem[1]
      
    print("\nRanking geral:\n-------------------")
    
    #Ordenar pelo segundo elemento da lista
    rankingSorted = sorted(ranking,key=takeSecond, reverse=True)
    
    for posicao in rankingSorted:
      print(f'Nome: {posicao[0]}\nPontos: {posicao[1].strip()}\n------------------')     
  
#----------------------------------------------------------#
# Função para chamar menu de opções                        #
#----------------------------------------------------------#
def menuInicial():
  # Exibir menu de opções
  print('Seja bem-vindo! Qual das opções a seguir você deseja realizar?\n\n')
  print('1 - Adicionar pergunta ao banco de perguntas')
  print('2 - Remover pergunta do banco de perguntas')
  print('3 - Alterar pergunta do banco de perguntas')
  print('4 - Buscar uma pergunta no banco de perguntas')
  print('5 - Jogar')
  print('0 - Mostrar ranking geral\n')
  
  opcao = int(input('Digite o número da opção desejada: '))
  
  if  opcao == 5:
    jogar()
  elif opcao == 1:
    adicionarPergunta()
  elif opcao == 2:
    removerPergunta()
  elif opcao == 3:
    alterarPergunta()
  elif opcao == 0:
    nivel = input('Qual o nível você deseja ver o ranking?\n(f=fácil, m=médio e d=difícil): ')
    listarRanking(nivel)

menuInicial()