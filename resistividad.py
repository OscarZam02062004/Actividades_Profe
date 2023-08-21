#Resistencia en un conductor electrico
# R=p*(L/S)
#Este programa va contener caract de materiales precargadas
#En un arreglo agregamos nombre del material y resistividad
#Directorio
resistividad={"al":(0.028,"Aluminio"),"cu":(0.017,"Cobre"),"au":(0.023,"Oro"),"pl":(0.11,"Platino"),"pb":(0.22,"Plomo"),"zn":(0.061,"Zinc")}
L=float(input("Ingresa la longitud del conductor en [m]: "))
while True:
    S=float(input("Ingresa la seccion del conductor en [mm2]: "))
    if S == 0:
        print("Error, la sección no puede ser cero. Ingresa una sección diferente.")
    else:
        break
materiaL=input("Ingresa el simbolo del material: ").lower()

if materiaL in resistividad:
    p=resistividad[materiaL][0]
    print("Resistividad de",resistividad[materiaL][1],"=[ohm.mm1/m]")
    
    R=p*L/S
    print("La resistencia de",R,"ohms")
else:
    print("Material no encontrado   ")