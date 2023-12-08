import secrets #Esta libreria nos proporciona números y textos aleatorios de manera segura.
import hashlib #Esta libreria nos proporciona dibersos hash, es utilizada en este código para cifrar contrasenas

#rango de lonjitudes
LONGITUD_MINIMA = 12
LONGITUD_MAXIMA = 30

#Funcion para generar contrasena segura
def generar_contrasena_segura(longitud, algoritmo_cifrado):
    #Este bucle lo utilizo para asegurarme que el cifrado cumpla con los requisitos de seguridad
    while True: 

        # Genera una cadena aleatoria segura, la funcion le pertenese a la libreria secrets
        contrasena = secrets.token_urlsafe(longitud)
        # Aplica el cifrado seleccionado
        cifrado = hashlib.new(algoritmo_cifrado)
        cifrado.update(contrasena.encode('utf-8'))
        contrasena_cifrada = cifrado.hexdigest()
        return contrasena, contrasena_cifrada


def verificar_contraseña(contraseña, contraseña_cifrada, algoritmo_cifrado):
    # Verifica si la contraseña introducida en claro (descifrada) coincide con la contraseña cifrada almacenada
    cifrado = hashlib.new(algoritmo_cifrado)
    cifrado.update(contraseña.encode('utf-8'))
    return cifrado.hexdigest() == contraseña_cifrada


#Funcion para obtener diferentes algoritmos de cifrado. Para dar a elejir al usuario el que desea
def obtener_algoritmos_cifrado_disponibles():
    return hashlib.algorithms_guaranteed

#Funcion para validar si la lonjitud de contrasena requerida esta entre 12 y 30 para que no sea demasiado larga ni demasiado corta
def obtener_longitud_contrasena():
    #Ciclo para solicitar la contarseña nuevamente hasta que se cumpla con los paraetros requeridos
    while True:
        try:
            longitud_contrasena = int(input("Bienvenido. Por favor ingrese la longitud que desea para generar su contraseña (entre 12 y 30 caracteres): "))
            if LONGITUD_MINIMA <= longitud_contrasena <= LONGITUD_MAXIMA:
                return longitud_contrasena
            else:
                print("Lo sentimos, la longitud de la contraseña debe estar entre 12 y 30 caracteres.")
        except ValueError:
            print("Por favor, ingrese un valor numerico válido.")

#Funcion para solicitar diferentes algoritmos de cifrado.
def obtener_algoritmo_cifrado():
    algoritmos_disponibles = obtener_algoritmos_cifrado_disponibles()
    
    #Ciclo para reintentar solicitar la contarseña nuevamente hasta que se cumpla con los parametros requeridos
    while True:
        algoritmo_cifrado = input(f"Seleccione un algoritmo de cifrado ({', '.join(algoritmos_disponibles)}): ").lower()
        if algoritmo_cifrado in algoritmos_disponibles:
            return algoritmo_cifrado
        else:
            print("Algoritmo no válido. Por favor, elija uno de los algoritmos disponibles.")

# Solicitar al usuario la longitud y el algoritmo de cifrado
longitud_contrasena = obtener_longitud_contrasena()
algoritmo_cifrado = obtener_algoritmo_cifrado()

# Generar la contrasena segura
contrasena, contrasena_cifrada = generar_contrasena_segura(longitud_contrasena, algoritmo_cifrado)

# Mostrar la contrasena cifrada
print("Esta es su contraseña cifrada:", contrasena_cifrada)
print("Esta es su contraseña segura en claro:", contrasena)
contraseña_usuario = input("Si desea comprobar el algoritmo de descifrado de su contraseña debe introducirla en claro o descifrada a continuacion:")

if verificar_contraseña(contraseña_usuario, contrasena_cifrada, algoritmo_cifrado):
    print("**********Contraseña válida. Acceso concedido**********")
else:
    print("**********Contraseña incorrecta. Acceso denegado**********")