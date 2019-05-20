from gpiozero import LED
from time import sleep

grøn1 = LED(17)
gul1 = LED(27)
rød1 = LED(22)
grøn2 = LED(0)
gul2 = LED(5)
rød2 = LED(6)
sving1 = LED(14)
sving2 = LED(25)


    
def state0():
    print("Kombardo!")
    rød2.on()
    grøn1.on()
    sleep(5.5)
    grøn1.off()
    return state1()

def state1():
    print("Taxa Grønt!")
    gul1.on()
    sleep(2)
    gul1.off()
    return state2()

def state2():
    print("Hold For Satan!")
    rød1.on()
    return state7()

def state3():
    print("Gør Dig Klar!")
    sleep(0.75)
    rød1.on()
    sleep(1)
    gul1.on()
    sleep(1.5)
    rød1.off()
    gul1.off()
    return state0()




def state4():
    rød2.off()
    print("Kombardo!")
    grøn2.on()
    sleep(5.5)
    grøn2.off()
    return state5()

def state5():
    print("Taxa Grønt!")
    gul2.on()
    sleep(2)
    gul2.off()
    return state6()

def state6():
    print("Hold For Satan!")
    rød2.on()
    return state3()

def state7():
    print("Gør Dig Klar!")
    sleep(0.75)
    rød2.on()
    sleep(1)
    gul2.on()
    sleep(1.5)
    rød2.off()
    gul2.off()
    return state4()
    


state=state0

while state: state=state()
print()

