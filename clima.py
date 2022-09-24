#bucle de datos 


print("Ingrese datos del clima")

temperaturas=[]
def ingresartemperaturas():
    for x in range(0,20,1):
        temperatura=int(input('Dijite Temperatura del clima: '))
        temperaturas.append(temperatura)

ingresartemperaturas()


acumulador=0
for y in (temperaturas):
    acumulador=acumulador+y

  
totalTemperatura =acumulador/len(temperaturas)

print(f'resultado de suma de las temperaturas {acumulador}')
print(f'resultado de promedio de temperatura {totalTemperatura}')   



