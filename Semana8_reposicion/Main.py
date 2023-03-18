from Calculadora import Calculadora

lista = []


def menu():
    try:
        print('--------Ordenar lista----')
        print('Opción #1 Crear lista de numeros')
        print('Opción #2 Ordenar lista de numeros')
        print('Opción #3 Salir del sistema')
        print('-------------------------')
        while True:
            a = Calculadora() #concepto de instanciar un objeto
            tecla = input("Digitar opcion: ")            
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                lista = a.crearListaNumeros()                
            elif i==2:
                a.printBubbleSort(lista)                
            elif i==3:
                break
            else:
                print('Opcion invalida')
                continue
    except BaseException:
            pass
    finally:
        print("Press Enter to continue ...")
        input()
        
        
if __name__ == "__main__":
    menu()