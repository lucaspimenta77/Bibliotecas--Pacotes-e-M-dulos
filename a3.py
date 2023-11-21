import string

def contem_apenas_digitos(texto):
   
    return all(caracter in string.digits for caracter in texto)

texto = "12345ab"

if contem_apenas_digitos(texto):
    print("A string contém apenas dígitos.")
else:
    print("A string não contém apenas dígitos.")
