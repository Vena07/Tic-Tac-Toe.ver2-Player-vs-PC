import random
import time

print(" ")
print("Tic-Tac-Toe(Player vs PC)")

pole1 = "1"
pole2 = "2"
pole3 = "3"
pole4 = "4"
pole5 = "5"
pole6 = "6"
pole7 = "7"
pole8 = "8"
pole9 = "9"

vyhodnoceno = True
konec = False
vyhra = False

def VyberPrvnihoKola():
    global pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9
    vybrano = False
    while not vybrano:
        cislo = random.randint(1, 9)
        if cislo == 1:
            if pole1 == "1":
                pole1 = "O"
                vybrano = True
        elif cislo == 2:
            if pole2 == "2":
                pole2 = "O"
                vybrano = True
        elif cislo == 3:
            if pole3 == "3":
                pole3 = "O"
                vybrano = True
        elif cislo == 4:
            if pole4 == "4":
                pole4 = "O"
                vybrano = True
        elif cislo == 5:
            if pole5 == "5":
                pole5 = "O"
                vybrano = True
        elif cislo == 6:
            if pole6 == "6":
                pole6 = "O"
                vybrano = True
        elif cislo == 7:
            if pole7 == "7":
                pole7 = "O"
                vybrano = True
        elif cislo == 8:
            if pole8 == "8":
                pole8 = "O"
                vybrano = True
        elif cislo == 9:
            if pole9 == "9":
                pole9 = "O"
                vybrano = True

def SanceVyhry():
    global  pole1, pole2,pole3 ,pole4,pole5,pole6,pole7,pole8,pole9,vyhra 
    if pole1 == pole2 == "O" and pole3 == "3":
        pole3 = "O"
        vyhra = True
    elif pole2 == pole3 == "O" and pole1 == "1":
        pole1 = "O"
        vyhra = True
    elif pole1 == pole3 == "O" and pole2 == "2":
        pole2 = "O"
        vyhra = True
    else:
        if pole7 == pole8 == "O" and pole9 == "9":
            pole9 = "O"
            vyhra = True
        elif pole8 == pole9 == "O" and pole7 == "7":
            pole7 = "O"
            vyhra = True
        elif pole7 == pole9 == "O" and pole8 == "8":
            pole8 = "O"
            vyhra = True
        else:
            if pole1 == pole5 == "O" and pole9 == "9":
                pole9 = "O"
                vyhra = True
            elif pole5 == pole9 == "O" and pole1 == "1":
                pole1 = "O"
                vyhra = True
            elif pole1 == pole9 == "O" and pole5 == "5":
                pole5 = "O"
                vyhra = True
            else:
                if pole3 == pole5 == "O" and pole7 == "7":
                    pole7 = "O"
                    vyhra = True
                elif pole5 == pole7 == "O" and pole3 == "3":
                    pole3 = "O"
                    vyhra = True
                elif pole3 == pole7 == "O" and pole5 == "5":
                    pole5 = "O"
                    vyhra = True
                else:
                    if pole7 == pole4 == "O" and pole1 == "1":
                        pole1 = "O"
                        vyhra = True
                    elif pole4 == pole1 == "O" and pole7 == "7":
                        pole7 = "O"
                        vyhra = True
                    elif pole7 == pole1 == "O" and pole4 == "4":
                        pole4 = "O"
                        vyhra = True    
                    else:      
                        if pole8 == pole5 == "O" and pole2 == "2":
                            pole2 = "O"
                            vyhra = True
                        elif pole5 == pole2 == "O" and pole8 == "8":
                            pole8 = "O"
                            vyhra = True
                        elif pole8 == pole2 == "O" and pole5 == "5":
                            pole5 = "O"
                            vyhra = True
                        else:
                            if pole9 == pole6 == "O" and pole3 == "3":
                                pole3 = "O"
                                vyhra = True
                            elif pole6 == pole3 == "O" and pole9 == "9":
                                pole9 = "O"
                                vyhra = True
                            elif pole9 == pole3 == "O" and pole6 == "6":
                                pole6 = "O"
                                vyhra = True
                            else:
                                if pole4 == pole5 == "O" and pole6 == "6":
                                    pole6 = "O"
                                elif pole6 == pole5 == "O" and pole4 == "4":
                                    pole9 = "O"
                                elif pole4 == pole6 == "O" and pole5 == "5":
                                    pole5 = "O"                        

def SanceBloku():
        global  pole1, pole2,pole3 ,pole4,pole5,pole6,pole7,pole8,pole9,vyhodnoceno  
        vyhodnoceno = True
        if pole1 == pole2 == "X" and pole3 == "3":
            pole3 = "O"
            vyhodnoceno = False
        elif pole2 == pole3 == "X" and pole1 == "1":
            pole1 = "O"
            vyhodnoceno = False
        elif pole1 == pole3 == "X" and pole2 == "2":
            pole2 = "O"
            vyhodnoceno = False
        else:
            if pole7 == pole8 == "X" and pole9 == "9":
                pole9 = "O"
                vyhodnoceno = False
            elif pole8 == pole9 == "X" and pole7 == "7":
                pole7 = "O"
                vyhodnoceno = False
            elif pole7 == pole9 == "X" and pole8 == "8":
                pole8 = "O"
                vyhodnoceno = False
            else:
                if pole1 == pole5 == "X" and pole9 == "9":
                    pole9 = "O"
                    vyhodnoceno = False
                elif pole5 == pole9 == "X" and pole1 == "1":
                    pole1 = "O"
                    vyhodnoceno = False
                elif pole1 == pole9 == "X" and pole5 == "5":
                    pole5 = "O"
                    vyhodnoceno = False
                else:
                    if pole3 == pole5 == "X" and pole7 == "7":
                        pole7 = "O"
                        vyhodnoceno = False
                    elif pole5 == pole7 == "X" and pole3 == "3":
                        pole3 = "O"
                        vyhodnoceno = False
                    elif pole3 == pole7 == "X" and pole5 == "5":
                        pole5 = "O"
                        vyhodnoceno = False
                    else:
                        if pole7 == pole4 == "X" and pole1 == "1":
                            pole1 = "O"
                            vyhodnoceno = False
                        elif pole4 == pole1 == "X" and pole7 == "7":
                            pole7 = "O"
                            vyhodnoceno = False
                        elif pole7 == pole1 == "X" and pole4 == "4":
                            pole4 = "O"
                            vyhodnoceno = False
                        else:
                            if pole8 == pole5 == "X" and pole2 == "2":
                                pole2 = "O"
                                vyhodnoceno = False
                            elif pole5 == pole2 == "X" and pole8 == "8":
                                pole8 = "O"
                                vyhodnoceno = False
                            elif pole8 == pole2 == "X" and pole5 == "5":
                                pole5 = "O"
                                vyhodnoceno = False
                            else:
                                if pole9 == pole6 == "X" and pole3 == "3":
                                    pole3 = "O"
                                    vyhodnoceno = False
                                elif pole6 == pole3 == "X" and pole9 == "9":
                                    pole9 = "O"
                                    vyhodnoceno = False
                                elif pole9 == pole3 == "X" and pole6 == "6":
                                    pole6 = "O"
                                    vyhodnoceno = False
                                else:
                                    if pole4 == pole5 == "X" and pole6 == "6":
                                        pole6 = "O"
                                        vyhodnoceno = False
                                    elif pole6 == pole5 == "X" and pole4 == "4":
                                        pole9 = "O"
                                        vyhodnoceno = False
                                    elif pole4 == pole6 == "X" and pole5 == "5":
                                        pole5 = "O"
                                        vyhodnoceno = False 

def Pole():
    for i in range(2):
        print(" ")
    
    print(" ")
    print(f" {pole7} │ {pole8} │ {pole9}")
    print(f"───┼───┼───")
    print(f" {pole4} │ {pole5} │ {pole6}")
    print(f"───┼───┼───")
    print(f" {pole1} │ {pole2} │ {pole3}")
    print(" ")

def VyberPole():
    global pole1, pole2,pole3 ,pole4,pole5,pole6,pole7,pole8,pole9
    if vybrane == 1:
        pole1 = "X"
    elif vybrane == 2:
        pole2 = "X"
    elif vybrane == 3:
        pole3 = "X"
    elif vybrane == 4:
        pole4 = "X"
    elif vybrane == 5:
        pole5 = "X"
    elif vybrane == 6:
        pole6 = "X"
    elif vybrane == 7:
        pole7 = "X"
    elif vybrane == 8:
        pole8 = "X"
    elif vybrane == 9:
        pole9 = "X"
    
def vyhodnoceni():
    global vyhra
    if pole1 == pole2 == pole3 or pole4 == pole5 == pole6 or pole7 == pole8 == pole9 or pole1 == pole4 == pole7 or pole2 == pole5 == pole8 or pole3 == pole6 == pole9 or pole7 == pole5 == pole3 or pole9 == pole5 == pole1:
        vyhra = True

def Remiza():
    global vyhra
    if (pole1 == "X" or pole1 == "O") and (pole2 == "X" or pole2 == "O") and (pole3 == "X" or pole3 == "O") and (pole4 == "X" or pole4 == "O") and (pole5 == "X" or pole5 == "O") and (pole6 == "X" or pole6 == "O") and (pole7 == "X" or pole7 == "O") and (pole8 == "X" or pole8 == "O") and (pole9 == "X" or pole9 == "O"):
        Pole()
        print("Konec hry")
        vyhra = True   
    
kolo=0

while konec == False:
    Pole()
    print("Hráč X:")
    kontrola = True
    while kontrola== True:
        vybrane = int(input("Vyberte si pole: "))
        if vybrane < 1 or vybrane > 9:
            print("Vybrali jste špatné pole!")
        else:
            kontrola = False
    VyberPole()
    vyhodnoceni()
    Remiza()
    if vyhra == True:
        Pole()
        print("Konec hry")
        break
    
    
    Pole()
    print("Hráč O:")
    print("Vybírá pole")
    time.sleep(2)
    if kolo==0:
        VyberPrvnihoKola()
        kolo+=1
    else:
        SanceVyhry()

        if vyhra==False:
            SanceBloku()
            if vyhodnoceno == True:
                VyberPrvnihoKola()
    
    Remiza()
    if vyhra == True:
        Pole()
        print("Konec hry")
        break
    