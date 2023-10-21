#Variável global para armazenar restaurantes
#[["Nome do restaurante",[prato_1, prato_2, prato_3]]]
restaurantes = []

def menu():
    menu = '''
  ---------- Menu ----------
  [1] - Adicionar Restaurante
  [2] - Realizar Pedido
  [3] - Adicionar Pratos à um Restaurante
  [4] - Visualizar Restaurantes e Cardápios
  [0] - Finalizar
  --------------------
  => '''
    return input(menu)


# Retorna lista com nome, valor, e tempo de preparo de cada prato
# [[prato_1,valor,tempo],[prato_2,valor,tempo]]
def adiciona_cardapio():
  cardapio = []
  finaliza = True
  while finaliza:
    nome_prato = input('Nome do prato: ')
    valor_prato_str = input('Valor do prato: ').replace(',', '.')
    valor_prato = float(valor_prato_str)
    tempo_preparo = input('Tempo de preparo: ')
    
    cardapio.append([nome_prato, valor_prato, tempo_preparo])
    
    print('[0] - Finalizar \n[1] - Continuar')
    if input() == '0':
        break
  return cardapio

def adiciona_restaurante():
  nome_restaurante = input('Nome do restaurante: ').title()
  cardapio_restaurante = adiciona_cardapio()
  novo_restaurante = [nome_restaurante,cardapio_restaurante]
  restaurantes.append(novo_restaurante)
  
def exibe_cardapio(restaurante):
  print(f'            Cardápio do Restaurante {restaurante[0]}\n')
  print('|     Prato       |      Preço       | Tempo de Preparo  |')
  print('-'*58)
  pratos = restaurante[1]
  for prato in pratos:
    print(f'|{prato[0]:^16} | {prato[1]:^16} | {prato[2]:^18} |')
    print('-'*58)
    
def exibe_menu(nome_restaurante):
  for item in restaurantes:
    if nome_restaurante == item[0]:
      exibe_cardapio(item)

def exibir_pedido(pedido):
  ordem = sorted(pedido)
  tem = []
  print('Nº |     Prato       |      Preço       | Tempo de Preparo  | Quantidade | ')
  for i in ordem:
    qnt = ordem.count(i)
    if i not in tem:
      print(f'{pedido.index(i):02d} | {i[0]:^15} | {(i[1] * qnt):^16} | {i[2]:^17} | {qnt:^11}|')
      tem.append(i)
    else:
      continue

def realizar_pedido():
  pedidos = []
  while True:
    prato_desejado = input('Digite o prato desejado: ').title()
    for restaurante in restaurantes:
      cardapio = restaurante[1]
      for prato in cardapio:
        if prato_desejado == prato[0]:
          pedidos.append(prato)
    print('[1] - Continuar com pedido \n[0] - Finalizar pedido')
    if input() == '0':
      break
  exibir_pedido(pedidos)
  

def selecionar_restaurante():
  # restaurante[0] retorna o nome do restaurante selecionado
  # restaurante[1] retorna o cardápio do restaurante
  print('Estes são os restaurantes disponíveis:')
  
  for restaurante in restaurantes:
      print(restaurante[0])

  while True:
    restaurante_buscado = input('Digite o nome do restaurante: ').title()
    for restaurante in restaurantes:
      if restaurante_buscado == restaurante[0]:
        exibe_menu(restaurante_buscado)
        realizar_pedido()
        return
    print("Restaurante não encontrado. Tente novamente.")

#Adiciona ao cardápio de um restaurante específico.
def adicionar_pratos():
  # restaurante[0] retorna o nome do restaurante selecionado
  # restaurante[1] retorna o cardápio do restaurante
  print('Estes são os restaurantes disponíveis:')
  
  for restaurante in restaurantes:
      print(restaurante[0])

  while True:
    restaurante_buscado = input('Digite o nome do restaurante: ').title()
    for restaurante in restaurantes:
      if restaurante_buscado == restaurante[0]:
        exibe_menu(restaurante_buscado)
        print("Adicione novos pratos ao cardápio:")
        cardapio_adicional = adiciona_cardapio()
        for prato_novo in cardapio_adicional:
                restaurante[1].append(prato_novo)
        print("Cardápio atualizado!")
        return
    print("Restaurante não encontrado. Tente novamente.")

#Adicionado pra verificar a inserção correta dos dados
def visualizar_restaurantes():
    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado!")
        return

    for restaurante in restaurantes:
        exibe_cardapio(restaurante)
            
def main():
  while True:
    opcao = menu()
    if opcao == '1':
      adiciona_restaurante()
    elif opcao == '2':
      selecionar_restaurante()
    elif opcao == '3':
      adicionar_pratos()
    elif opcao == '4':
      visualizar_restaurantes()
    elif opcao == '0':
      print('Encerrando...')
      break
    else:
      ('Opção Inválida')

main()