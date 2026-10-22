import json
from datetime import datetime, timedelta
import os

print('===========medicamentos===============')

try:
    with open ('estoque.json','r') as arquivo:
        estoque = json.load(arquivo)
except FileNotFoundError:
    estoque=[]
except json.JSONDecodeError:
    print()
    atualizado = datetime.now()
    texto_at = atualizado.strftime('%d-%m-%y__%H.%M')
    n_n = ('estoque_quebrado__{}.json').format(texto_at)
    os.rename('estoque.json',n_n)
    print('Arquivo com problema!\n Os medicamentos anteriores estão no arquivo:',n_n)
    print()

    estoque=[]

opcao=''

while opcao != '4':

    print('1- Cadastrar novo medicamento')
    print('2- Consultar o estoque')
    print('3- Consultar as validades dos medicamentos')
    print('4- Sair')

    opcao=input('Escolha a opção desejada:')
    
    if opcao == '1':
        print('===========CADASTRAR==========')
        
        nome = input('Nome: ')

        quantidade = None
        while quantidade is None:
            try:
                quantidade = int(input('Quantidade: '))
            except ValueError:
                print()
                print('ERRO! Digite um número. ')
                print()
        
        validade = None
        while validade is None:
            try:
                validade = datetime.strptime(input('Validade: '),'%m/%Y')
                texto = validade.strftime('%m/%Y')
            except ValueError:
                print('Digite uma data! EX: MM/AAAA')

        
        lote = input('Lote: ')

        
        remedio={
            'nome': nome,
            'quantidade': quantidade,
            'validade': texto,
            'lote': lote    
        }
        
        estoque.append(remedio)
        with open ('estoque.json','w') as arquivo:
            json.dump(estoque,arquivo)
        print('Medicamento cadastrado!')
        print()

    elif opcao == '2':

        print('==========ESTOQUE==========')

        if estoque:
            for medicamento in estoque:
                print(f'Nome:{medicamento['nome']} \n Quantidade:{medicamento['quantidade']} \n Lote:{medicamento['lote']}')
                print()
        
        else:
            print()
            print('Nenhum remédio cadastrado!')
            print()
            
    elif opcao == '3':
         print('=========VALIDADE========')

         if estoque:
            hoje = datetime.now()
            margem = timedelta (days = 30)
            
            for medicamento in estoque:
                validade = datetime.strptime(medicamento['validade'], '%m/%Y')
                if validade.month == 12:
                    p_s = datetime(validade.year +1, 1, 1)
                else:
                    p_s = datetime(validade.year, validade.month +1, 1)
                if hoje >= p_s:
                    situacao = 'Vencido'
                elif hoje+margem >= p_s:
                    situacao = 'Próximo do vencimento'
                else:
                    situacao = 'Dentro da validade'

                print(f'Nome:{medicamento['nome']} \n Validade:{medicamento['validade']} \n Situação:{situacao}')
                print()
         else:
            print('Nenhuma validade disponível.')
            print()
   
    elif opcao == '4':
        print()
        print('Até a próxima')
        print()

    else:
        print()
        print('Opção inválida! Escolha um número de 1 a 4')
        print()