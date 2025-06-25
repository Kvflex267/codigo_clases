from datetime import datetime

personas =  {}


def validar_usuarios(usuario):
    if len(usuario)  != 8:

        return False
    letras = usuario[:1]
    numeros = usuario[1:]
    return letras.isalpha() and letras.issuper() and numeros.isdigit()

def  validar_sexo(sexo):
    return sexo.upper() in ["M", "F"]

def registra_personas():
    while True:
        usuario = input("Porfavor ingrese el usuario (Debe tener al menos 1 número, debe tener al menos 1 letra)")
        if not validar_usuarios(usuario):
            print("Usuario invalido. Debe tener al menos 1 número, debe tener al menos 1 letra( EJ: BCD34). ")
        continue
        
        if usuario in personas:
            print("Este Usuario ya esta registrado.") 
        continue

nombre = input("Ingrese el nombre del usuario: ")  
sexo = input("Ingrese el sexo del Usuario (M/F): ").upper()
if not validar_sexo(sexo):
    print("Sexo invalido solo se permiten (M/F)")
    continue
personas = input ("Ingrese el tipo de persona que busca")
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

personas[usuario] = {
"persona": nombre,
"sexo": sexo,
"persona": tipo,
"fecha": fecha
}
print("La persona se ha registrado correctamente. ")
break

def eliminar_personas():
   usuarios = input("Ingrese porfavor el nombre de usuario que desea eliminar: ")
   if usuario in personas:
   del  personas [usuario]
       




    




          




    

































































































print("\n--- Menú ---")
print("1. Ingresar persona")
print("2. Eliminar persona")
print("3. Buscar persona")
print("4. Filtrar por tipo de persona")
print("5. Salir")
