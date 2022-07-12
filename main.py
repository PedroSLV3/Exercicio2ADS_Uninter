print('Bem-vindo a pizzaria do Pedro Henrique da Silva')
print('--CARDAPIO--') #EXIBE O CARDAPIO NA TELA
print('| CODIGO | DESCRIÇÃO  | Pizza M | Pizza G | ')
print('|   21   | Napolitana | R$20,00 | R$26,00 | ')
print('|   22   | Margherita | R$20,00 | R$26,00 | ')
print('|   23   | Calabresa  | R$25,00 | R$32,50 | ')
print('|   24   | Toscana    | R$30,00 | R$39,00 | ')
print('|   25   | Portuguesa | R$30,00 | R$39,00 | ')

TotalPizzas = 0 #VARIAVEL QUE REPRESENTA A QUANTIA DE PIZZAS PEDIDAS
Custo = 0 #VARIAVEL QUE REPRESENTA O VALOR GASTO

while True:
    Tpizza = input('Qual o tamanho desejado? (M ou G)') #SOLICITA O TAMANHO DA PIZZA #ESTE É O INICIO
    if not (Tpizza == 'M' or Tpizza == 'G'): #CONFIRMAR SE O TAMANHO DA PIZZA É DIFERENTE DE M OU G
            print('Tamanho invalido') #SE FOR DIFERENTE MOSTRA O ERRO
            continue #CASO SEJA DIFERENTE RETORNA AO INICIO
    else:
        Sabor = input('Digite o código do sabor desejado:')#SOLICITA O SABOR EM FORMA DE CODIGO DO CARDAPIO
        if not (Sabor == '21' or Sabor == '22' or Sabor == '23' or Sabor == '24' or Sabor == '25' ): #CONFIRMA SE O CODIGO DE SABOR FORNECIDO É DIFERENTE DOS DISPONIBILIZADOS NO CARDAPIO
            print('Sabor inválido')# SE FOR DIFERENTE MOSTRA O ERRO
            continue # VOLTA AO INICIO
        else:
            if (Sabor == '21' ):  # APARTIR DAQUI SOMA OS VALORES CONFORME TAMANHO E CODIGO
                if (Tpizza == 'M'):
                    Custo += 20
                    print("Você pediu uma pizza Média do sabor Napolitana")
                if (Tpizza == 'G'):
                    Custo += 26
                    print("Você pediu uma pizza Grande do sabor Napolitana")

            elif (Sabor == '22'):
                if (Tpizza == 'M'):
                    Custo += 20
                    print("Você pediu uma pizza Média do sabor Margherita")
                if (Tpizza == 'G'):
                    Custo += 26
                    print("Você pediu uma pizza Grande do sabor Margherita")

            elif (Sabor == '23'):
                if (Tpizza == 'M'):
                    Custo += 25
                    print("Você pediu uma pizza Média do sabor Calabresa")
                if (Tpizza == 'G'):
                    Custo += 32.50
                    print("Você pediu uma pizza Grande do sabor Calabresa")

            elif (Sabor == '24'):
                if (Tpizza == 'M'):
                    Custo += 30
                    print("Você pediu uma pizza Média do sabor Toscana")
                if (Tpizza == 'G'):
                    Custo += 39
                    print("Você pediu uma pizza Grande do sabor Toscana")

            elif (Sabor == '25'):
                if (Tpizza== 'M'):
                    Custo += 30
                    print("Você pediu uma pizza Média do sabor Portuguesa")
                if (Tpizza == 'G'):
                    Custo += 39
                    print("Você pediu uma pizza Grande do sabor Portuguesa")

            TotalPizzas += 1 #CASO TUDO ESTIVER CERTO, ADICIONA 1 PIZZA AO TOTAL DE PIZZAS
            Continuar = input('Deseja pedir algo mais?(S/N)') #SOLICITA SE O CLIENTE DESEJA ADQUIRIR ALGO MAIS

    if (Continuar == 'S'):#SE O USUARIO DIGITAR S, VOLTA AO INICIO
        continue
    if (Continuar == 'N'):#MOSTRA O TOTAL DA CONTA SE O USUARIO DIGITAR N
        print('Foram pedidas {} pizzas, ficou o total de {}'.format(TotalPizzas, Custo))
        break
    else:
        print('Opção inválida')
        continue



