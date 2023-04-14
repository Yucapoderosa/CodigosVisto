import Crypto as Cry
resultado = ""

try:
    print("------------------------------------")
    print("Menu del sistema:")
    print("1.Encriptar palabras\n\r"+
          "2.Mostrar lista de palabras encriptadas\n\r"+
          "3.Salir del sistema\n\r")
    while (True):
        opUsuario = input("\n\n\rDigite la opción de menu a realizar: ")
        if (not opUsuario.isdigit()):
            print('Usted no digito una opción numerica valida\n\r')
            continue
        if (opUsuario == '1'):
           try:               
               while (True):                   
                    textoCifrar = input("Que texto desea cifrar? [Ctrl+C para salir]: ")
                    textoCifrado = Cry.encriptarText(textoCifrar)
                    dataSave = { #dict
                        'Original' : textoCifrar,
                        'Encriptado': textoCifrado
                    }
                    Cry.listaPalabrasEncriptadas.append(dataSave)
           #print("La palabra cifrada es: "+restulado)
           except BaseException:
               continue
        if (opUsuario == '2'):
            print("\n")
            for item in Cry.listaPalabrasEncriptadas:
                print(str(item["Original"]).ljust(25,".")+str(item["Encriptado"]))
                
            continue
                
        break
    print("Hola mundo")
except BaseException:
    print("Termino la ejecucion")
    
input()
