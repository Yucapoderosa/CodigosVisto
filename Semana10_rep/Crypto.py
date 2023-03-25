#UpperCamelCase
#LowerCamelCase (variables, metodos)

charToChange = ['a','e','i','o','u'] #list
revToChange = ['h','p','Ñ','6','$']
mixText = "a-h,e-p,i-Ñ,o-6,u-$" #mixText.split(',') ->['a-h','e-p','i-Ñ','o-6','u-$']

listaPalabrasEncriptadas = []

def encriptarText(pTexto) -> str: #Costa Rica ->C6sth RÑch
    nuevoTexto = ''
    for c in pTexto:
        #Determinar si el caracter se debe remplazar
        if (c in charToChange):
            for l in mixText.split(','):  #a-h,e-p,i-Ñ,o-6,u-$ -> ['a-h','e-p','i-Ñ','o-6','u-$']
                v = l.split('-')[0] #'o-6' -> ['o','6']
                if (c == v):
                    nuevoTexto += l.split('-')[1]
        else:
            nuevoTexto += c #C
    
    return nuevoTexto    


def deencriptarText(pTexto): #Costa Rica ->C6sth RÑch
    nuevoTexto = ''
    for c in pTexto:
        #Determinar si el caracter se debe remplazar
        if (c in charToChange):
            for l in mixText.split(','):
                v = l.split('-')[0]
                if (c == v):
                    nuevoTexto += l.split('-')[1]
        else:
            nuevoTexto += c #C
    
    return nuevoTexto      






