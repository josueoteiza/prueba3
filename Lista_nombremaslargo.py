#Solicitar tres nombres al usuario
nombre1=input("Ingrese el primer nombre")
nombre2=input("Ingrese el segundo nombre")
nombre3=input("Ingrese el tercer nombre")

#Almacenar los nombres en una lista
nombres=[nombre1,nombre2,nombre3]

#Encontrar el nombre con mayor cantidad de caracteres
#key=len indicarán al programa ordenar la lista de nombres por longitud, del más pequeño al más largo.
nombre_mas_largo=max(nombres,key=len)

#Mostrar el nombre con mayor cantidad de caracteres
print(f"El nombre con mayor cantidad de caracteres es:{nombre_mas_largo}")