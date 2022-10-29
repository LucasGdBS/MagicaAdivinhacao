def mostragem_inicial(c=1, pergunta=True):
  h = False
  for i in range(1, 8):
    print('{}\t{}\t{}'.format(c, c+1, c+2))
    c = c+3
  if pergunta == True:
    while h == False:
      escolha = int(input('Escolha um numero, e diga em qual coluna ele está: '))
      if 1 <= escolha <= 3:
        h = True
    return escolha

def inserir_na_lista(escolha, coluna1, coluna2, coluna3, c=1):
  if escolha == 1:
    for i in range(1,8):
      coluna2.append(c)
      coluna1.append(c+1)
      coluna3.append(c+2)
      c += 3
  elif escolha == 2:
    for i in range(1, 8):
      coluna1.append(c)
      coluna2.append(c+1)
      coluna3.append(c+2)
      c += 3
  elif escolha == 3:
    for i in range(1, 8):
      coluna1.append(c)
      coluna3.append(c+1)
      coluna2.append(c+2)
      c += 3
    
def horizontal(recebe, passa1, passa2, passa3, inicio=0):
  while len(recebe) <= 6:
    if inicio > 6:
      inicio -= 7
    if len(recebe) < 3:
      recebe.append(passa1[inicio])
      inicio += 3
    elif 3 <= len(recebe) < 5:
      recebe.append(passa2[inicio])
      inicio += 3
    elif 5 <= len(recebe) < 7:
      recebe.append(passa3[inicio])
      inicio += 3

def horizontal2(recebe, passa1, passa2, passa3, inicio=1):
  while len(recebe) <= 6:
    if inicio > 6:
      inicio -= 7
    if len(recebe) < 2:
      recebe.append(passa1[inicio])
      inicio += 3
    elif 2 <= len(recebe) < 5:
      recebe.append(passa2[inicio])
      inicio += 3
    elif 5 <= len(recebe) < 7:
      recebe.append(passa3[inicio])
      inicio += 3

def horizontal3(recebe, passa1, passa2, passa3, inicio=2):
  while len(recebe) <= 6:
    if inicio > 6:
      inicio -= 7
    if len(recebe) < 2:
      recebe.append(passa1[inicio])
      inicio += 3
    elif 2 <= len(recebe) < 4:
      recebe.append(passa2[inicio])
      inicio += 3
    elif 4 <= len(recebe) < 7:
      recebe.append(passa3[inicio])
      inicio += 3

def mostragem(coluna1, coluna2, coluna3, c=1):
  h = False
  for i in range(0, 7):
    print(f'{coluna1[i]}\t{coluna2[i]}\t{coluna3[i]}')

  while h == False:
    escolha = int(input('Escolha um numero, e diga em qual coluna ele está: '))
    if 1 <= escolha <= 3:
      h = True
  return escolha

def limpar_listas(a, b, c):
  a.clear()
  b.clear()
  c.clear()     

def flipar(escolha):
  global coluna1
  global coluna2
  global coluna3
  if escolha == 1:
    coluna1 = coluna5[:]
    coluna2 = coluna4[:]
    coluna3 = coluna6[:]
  elif escolha == 2:
    coluna1 = coluna4[:]
    coluna2 = coluna5[:]
    coluna3 = coluna6[:]
  elif escolha == 3:
    coluna1 = coluna4[:]
    coluna2 = coluna6[:]
    coluna3 = coluna5[:]

#Cria todas as listas que vou usar
coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 = list(), list(), list(), list(), list(), list()

#Mostra as colunas iniciais e pergunta em qual coluna está o número
escolha = mostragem_inicial()
#Coloca a coluna escolhida na coluna2
inserir_na_lista(escolha, coluna1, coluna2, coluna3)
#Distribui os números horizontalmente+
horizontal(coluna4, coluna1, coluna2, coluna3)
#+Seguindo a regra do 0362514, incremetando em 3 a partir de 0+
horizontal2(coluna5, coluna1, coluna2, coluna3)
#Sempre que o número passa de 6 ele é subtraido por 7
horizontal3(coluna6, coluna1, coluna2, coluna3)
#Mostra as colunas e pergunta em qual coluna está o número
escolha = mostragem(coluna4, coluna5, coluna6)
#Limpa as colunas 1, 2 e 3
limpar_listas(coluna1, coluna2, coluna3)
#Coloca as colunas dentro das colunas 1, 2 e 3
flipar(escolha)
#Limpa as colunas 4, 5 e 6
limpar_listas(coluna4, coluna5, coluna6)
#Distribui os números horizontalmente novamente
horizontal(coluna4, coluna1, coluna2, coluna3)
#Sempre seguindo a regra do 0362514
horizontal2(coluna5, coluna1, coluna2, coluna3)
#Preenchendo as colunas 4, 5 e 6
horizontal3(coluna6, coluna1, coluna2, coluna3)
#Mostra as colunas e pergunta em qual o número está
escolha = mostragem(coluna4, coluna5, coluna6)
#Limpa as colunas 1, 2 e 3
limpar_listas(coluna1, coluna2, coluna3)
#Coloca as colunas 4, 5 e 6 dentro das colunas 1, 2 e 3
flipar(escolha)
#Mostra o número escolhido
print(f'\nO número que você escolheu foi: {coluna2[3]}')
