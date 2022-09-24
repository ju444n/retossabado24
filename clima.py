#bucle de datos 
print("Ingrese datos del clima")

temperaturas=[]
def ingresartemperaturas():
    for x in range(0,3,1):
        temperatura=int(input('Dijite Temperatura del clima: '))
        temperaturas.append(temperatura)

ingresartemperaturas()
print(f'{len(temperaturas)}')