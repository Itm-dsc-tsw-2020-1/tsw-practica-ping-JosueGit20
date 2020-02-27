import os 
contador = 0
for h in range(1, 255, 1):
    if os.system("ping 200.33.171."+str(h)) == 0:
        contador +=1
        print(" ->SÍ está activa")
    else:
        print(" -> NO está activa")

print("Total activas: " + str(contador) + "\n Total inactivas: " + str(255-contador))

