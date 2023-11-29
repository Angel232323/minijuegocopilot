#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

# crea una aplicacion de consola con python que le pida al usuario elegiar entre 3 opciones
# las opciones son: 1) piedra 2) papel  3) tijeras
# la aplicacion debe elegir una opcion al azar y compararla con la opcion del usuario
# se debe validar que el usuario solo inserte una de las 3 opciones, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion
# si la opcion del usuario es igual a la opcion de la aplicacion se debe mostrar un mensaje de empate
# si la opcion del usuario es diferente a la opcion de la aplicacion se debe comparar las opciones
# si el usuario elige piedra y la aplicacion elige tijeras, el usuario gana
# si el usuario elige papel y la aplicacion elige piedra, el usuario gana
# si el usuario elige tijeras y la aplicacion elige papel, el usuario gana
# si el usuario elige piedra y la aplicacion elige papel, la aplicacion gana
# si el usuario elige papel y la aplicacion elige tijeras, la aplicacion gana
# si el usuario elige tijeras y la aplicacion elige piedra, la aplicacion gana
# se debe mostrar un mensaje con el resultado de la partida
# se debe mostrar un mensaje preguntando si el usuario desea volver a jugar
# si el usuario responde que si, se debe volver a mostrar las opciones
# si el usuario responde que no, se debe mostrar un mensaje de despedida y cerrar la aplicacion
# se debe validar que el usuario solo inserte si o no, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion
# se debe validar que el usuario solo inserte numeros, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion
# se debe validar que el usuario solo inserte numeros enteros, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion
# se debe validar que el usuario solo inserte numeros positivos, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion
# se debe validar que el usuario solo inserte numeros positivos menores a 4, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion
# se debe validar que el usuario solo inserte numeros positivos mayores a 0, en caso contrario se debe mostrar un mensaje de alerta y volver a pedir la opcion

# empieza desde aqui
# importa las librerias que necesites
import random

# crea una funcion que se encargue de mostrar las opciones
def mostrar_opciones():
    print("1) piedra")
    print("2) papel")
    print("3) tijeras")
# crea una funcion que se encargue de pedir la opcion al usuario
def pedir_opcion():
    opcion = input("elige una opcion: ")
    return opcion
# crea una funcion que se encargue de validar la opcion del usuario
def validar_opcion(opcion):
    if opcion == "1" or opcion == "2" or opcion == "3":
        return True
    else:
        return False
    
    # si la opcion es valida, retorna True
    # si la opcion no es valida, retorna False
# crea una funcion que se encargue de elegir una opcion al azar
def elegir_opcion():
    opcion = random.randint(1,3)
    return opcion
# crea una funcion que se encargue de comparar la opcion del usuario con la opcion de la aplicacion
def comparar_opciones(opcion_usuario, opcion_aplicacion):
    # si la opcion del usuario es igual a la opcion de la aplicacion, retorna 0
    # si la opcion del usuario es diferente a la opcion de la aplicacion, retorna 1
    if opcion_usuario == opcion_aplicacion:
        return 0
    else:
        return 1
# crea una funcion que se encargue de mostrar el resultado de la partida
def mostrar_resultado(resultado):
    if resultado == 0:
        print("empate")
    else:
        print("gano")
# crea una funcion que se encargue de preguntar si el usuario desea volver a jugar
def preguntar_volver_a_jugar():
    
    respuesta = input("desea volver a jugar? (si/no): ")
    if respuesta == "si":
        return True
    else:
        return False
# crea una funcion que se encargue de validar la respuesta del usuario
def validar_respuesta(respuesta):
    if respuesta == "si" or respuesta == "no":
        return True
    else:
        return False
# crea una funcion que se encargue de validar que el usuario solo inserte numeros
def validar_numero(numero):
    if numero.isdigit():
        return True
    else:
        return False
# crea una funcion que se encargue de validar que el usuario solo inserte numeros enteros
def validar_numero_entero(numero):
    if numero.isdecimal():
        return True
    else:
        return False
# crea una funcion que se encargue de validar que el usuario solo inserte numeros positivos
def validar_numero_positivo(numero):
    if int(numero) > 0:
        return True
    else:
        return False
# crea una funcion que se encargue de validar que el usuario solo inserte numeros positivos menores a 4
def validar_numero_positivo_menor_a_4(numero):
    if int(numero) < 4:
        return True
    else:
        return False
# crea una funcion que se encargue de validar que el usuario solo inserte numeros positivos mayores a 0
def validar_numero_positivo_mayor_a_0(numero):
    if int(numero) > 0:
        return True
    else:
        return False
# crea una funcion que se encargue de validar que el usuario solo inserte si o no  
def validar_si_o_no(respuesta):
    if respuesta == "si" or respuesta == "no":
        return True
    else:
        return False
# crea una funcion que se encargue de mostrar un mensaje de alerta y volver a pedir la opcion
def mostrar_alerta():
    print("opcion invalida")



# ahora llama todas las funciones que creaste en el orden que necesites
# recuerda que las funciones que creaste deben retornar un valor
# si la funcion retorna un valor, debes guardar ese valor en una variable
# si la funcion no retorna un valor, no debes guardar nada en una variable
# si la funcion retorna un valor, puedes usar ese valor en otra funcion
# si la funcion no retorna un valor, no puedes usar ese valor en otra funcion
# si la funcion retorna un valor, puedes usar ese valor en el codigo principal
# si la funcion no retorna un valor, no puedes usar ese valor en el codigo principal

# empieza a llamar las funciones desde aqui
# llama la funcion que se encarga de mostrar las opciones
mostrar_opciones()
# llama la funcion que se encarga de pedir la opcion al usuario
opcion_usuario = pedir_opcion()
# llama la funcion que se encarga de validar la opcion del usuario
validar_opcion(opcion_usuario)
# llama la funcion que se encarga de elegir una opcion al azar
opcion_aplicacion = elegir_opcion()
# llama la funcion que se encarga de comparar la opcion del usuario con la opcion de la aplicacion
resultado = comparar_opciones(opcion_usuario, opcion_aplicacion)
# llama la funcion que se encarga de mostrar el resultado de la partida
mostrar_resultado(resultado)
# llama la funcion que se encarga de preguntar si el usuario desea volver a jugar
#preguntar_volver_a_jugar()
respuesta= preguntar_volver_a_jugar()

# llama la funcion que se encarga de validar la respuesta del usuario
validar_respuesta(respuesta)
# # llama la funcion que se encarga de validar que el usuario solo inserte numeros
# validar_numero(numero)
# # llama la funcion que se encarga de validar que el usuario solo inserte numeros enteros
# validar_numero_entero(numero)
# # llama la funcion que se encarga de validar que el usuario solo inserte numeros positivos
# validar_numero_positivo(numero)
# # llama la funcion que se encarga de validar que el usuario solo inserte numeros positivos menores a 4
# validar_numero_positivo_menor_a_4(numero)
# # llama la funcion que se encarga de validar que el usuario solo inserte numeros positivos mayores a 0
# validar_numero_positivo_mayor_a_0(numero)
# llama la funcion que se encarga de validar que el usuario solo inserte si o no
validar_si_o_no(respuesta)
# # llama la funcion que se encarga de mostrar un mensaje de alerta y volver a pedir la opcion
mostrar_alerta()




# crea una funcion que se encargue de mostrar un mensaje de despedida y cerrar la aplicacion
def despedida():
    print("adios")
    exit()


