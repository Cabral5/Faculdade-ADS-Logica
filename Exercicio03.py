#Incicio das definiçoes.

#Inicio da função cachorro_peso()
preco = 0
multiplicador = 0
def cachorro_peso():  #Peso do cachorro
  print('Peso do cachorro.')

  while True:
    try:
      peso = float(input('Digite o peso do cachorro (Kg): ')) #Peso do cachorro
      if peso < 3:
        preco = 40
        return preco
      elif peso >= 3 and peso < 10:
        preco = 50
        return preco
      elif peso >= 10 and peso < 30:
        preco = 60
        return preco
      elif peso >= 30 and peso < 50:
        preco = 70
        return preco
      else:
        print('Não aceitamos cachorros acima de 50 Kg. Digite o peso navamente.')
        continue  #Volta ao início do loop
    except ValueError:
      print('Você digitou um valor não númerico.')
      continue  #Volta ao início do loop

#Fim da função cachorro_peso()

#Inicio da função cachorro_pelo()
def cachorro_pelo():
  print('Pelo do cachorro.')

  while True:
    peloCachorro = input('Qual é o pelo do cachorro: \n'+
                       'c - Pelo Curto\n'+
                       'm - Pelo Médio\n'+
                       'l - Pelo Longo\n'+
                       ' >> ') #Menu de escolha do pelo
    peloCachorro = peloCachorro.lower()
    if peloCachorro == 'c':
      return 1
    if peloCachorro == 'm':
      return 1.5
    if peloCachorro == 'l':
      return 2
    else:
      print('Digite apenas (c, m ou l).')
 #Fim da função cachorro_pelo()

 #Incicio da função cachorro_extra()
def cachorro_extra():
  print('Extras do cachorro.')
  acumulador = 0

  while True:
    extras = input('Deseja fazer algum adicional:\n'+
                   '0 - Não desejo adicionar mais nenhum extra.\n'+
                   '1 - Corte de unhas.\n'+
                   '2 - Escovar os dentes.\n'+
                   '3 - Limpar as orelhas.\n'+
                   ' >> ') #Menu adicional
    if extras == '0':
        return acumulador
    elif extras == '1':
        acumulador = acumulador + 10
        continue
    elif extras == '2':
      acumulador = acumulador + 12
      continue
    elif extras == '3':
      acumulador = acumulador + 15
      continue
    else:
      print('Digite apenas (0, 1, 2 ou 3).')

#Fim da função cachorro_extra()

#Inicio do programa
print('Bem-Vindo ao PetShop do Alexandre Cabral.')
#Variaveis
peso = cachorro_peso()
peloCachorro = cachorro_pelo()
extras = cachorro_extra()
total = (peso * peloCachorro) + extras

print('Total a ser pago: R$ {:.2f} (peso: R$ {:.2f}, peloCachorro: R$ {:.2f}, extras: R$ {:.2f})'.format(total, peso, peloCachorro, extras))