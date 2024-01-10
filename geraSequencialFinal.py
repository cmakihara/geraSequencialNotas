import os

'''
:gerarSequencial: Gera a sequencia de numeros entre as faixas informadas
:param faixaNotas: Lista de faixa inicial e final
:output: os numeros sequencias entra as faixa inicial e final
''' 
def gerarSequencial(faixaNotas):
    qtdNotas=0
    if(len(faixaNotas)%2 == 0):
        for i in range(0,len(faixaNotas),2):
            ini = faixaNotas[i]
            fim = faixaNotas[i+1]
            if ini > fim:
                print('\nALERTA: Contem faixa inicial menor que a final Verifique\n')
                print('Faixa inicial: ',ini,'\nFaixa final: ',fim,'\n')
                input('Press ENTER to exit') 
                exit()

            while(ini <= fim):
                print(ini, end =",")
                ini += 1
                qtdNotas +=1
        print("\n\nTotal de numerações de notas geradas: ",qtdNotas,'\n')        
        input('Press ENTER to exit')    
    else:
        print("ERRO: QTD IMPAR das faixas de notas\n")
        inserirFaixas()

       
def inserirFaixas():
    faixaInput = input('Insira as faixas de notas(numeros) separado por (,) Ex:12,15,55,55\n')
    faixaNotas = faixaInput.split(',') 
    os.system('cls')
    for faixa in faixaNotas:
        if not(faixa.isnumeric()):
            print("ERRO somente (numero) e (,) permitido\n")
            print('Caractere invalido: ',faixa,'\n')
            input('Press ENTER to exit')   
            exit()
    
    listNotas = list(map(int,faixaNotas))
    gerarSequencial(listNotas)

if __name__ == '__main__':
    inserirFaixas()
