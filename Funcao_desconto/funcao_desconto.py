def desconto(valor_item=0.0, desc=0.0):
    """
    :param valor_item: Valor inicial do produto atribuido pelo usuário, ao qual será aplicado o percentual de desconto.
    :param desc: Valor percentual do desconto atribuido pelo usuario a ser aplicado sobre o valor inicial do produto.
    :return: Valor final do produto após a aplicação do percentual de desconto definido pelo usuário.
    """
    valor_total = valor_item - (valor_item * desc) / 100
    return valor_total


'''Programa principal.'''
try:
    print(f'-=-'*20)
    print(f'Cálculo de preço final de venda.')
    print(f'Informe o produto, o valor de venda e o desconto.')
    print(f'Digite SAIR para encerrar a operação.')
    print(f'-=-' * 20)
    while True:
        nome_prod = str(input('informe o nome do produto: ')).upper()
        while nome_prod == '':
            nome_prod = str(input('informe o nome do produto ou digite sair para encerrar a operação: ')).upper()
        if nome_prod == 'SAIR':
            break
        else:
            valor_prod = float(input('informe o valor do produto R$: '))
            desc_prod = float(input('informe a porcentagem do desconto a ser realizado: '))
            valor_final = desconto(valor_prod, desc_prod)
            while valor_final < 0:
                print(f'O valor do desconto excede o valor do produto')
                desc_prod = float(input('informe a porcentagem do desconto a ser realizado: '))
                valor_final = desconto(valor_prod, desc_prod)
            else:
                if valor_final > valor_prod:
                    valor_final = valor_prod 
                print(f'O produto {nome_prod} no valor de R${valor_prod:.2f} recebeu o desconto de {desc_prod:.1f}%')
                print(f'O valor do produto {nome_prod} agora é de R${valor_final:.2f}')
        resp = str(input('Quer continuar? [S/N]: ')).upper()
        while resp not in 'SN':
            print('Erro! Opção inválida')
            resp = str(input('Quer continuar? [S/N]: ')).upper()
        if resp == 'N':
            break
except (ValueError, TypeError):
    print(f'Erro! Houve um problema com os dados informados')
    print(f'Por favor reinicie a operação')
finally:
    print(f'Operação Finalizada.')
