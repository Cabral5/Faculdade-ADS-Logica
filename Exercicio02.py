print('Bem-vindo a sorverteria do Alexandre Cabral.')
print('+----------------------------------CARDÁPIO----------------------------------+')
print('|N° Bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)|')
print('|   01    |       R$  6,00         |     R$  7,00       |     R$  8,00       |')
print('|   02    |       R$ 11,00         |     R$ 13,00       |     R$ 15,00       |')
print('|   03    |       R$ 15,00         |     R$ 18,00       |     R$ 21,00       |')
print('+----------------------------------------------------------------------------+')

valor = 0
while True:  # Laço infinito
    sabor = (input('Qual o sabor desejado,(tr, pr ou es): '))
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Opção inválida. Digite somente (tr/pr/es)  ')
        continue  # serve para quando o usuario digitar algo que não esteja seja invalido, volta para o laço

    qtd = input('Quantas bolas de sorverte desejado,(01, 02 ou 03): ')
    if qtd != '01' and qtd != '1' and qtd != '02' and qtd != '2' and qtd != '03' and qtd != '3':
        print('Número de bolas de sorvete inválida. ')
        continue  # serve para quando o usuario digitar algo que não esteja seja invalido, volta para o laço


    if qtd == '01' and sabor == 'tr':
        print('Você escolheu 01 bola de sorverte, sabor tradicional.')
        valor = valor + 6  #pega o valor que tinha no valor e soma com 6 e assim por diante
    elif qtd == '01' and sabor == 'pr':
        print('Você escolheu 01 bola de sorverte, sabor premium.')
        valor = valor + 7
    elif qtd == '01' and sabor == 'es':
        print('Você escolheu 01 bola de sorverte, sabor especial.')
        valor = valor + 8
    elif qtd == '02' and sabor == 'tr':
        print('Você escolheu 02 bola de sorverte, sabor tradicional.')
        valor = valor + 11
    elif qtd == '02' and sabor == 'pr':
        print('Você escolheu 02 bola de sorverte, sabor premium.')
        valor = valor + 13
    elif qtd == '02' and sabor == 'es':
        print('Você escolheu 02 bola de sorverte, sabor especial.')
        valor = valor + 15
    if qtd == '03' and sabor == 'tr':
        print('Você escolheu 03 bola de sorverte, sabor tradicional.')
        valor = valor + 15
    elif qtd == '03' and sabor == 'pr':
        print('Você escolheu 03 bola de sorverte, sabor premium.')
        valor = valor + 18
    elif qtd == '03' and sabor == 'es':
        print('Você escolheu 03 bola de sorverte, sabor especial.')
        valor = valor + 21

    mais_pedidos = input('Deseja pedir mais alguma coisa (S/N): ')
    mais_pedidos = mais_pedidos.upper() #resolve o problema de letra maiuscula é minuscula
    print(mais_pedidos)
    if mais_pedidos == 'S':
        continue
    else:
        print('O valor total a ser pago é de: R$ {:.2f}'.format(valor)) #:.2f dentro da chave é ref. a (duas) casas decimais
        break  #encerra o programa