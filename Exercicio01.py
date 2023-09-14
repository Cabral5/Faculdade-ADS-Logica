print('Bem-Vindo a Loja do Alexandre Cabral.')
valor_prod = float(input('Digite o valor do produto: '))
qtd_prod = int(input('Digite a quantidade do produto: '))
desconto = 0
#Sem desconto
if qtd_prod <= 200:
  desconto = 0.00
elif qtd_prod >= 201 and qtd_prod < 1000:
  desconto = 0.05
elif qtd_prod >= 1000 and qtd_prod < 2000:
  desconto = 0.10
else:
  desconto = 0.15

#Com desconto

total_sem_desconto = valor_prod * qtd_prod
print('O valor sem desconto é de: R$ {:.2f}'.format(total_sem_desconto))

total_com_desconto = total_sem_desconto - total_sem_desconto * desconto
print('O valor com desconto é de: R$ {:.2f}'.format(total_com_desconto))