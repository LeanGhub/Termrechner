from time import sleep
import os



class var:

    def multiply(x, y):
        
        numberx = []
        numbery = []
        vars_result = []
        all_vars= []
        global result
        
        for stelle in x:

            if stelle.isnumeric() or stelle == "-":
                numberx.append(stelle)
#               print(f"NumberX = {numberx}")
            
            elif stelle.isalpha() or stelle == "^" or last_stelle == "^":
                all_vars.append(stelle)
#               print(f"All Variables: {all_vars}")
            
            
            last_stelle = stelle

        for stelle in y:

            if stelle.isnumeric() or stelle == "-":
                numbery.append(stelle)
#               print(f"NumberY = {numbery}")
            
            elif stelle.isalpha():
                all_vars.append(stelle)
#               print(f"All Variables: {all_vars}")

        

        

        

        if len(numberx) == 0:
            numberx.append("1")
        if len(numbery) == 0:
            numbery.append("1")


        if numberx[0] == "-" and len(numberx) == 1:
            numberx[0] = numberx[0].replace("-", "-1")
        
        if numbery[0] == "-" and len(numbery) == 1:
            numbery[0] = numbery[0].replace("-", "-1")
        


        for stelle in all_vars:
            x = all_vars.count(stelle)
            myStr = stelle
#           print("The string is:",myStr)
            myVars = locals()
            myVars[myStr] = x
            vars_result.append(f"{myStr}^{x}")


        r2 = [*set(vars_result)]
        r2.sort()
        r2 = "".join(r2)
        r2 = r2.replace("^1", "")
#       r2 = r2.replace("1", "")  # Es könnte sein, dass diese Zeile alles zerstört.
        

        
        try:
            r1 = int("".join(numberx))  *  int("".join(numbery))
            result = f"{r1}{r2}"
        except:
            result = f"{r2}"


        

#       print(f"Vereinfacht: {result}")




    def add(x, y):
        
        numberx = []
        numbery = []
        varx = []
        vary = []
        vars_result = []
        all_vars= []
        numberx_appended = False
        numbery_appended = False
        global result
        
        for stelle in x:

            if stelle.isnumeric() or stelle == "-":
                numberx.append(stelle)
#               print(f"NumberX = {numberx}")
            
            elif stelle.isalpha():
                varx.append(stelle)
#               print(f"VarX: {varx}")

        for stelle in y:

            if stelle.isnumeric() or stelle == "-":
                numbery.append(stelle)
#               print(f"NumberY = {numbery}")
            
            elif stelle.isalpha():
                vary.append(stelle)
#               print(f"VarY: {vary}")
        
        
        
        
        varx = sorted(varx)
        vary = sorted(vary)



#       print(f"NumberX: {numberx}")
#       print(f"VarX: {varx}")
#       print(f"NumberY: {numbery}")
#       print(f"VarY: {vary}")

        if len(numberx) == 0:
            numberx.append("1")
            numberx_appended = True
        if len(numbery) == 0:
            numbery.append("1")
            numbery_appended = True


        if numberx[0] == "-" and len(numberx) == 1:
            numberx[0] = numberx[0].replace("-", "-1")

        if numbery[0] == "-" and len(numbery) == 1:
            numbery[0] = numbery[0].replace("-", "-1")
            
        


#       print(numberx_appended)
#       print(numbery_appended)

#       print(x, y)

        if varx == vary:


            if numberx != 0    and    numbery != 0    and   int("".join(numberx)) + int("".join(numbery)) != 0:
                r1 = int("".join(numberx)) + int("".join(numbery))
                r2 = "".join(varx)
                result = f"{r1}{r2}"

            elif int("".join(numberx)) + int("".join(numbery)) == 0    and    (numberx_appended == False  and  numbery_appended == False):
                result = 0

            else:
                result = 0
        
        else:
            result = f"{x} + {y}"


        
        


            


#       print(f"Vereinfacht: {result}")



    def substract(x, y):
        
        numberx = []
        numbery = []
        varx = []
        vary = []
        vars_result = []
        all_vars= []
        numberx_appended = False
        numbery_appended = False
        global result
        
        for stelle in x:

            if stelle.isnumeric() or stelle == "-":
                numberx.append(stelle)
#               print(f"NumberX = {numberx}")
            
            elif stelle.isalpha():
                varx.append(stelle)
#               print(f"VarX: {varx}")

        for stelle in y:

            if stelle.isnumeric() or stelle == "-":
                numbery.append(stelle)
#               print(f"NumberY = {numbery}")
            
            elif stelle.isalpha():
                vary.append(stelle)
#               print(f"VarY: {vary}")

        

        varx = sorted(varx)
        vary = sorted(vary)



#       print(f"NumberX: {numberx}")
#       print(f"VarX: {varx}")
#       print(f"NumberY: {numbery}")
#       print(f"VarY: {vary}")

        if len(numberx) == 0:
            numberx.append("1")
            numberx_appended = True

        if len(numbery) == 0:
            numbery.append("1")
            numbery_appended = True

        if numberx[0] == "-" and len(numberx) == 1:
            numberx[0] = numberx[0].replace("-", "-1")

        if numbery[0] == "-" and len(numbery) == 1:
            numbery[0] = numbery[0].replace("-", "-1")
            

#       print(numberx_appended)
#       print(numbery_appended)


        if varx == vary:

            if numberx != 0    and    numbery != 0    and   int("".join(numberx)) - int("".join(numbery)) != 0:
                r1 = int("".join(numberx)) - int("".join(numbery))
                r2 = "".join(varx)
                result = f"{r1}{r2}"

            elif int("".join(numberx)) - int("".join(numbery)) == 0    and    (numberx_appended == True  and  numbery_appended == True):
                result = 0
        else:
            result = f"{x} - {y}"

        
#       print(f"Vereinfacht: {result}")



# / / / / / / / / / / / / / / / / / /

# Hier drunter fängt das eigentliche Rechnen an

# / / / / / / / / / / / / / / / / / /

            
            
            

index = 0

input = input("Schreibe deinen Term: ")

input = input.replace(" ", "")            # Leerzeichen entfernen


input = input.replace("+", "_+_")         # Splitten des Terms Anfang
input = input.replace("-", "_-_")         
input = input.replace("*", "_*_")         # / / / / / / / / / / / / / 
input = input.replace("/", "_/_")
                                          # / / / / / / / / / / / / /
split_input = input.split("_")
print(split_input)                        # Splitten des Terms Ende

term = split_input


solved = False

steps = []

while len(term) > 1:
    

    if term == ['1', '+', '1']:                                   # Sehr dumme Easteregs Anfang
        print("Da weiß doch jeder, dass das 69 ergibt!")
        steps.append("sussy susmongus")
        break


    if "*" in term or "/" in term:
        print("hi2")

        while "*" in term or "/" in term:

            print("stuck")


            for digit in term:

                if term[index] == "*":
                    x = term[index - 1]
                    y = term[index + 1]
                    
                    var.multiply(x, y)
                    
                    print(f"Zwichenergebnis: {result}")
                    
                    term.insert(index, result)
    #               print(term)
                    del term[index + 1]
    #               print(term)
                    del term[index + 1]
    #               print(term)
                    del term[index - 1]
    #               print(term)
                    index = 0
                    steps.append(f"{x} mit {y} multiplizieren")


                    r1 = "".join(term)
                    print(f"Vereinfachter Term: {r1}")


                elif term[index] == "/":
                    print("Im Moment arbeiten wir daran, Dividieren hinzuzufügen.")
                    break

            

            index += 1

        index = 0         # Index zurücksetzen, sodass er nicht außer Reichweite ist.

    for digit in term:

        if term[index] == "+":
            x = term[index - 1]
            y = term[index + 1]
                
            var.add(x, y)
                
            print(f"Ergebnis: {result}")
                
            term.insert(index, result)
#           print(term)
            del term[index + 1]
#           print(term)
            del term[index + 1]
#           print(term)
            del term[index - 1]
#           print(term)
            index = 0
            steps.append(f"{x} und {y} addieren")


            r1 = "".join(term)
            print(f"Vereinfachter Term: {r1}")


        elif term[index] == "-":
            x = term[index - 1]
            y = term[index + 1]
                
            var.substract(x, y)
                
            print(f"Ergebnis: {result}")
                
            term.insert(index, result)
#           print(term)
            del term[index + 1]
#           print(term)
            del term[index + 1]
#           print(term)
            del term[index - 1]
#           print(term)
            index = 0
            steps.append(f"{y} von {x} abziehen")


            r1 = "".join(term)
            print(f"Vereinfachter Term: {r1}")

        index += 1

            
    try:        
        if last_result == result:
            break
    except:
        pass
    
    try:
        last_result = result
    except:
        pass



index = 0



print("Schritte:")
print(steps)
