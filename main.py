import math

#numberA = (int(input("Insira o primeiro número: ")))
#print(type(numberA))
#numberB = (int(input("Insira o segundo número: ")))
#c= numberA+numberB
#print(c)

finalValue = "Empty final value"
operation = ""

def menu():
    print("\n*****************************************")
    print("********       Calculadora      *********")
    print("*****************************************\n")    
    calculate()

def calculate():

    ##Código para baixo funciona
    operation = (str(input("Insira a operação que deseja (Ex:*;/;%;+): ")))
    
    if(len(operation)==1 or len(operation)==3 or len(operation)==4):
        if(operation == "+"):
            numberA = (int(input("Insira o primeiro número: ")))
            numberB = (int(input("Insira o segundo número: ")))
            finalValue = numberA + numberB
        elif(operation == "-"): 
            numberA = (int(input("Insira o primeiro número: ")))
            numberB = (int(input("Insira o segundo número: "))) 
            finalValue = numberA - numberB
        elif(operation == "/"):
            numberA = (int(input("Insira o primeiro número: ")))
            numberB = (int(input("Insira o segundo número: ")))
            finalValue = numberA/numberB
        elif(operation == "*"):
            numberA = (int(input("Insira o primeiro número: ")))
            numberB = (int(input("Insira o segundo número: ")))
            finalValue = numberA*numberB
        elif(operation == "%"):
            numberA = (int(input("Insira o primeiro número: ")))
            numberB = (int(input("Insira o segundo número: ")))
            finalValue = numberA%numberB
        elif(operation == "pow"):
            numberA = (int(input("Insira a base: ")))
            numberB = (int(input("Insira o expoente: ")))
            finalValue = numberA ** numberB
        elif(operation == "sqrt"):
            numberA = (int(input("Insira o número: ")))
            finalValue=math.sqrt(numberA)
        else:
            print("** Operação Inválida **")
            input("Pressione ENTER para continuar")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            menu()   

        print("Resultado: ",finalValue,"\n")
        input("Pressione ENTER para continuar")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        menu()              
    else:
        print("\n***Insira uma operação válida***\n")
        input("Pressione ENTER para continuar")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        menu()

#calculate()
menu()