lista_colaborador = []
id_colaborador = 0

def cadastrar_colaborador(id):
  print('Cadastrar um colaborador.')
  print('Cadastro do colaborador: {}'.format(id))
  nome = input('Entre com o nome do colaborador: ')
  setor = input('Entre com o setor do colaborador: ')
  salario = float(input('Entre com o salario (R$) do colaborador: '))

  dicionario_colaborador = {'id'        : id,
                            'nome'      : nome,
                            'setor'     : setor,
                            'salario'   : salario}
  lista_colaborador.append(dicionario_colaborador.copy())

def consultar_colaborador():
  print('Consultar um colaborador.')
  while True:
    consultar = input('\nEscolha a opção desejada:\n'+
                          '1 - Consultar todos os Colaboradores\n'+
                          '2 - Consultar Colaborador por id\n'+
                          '3 - Consultar Colaborador(s) por setor\n'+
                          '4 - Retornar\n'+
                          '>>')
    if consultar == '1':
      print('Você escolheu a opção Consultar todos os Colaboradores')
      for colaborador in lista_colaborador: #colaborador vai varrer toda a lista de colaborador
        print('-----------------')
        for key, value in colaborador.items(): #Varrer todos os colaboradores de chave e valor do dicionario do colaborador
          print('{}: {}'.format(key, value))
        print('-----------------')
    elif consultar == '2':
      print('Você escolheu a opção Consultar Colaborador por id')
      id = int(input('Entre com o id do colaborador: '))
      for colaborador in lista_colaborador:
        if colaborador['id'] == id: #o valor do campo id desse dicionario é igual o colaborador
            print('-----------------')
            for key, value in colaborador.items(): #Varrer todos os colaboradores de chave e valor do dicionario do colaborador
              print('{}: {}'.format(key, value))
            print('-----------------')
    elif consultar == '3':
      print('Você escolheu a opção Consultar Colaborador(s) por setor')
      id = input('Entre com o setor do colaborador: ')
      for colaborador in lista_colaborador:
        if colaborador['setor'] == id: #o valor do campo setor desse dicionario é igual o colaborador
            print('-----------------')
            for key, value in colaborador.items(): #Varrer todos os colaboradores de chave e valor do dicionario do colaborador
              print('{}: {}'.format(key, value))
            print('-----------------')
    elif consultar == '4':
      return #Sai da função consultar e volta volta para o menu
    else:
      print('Opção inválida. Tente Novamente.')
      continue  # Volta ao início do laço

def remover_colaborador():
  print('Remover um colaborador')
  id = int(input('Entre com o id do Colaborador que deseja remover: '))
  for colaborador in lista_colaborador:
    if colaborador['id'] == id:
      lista_colaborador.remove(colaborador)
      print('id Removida')

#Inicio do programa
print('Bem-Vindo ao Controle de Colaboradores do Alexandre Cabral.')
while True:
  opcao_principal = input('\nEscolha a opção desejada:\n'+
                          '1 - Cadastrar Colaborador\n'+
                          '2 - Consultar Colaborador\n'+
                          '3 - Remover Colaborador\n'+
                          '4 - Sair\n'+
                          '>>')
  if opcao_principal == '1':
    id_colaborador = id_colaborador + 1
    cadastrar_colaborador(id_colaborador)
  elif opcao_principal == '2':
    consultar_colaborador()
  elif opcao_principal == '3':
    remover_colaborador()
  elif opcao_principal == '4':
    break # Encerra o laço e o programa acaba
  else:
    print('Opção inválida. Tente Novamente.')
    continue # Volta ao início do laço
