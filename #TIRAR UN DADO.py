#TIRAR UN DADO
print ("¡Proba tu suerte tirando el dado!")
import random

tirar = True 

while tirar: 
    tiro = input('Para tirar el DADO presiona ENTER')
    resultado = random.randint (1,6)
    print ('El resultado de tu tiro es:', resultado)

    if not input ('¿Queres tirar de nuevo? (si/no): ').lower() == 'si':
        break

print ('¡HASTA LA VISTA BABY!')
