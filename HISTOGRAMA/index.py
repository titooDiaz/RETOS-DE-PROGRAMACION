datos = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]

def histograma(datos):
    for i in datos:
        for x in range(int(i)):
            print("*", end="")
        print('\n')

histograma(datos)