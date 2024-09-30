#OK Entry an input at the terminal -> 9 digits;
    # I'll process the data
#OK Transform at an matrix array of 3 x 3;
# them I'll separatly make the methods;
# them I'll show them the result for the string they have send to me;

import numpy as np

#Eu teria que colocar mais alguns métodos de data cleaning para ter certeza que vou receber 
# os dados corretos, mas vamos ignorar isso no mometno;
def asking():
        while True:
            try:
                #An variable store/contain an array with 9 intenger numbers;
                lista = input('Send me an array with 9 intengers numbers (separeted by spaces):')
                
                #divide a string em uma lista de números
                numero = np.array([int(num) for num in lista.split()])

                if len(numero) != 9:
                    print('Por favor insira exatamente 9 números inteiros')
                    continue#reinicia o loopo se a condição não for atingida

                print(numero)
                return numero # se a transação for bem sucedida irá retornar lista
                #Aparentemente quando eu tento printar o número depois que ele recebeu 
                # o return eu não consigo, provavelmente porque é como aquela variável não estivesse mais naquele escopo; 
                #print(numero)
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro")


def calculate(numero):
    
    matrix = numero.reshape(3, 3)
    # Calculando métricas por coluna (axis=0), por linha (axis=1) e como matriz achatada (flattened)
    
    calculations = {
        'mean': {
            'columns': np.mean(matrix, axis=0),
            'rows': np.mean(matrix, axis=1),
            'flattened': np.mean(matrix)
        },
        'variance': {
            'columns': np.var(matrix, axis=0),
            'rows': np.var(matrix, axis=1),
            'flattened': np.var(matrix)
        },
        'std_dev': {
            'columns': np.std(matrix, axis=0),
            'rows': np.std(matrix, axis=1),
            'flattened': np.std(matrix)
        },
        'max': {
            'columns': np.max(matrix, axis=0),
            'rows': np.max(matrix, axis=1),
            'flattened': np.max(matrix)
        },
        'min': {
            'columns': np.min(matrix, axis=0),
            'rows': np.min(matrix, axis=1),
            'flattened': np.min(matrix)
        },
        'sum': {
            'columns': np.sum(matrix, axis=0),
            'rows': np.sum(matrix, axis=1),
            'flattened': np.sum(matrix)
        }
    }

    # Exibindo os resultados
   # Imprimindo os resultados no formato desejado
    print("{")
    for key, value in calculations.items():
        print(f"  '{key}': [columns: {value['columns']}, rows: {value['rows']}, flattened: {value['flattened']}],")
    print("}")



    return calculations