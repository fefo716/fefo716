# Import the necessary librery
import pandas as pd
import time

# Create the table with the info

data = {'numerador': [1,2,3,4,5,6,7,8,9], 'campo': ['Presentación','Info de Contacto',
                                                                              'Pinturas Paclin','Hiper Libertad','Kevingston',
                                                                              'Estudios/Cursos','Idiomas','Lenguajes y Plataformas'
                                                                             ,'Carta'],
       'cuerpo': ['Me llamo Federico, me dicen Fefo, tengo 32 años. Vivo con mi familia: Renata (mi esposa) y mis peques Pauli (5) y Jero (2); en Córdoba Capital. Soy fan de los deportes, las películas y me encanta viajar y estar al aire libre. Disfruto mi tiempo, también, leyendo sobre tecnologías y crypto, me considero auto-didacta. Mis amigos dicen que soy curioso, empático y yo estoy convencido de que solo puedo lograr cosas buenas ... pero en equipo NO HAY TECHO.'
                 ,'Celular: 3513290810; Mail: fefo.morales@hotmail.com; LinkedIn: https://www.linkedin.com/in/federicomoralesrampulla/'
                 ,'Abril 2018 _ Actualidad- Gerente de Operaciones (8 personas a cargo) • Responsable del área logística que abarca todo tipo de movimientos de entrada y salida de mercadería. Stock e inventarios, tanto de materia prima como de productos para la venta.'
                 ,'Abril 2016 _ Marzo 2018- Data Analyst Supply Chain. • Stock, Distribución, Logística y reportes de KPI´s a la gerencia y dirección: datos y reportes en MicroStrategy. Analista  integral: abastecimiento, logística y comercio internacional. Compras: almacén dulce, fresco y verduleria, higiene y cuidado personal. Automatización de pedidos, generación de pedidos y distribución.'
                 ,'Junio 2011 _ Febrero 2016- Atención al público, ventas • Atención de local comercial. Apertura/cierre de caja. Control de stock. Compras en fábrica (Buenos Aires) y manejo de presupuesto de compras.'
                 ,'Machine Learning & Data science _ Udemy (en curso) \n Laboratorio IA UBA – Inteligencia Artificial y Deep Learning - (en curso) \n Python Bootcamp Programación _ Udemy (Certificado) \n Tecnicatura en Logística _ I.U.A (no finalizado, materias: 9/18) \n Ingeniería Aeronáutica _ I.U.A (no finalizado,materias: 16/50)'
                 ,'Inglés _ b2 overall'
                 ,'Python – orientado a objetos y Data science (librerías: pandas, numpy, seaborn, matplotlib). \n SQL – Conceptos claves para el manejo de tablas y extracción de información. \n VBA – Conceptos básicos para el armado de macros y automatización. \n MICROSOFT EXCEL – Manipulación y limpieza de datos. \n POWER BI - Visualización. \n MARIA DB – Creación de base de datos, manejo y extracción de información. \n MICROSTRATEGY – Consultas y extracción de información, armado de reportes. \n AUTOMATION ANYWHERE – Automatización de tareas. \n JIRA – Planificación y ejecución de proyectos. \n SAP – Extracción de información y consultas.'
                 ,'Quiero aportarle valor a cada proceso en el cual desempeñe mis tareas. Trabajar con creatividad, resolver con dinamismo y comunicarme con pasión. Busco adentrarme en un roll el cual me permita conocer de lleno el rubro IT y que también que me de lugar a ser escuchado y pueda opinar sobre otras tareas, áreas; crecer yo y ayudar a crecer a la empresa.']}

# Create DataFrame.
dataframe = pd.DataFrame(data)

# Variables
lectura = True
i = 0
n = 0
recruiter = ''
sample_text = ''
a = 'S'

# Beginning
recruiter = input('Hola, estas en el CV interactivo de Federico, ¿cómo es tu nombre? \n ')
print(f" Antes que nada, agradezco tu tiempo {recruiter}. \n Para manejarte por este CV tenes que guiarte por los números del índice que te muestro a continuación:")
print('INDICE: \n __ 1 - Presentación \n __ 2 - Como contactarme \n __ 3 - Experiencias Laborales_Gerente de Operaciones {Paclin, Pinturas y Agro} \n __ 4 - Experiencias Laborales_Analista Supply Chain {Libertad, Retail} \n __ 5 - Experiencias Laborales_Vendedor y At. al cliente {Kevingston House, Indumentaria} \n __ 6 - Estudios/Cursos \n __ 7 - Idiomas \n __ 8 - Lenguajes y Plataformas \n __ 9 - Carta')
i = int(input('\n Que te gustaría leer de mi CV?: \n'))    

while lectura:      
    if i in range(0,10):
            texto_selecc = dataframe[(dataframe['numerador'] == i)]
            titulo = list(texto_selecc['campo'])
            print(f'Bien, elegiste: {titulo}')
            lectura2 = True
            sample_text = list(texto_selecc['cuerpo'])
            print(f" {sample_text}")
            while lectura2:
                a = input('¿Querés seguir interactuando? \n responde con un número para ir directamente al tema o N para salir: \n')
                if a == 'N' or a == 'n' or a == 'no':
                    print('Espero que hayas encontrado todo lo que buscabas, éxitos!')
                    # espera en segundos
                    time.sleep(4)
                    lectura = False
                    lectura2 = False
                    break
                else:
                    i = int(a)
                    if i in range(0,10):
                        texto_selecc = dataframe[(dataframe['numerador'] == i)]
                        titulo = list(texto_selecc['campo'])
                        print(f'Ok, vamos con {titulo}')
                        sample_text = list(texto_selecc['cuerpo'])
                        print(f" {sample_text}")
                        pass
                    else:
                        i = int(input('Revisa el índice, coloca un número válido: '))
                        texto_selecc = dataframe[(dataframe['numerador'] == int(i))]
                        sample_text = list(texto_selecc['cuerpo'])
                        print(f" {sample_text}")
                        pass
      
    else:
            i = int(input('Revisa el índice, coloca un número válido: '))
            lectura2 = True
            texto_selecc = dataframe[(dataframe['numerador'] == int(i))]
            sample_text = list(texto_selecc['cuerpo'])
            print(f" {sample_text}")
            while lectura2:
                a = input('¿Querés seguir interactuando? \n responde con un número para ir directamente al tema o N para salir: \n')
                if a == 'N' or a == 'n' or a == 'no':
                    print('Espero que hayas encontrado todo lo que buscabas, éxitos!')
                    # espera en segundos
                    time.sleep(4)
                    lectura = False
                    lectura2 = False
                    break
                else:
                    i = int(a)
                    if i in range(0,10):
                        texto_selecc = dataframe[(dataframe['numerador'] == i)]
                        titulo = list(texto_selecc['campo'])
                        print(f'Ok, vamos con {titulo}')
                        sample_text = list(texto_selecc['cuerpo'])
                        print(f" {sample_text}")
                        pass
                    else:
                        i = int(input('Revisa el índice, coloca un número válido: '))
                        texto_selecc = dataframe[(dataframe['numerador'] == int(i))]
                        sample_text = list(texto_selecc['cuerpo'])
                        print(f" {sample_text}")
                        pass
