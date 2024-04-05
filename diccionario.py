#diccionario perro
perro={}
print("lista vacia:", perro,)

#añadir elementos a perro
perro['nombre']="cerberus"
perro['color']="azabache"
perro['raza']="chihuahua"
perro['cabezas']= 3
perro['patas']= 4
perro['edad']="1 milenio"
print("\n","elementos agregados a perro:",perro,)

#diccionario estudiante
estudiante={
    "nombre":"sebastian",
    "apellido":"perea",
    "sexo":"masculino",
    "edad": 18,
    "estado civil": "soltero",
    "habilidades": ["python", "html","java","javascrip" , "linux"],
    "país": "colombia",
    "ciudad": "cartagena",
    "dirección": "paraiso #2"
}
print("\n","diccionario estudiante:","\n", estudiante)

#longitud de estudiante
print("\n","longitud del diccionario estudiante: ",len(estudiante), "\n")

#valor de las habilidades y tipo de datos usando una lista
print("el tipo de dato de las habilidades es:\n",type(estudiante["habilidades"]))

#añadir habilidades
estudiante["habilidades"].extend(["cocinar"])
estudiante["habilidades"].extend(["lavar"])
print("\n lista con habilidades añadidas:\n",estudiante["habilidades"],"\n")

#obtener claves
print("claves de estudiante: \n",estudiante.keys(),"\n")

#obtener valores
print("valores de estudiante: \n",estudiante.values(), "\n")

#Cambie el diccionario a una lista de tuplas utilizando el método items()
tupla_estudiante = estudiante.items()
print("la lista en tuplas:\n",tupla_estudiante, "\n")

#quitar un elemento
del estudiante["habilidades"]
print("la lista sin el elemento habilidades: \n",estudiante, "\n")

#borrar el diccionario estudiante
estudiante.clear()
print("luego de vaciar la lista estudiante, queda:\n",estudiante)
