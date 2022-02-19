# Import the necessary librery
import pandas as pd

# Take the info for the csv
df = pd.read_csv("C:\\Users\\Usuario\\Desktop\\FefoLance\\Morales Rampulla\\fefo-cv.csv",delimiter=';')

# Variables
lectura = True
i = 0
n = 0
recruiter = ''
sample_text = ''
a = 'S'

# Beginning
recruiter = input('Hola, estas en el CV interactivo de Federico, ¿cómo es tu nombre:? \n ')
print(f" {recruiter} para manejarte por este CV tenes que guiarte por los números del índice que te muestro a continuación:")
print('INDICE: \n __ 1 - Sobre mi \n __ 2 - Como contactarme \n __ 3 - Experiencias Laborales_Gerente de Operaciones {Paclin, Pinturas y Agro} \n __ 4 - Experiencias Laborales_Analista de Abastecimiento Senior {Libertad, Retail} \n __ 5 - Experiencias Laborales_Analista de Abastecimiento {Libertad, Retail} \n __ 6 - Experiencias Laborales_Vendedor y At. al cliente {Kevingston House, Indumentaria} \n __ 7 - Estudios/Cursos \n __ 8 - Idiomas \n __ 9 - Soft skill/Otros \n __ 10 - Carta')   
    
while lectura:
    
    i = int(input('\n Que te gustaría leer de mi CV?: \n'))
    if i in df['columna1']:
            lectura2 = True
            texto_selecc = df[(df['columna1'] == i)]
            sample_text = list(texto_selecc['columna4'])
            print(''.join(sample_text))
            while lectura2:
                a = input('\n Querés seguir interactuando, responde S o N: \n')
                if a == 'N' or a == 'n' or a == 'no':
                    print('Espero que hayas encontrado todo lo que buscabas, éxitos!')
                    a='n'
                    lectura = False
                    lectura2 = False
                    break
                else:
                    a='s'
                    lectura2 = False
      
    else:
            i = int(input('Revisa el índice, coloca un número válido: '))
            lectura2 = True
            texto_selecc = df[(df['columna1'] == int(i))]
            sample_text = list(texto_selecc['columna4'])
            print(f" {sample_text}")
            while lectura2:
                a = input('Querés seguir interactuando, responde S o N: \n')
                if a == 'N' or a == 'n' or a == 'no':
                    a='n'
                    lectura = False
                    lectura2 = False
                    break
                    print('Espero que hayas encontrado todo lo que buscabas, éxitos!')
                else:
                    a='s'
                    lectura2 = False