from BaseMath import BaseMath
import traceback

class Calculadora(BaseMath):
    def __init__(self) -> None:
        super().__init__()
        self.listaNumbers = []
    
    def printBubbleSort(self, lista):
        try:            
            desordenados = ""
            for i in range(len(lista)):
                desordenados += str(lista[i])+" - "
                #print(lista[i])
            desordenados = desordenados.removesuffix(" - ")
            print("Lista desordenada: "+desordenados)
            
            lista = self.bubbleSort(lista)
            ordenados = ""
            for i in range(len(lista)):
                ordenados += str(lista[i])+" - "
                #print(lista[i])
            ordenados = ordenados.removesuffix(" - ") 
               
            print("Lista ordenada: "+ordenados)
        except BaseException:
            print(traceback.format_exc())
            
    def crearListaNumeros(self) -> list:
        n = int(input("Cuantos numeros desea agregar?: "))
        for i in range(n):
            num = int(input("Digite el elemento numero#"+str(i+1).strip()+": "))
            self.listaNumbers.append(num)
        return self.listaNumbers