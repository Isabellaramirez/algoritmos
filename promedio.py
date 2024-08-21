edad = int
cantidad = int(input("cuantos aprendices hay = "))
promedio = 0
i=0
for i in range (cantidad): 
    edad = int(input(f"ingrese su edad"))
    promedio = promedio + edad

promedio = promedio / cantidad 

print ('el promedio es: ', promedio)