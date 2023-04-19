


def add(left, right):

    number_left = []
    number_right = []
    var_left = []
    var_right = []
    global number_adding
    global result
        
    if str(right).isnumeric() and str(left).isnumeric():
        result = int(right) + int(left)
    elif str(right).isnumeric():
        number_adding += int(right)
        result = left


    else:

        for stelle in str(left):

            if stelle.isnumeric():
                number_left.append(stelle)
        
            elif stelle.isalpha():
                var_left.append(stelle)

        for stelle in str(right):

            if stelle.isnumeric():
                number_right.append(stelle)
                
            elif stelle.isalpha():
                var_right.append(stelle)
            
        var_left = sorted(var_left)
        var_right = sorted(var_right)

        if len(number_left) == 0:
            number_left.append("1")

        if len(number_right) == 0:
            number_right.append("1")

        if var_left == var_right:
            r1 = int("".join(number_left)) + int("".join(number_right))
            r2 = str("".join(var_left))
            result = f"{r1}{r2}"

        else:
            result = f"{left} + {right}"
            # wichtig ! noch falsch
            #groß!

def substract(left, right):
    
    number_left = []
    number_right = []
    var_left = []
    var_right = []
    global number_adding
    global result

    if str(right).isnumeric() and str(left).isnumeric():
        result = int(right) - int(left)
    elif str(right).isnumeric():
        number_adding -= int(right)
        result = left


    else:

        for stelle in str(left):

            if stelle.isnumeric():
                number_left.append(stelle)
                
            elif stelle.isalpha():
                    var_left.append(stelle)

        for stelle in str(right):

            if stelle.isnumeric():
                number_right.append(stelle)
                
            elif stelle.isalpha():
                var_right.append(stelle)        
            
        var_left = sorted(var_left)
        var_right = sorted(var_right)

        if len(number_left) == 0:
            number_left.append("1")

        if len(number_right) == 0:
            number_right.append("1")

        if var_left == var_right:

            if number_left == number_right:
                result = 0

            else:
                r1 = int("".join(number_left)) - int("".join(number_right))
                r2 = str("".join(var_left))
                result = f"{r1}{r2}"

        else:
            result = f"{left} - {right}"
            # wichtig ! noch falsch 2
            # groß!



def multiply(left, right):

    number_left = []
    number_right = []
    var_left = []
    var_right = []
    global number_adding
    global result

    if str(right).isnumeric() and str(left).isnumeric():
        result = int(left) * int(right)

    elif str(right).isnumeric() or str(left).isnumeric():
        for stelle in str(left):

            if stelle.isnumeric():
                number_left.append(stelle)
            
            elif stelle.isalpha():
                var_left.append(stelle)

        for stelle in str(right):

            if stelle.isnumeric():
                number_right.append(stelle)
                
            elif stelle.isalpha():
                var_right.append(stelle)        
            
        var_left = sorted(var_left)
        var_right = sorted(var_right)

        if len(number_left) == 0:
            number_left.append("1")

        if len(number_right) == 0:
            number_right.append("1")

        if str(right).isnumeric() and not str(left).isnumeric():
            r1 = int("".join(number_left)) * int("".join(number_right))
            r2 = str("".join(var_left))
            result = f"{r1}{r2}"
        
        elif str(left).isnumeric() and not str(right).isnumeric():
            r1 = int("".join(number_left)) * int("".join(number_right))
            r2 = str("".join(var_right))
            result = f"{r1}{r2}"


    else:

        # ab jetzt bis divide von Mario
        #
        #
        #


        number_right = [] #Leere Listen  zum Aufteilen von "left" und "right"
        number_left = []
        var_right = ["null"]
        var_left = ["null"]
        exponents_right = []
        exponents_left = []
        merging_exponents = []
        merged_exponents_left = ["null"]
        merged_exponents_right = ["null"]
        all_vars = []
        vars_result = []
        index = 0
        power_right = False
        power_left = False
        adding_exponent = 0

        #print("\n")

        for char in left:

            if char == "^":
                power_left = True
                #print(f"Power Left: {power_left}")
            
            if char.isnumeric() and power_left == True:
                exponents_left.append(char)
                #print(f"Exponents Left: {exponents_left}")

            elif char.isnumeric() or char == "-" or char == ",":
                number_left.append(char)
                #print(f"Number Left: {number_left}")

            elif char.isalpha():
                
                if not char in all_vars:
                    all_vars.append(char)
                    all_vars.append(0)

                var_left.append(char)
                exponents_left.append(char)

                #print(f"Var Left: {var_left}")
                #print(f"Exponents Left: {exponents_left}")
            

                
        #print("\n")


        for char in right:

            if char == "^":
                power_right = True
                #print(f"Power Right: {power_right}")
            
            if char.isnumeric() and power_right == True:
                exponents_right.append(char)
                #print(f"Exponents Right: {exponents_right}")

            elif char.isnumeric() or char == "-" or char == ",":
                number_right.append(char)
                #print(f"Number Right: {number_right}")

            elif char.isalpha():

                if not char in all_vars:
                    all_vars.append(char)
                    all_vars.append(0)
                
                var_right.append(char)
                exponents_right.append(char)

                #print(f"Var Right: {var_right}")
                #print(f"Exponents Right: {exponents_right}")



        if len(number_right) ==  0:
            number_right.append("1")
        if len(number_left) ==  0:
            number_left.append("1")

        if number_left == "-" and len(number_left) == 1:
            number_left[0] = number_left[0].replace("-", "-1")

        if number_right == "-" and len(number_right) == 1:
            number_right[0] = number_right[0].replace("-", "-1")

        exponents_right.append("null")
        exponents_left.append("null")

        index = 0
        
        for element in exponents_left:

            if index == len(exponents_left) - 1:
                break

            next_element = exponents_left[index + 1]
            
            if element.isnumeric() and not next_element.isalpha():
                merging_exponents.append(element)

            elif element.isalpha():
                merged_exponents_left.append(element)
                merging_exponents = []

            else:
                merging_exponents.append(element)

                
                merged_exponents_left.append(float("".join(merging_exponents)))
                merging_exponents = []
            index += 1

        merged_exponents_left.append("null")
        #print(f"Merged Exponents LEFT: {merged_exponents_left}")

        index = 0

        for element in exponents_right:

            if index == len(exponents_right) - 1:
                break

            next_element = exponents_right[index + 1]
            
            if element.isnumeric() and not next_element.isalpha():
                merging_exponents.append(element)

            elif element.isalpha():
                merged_exponents_right.append(element)
                merging_exponents = []

            else:
                merging_exponents.append(element)

                
                merged_exponents_right.append(float("".join(merging_exponents)))
                merging_exponents = []
            index += 1

        merged_exponents_right.append("null")
        #print(f"Merged Exponents right: {merged_exponents_right}")
        





        
        index = 0


        #print("\n")
        #print(f"Final Merged Exponents LEFT: {merged_exponents_left}")
        #print(f"Fianl Merged Exponents RIGHT: {merged_exponents_right}")


        numbers_result  = float("".join(number_right)) * float("".join(number_left))
        #print(f"Numbers Result: {numbers_result}")

        #print(f"\n All Vars: {all_vars}")


        all_exponents = merged_exponents_left + merged_exponents_right


        for element in all_exponents:
            try:
                all_exponents.remove("null")
            except:
                pass
        

        #all_vars.append("null")
        #print(f"All Exponents: {all_exponents}")
        #print(f"All Vars(h): {all_vars}")

        
        index = 0
    
        for element in all_vars:
            #print(f"Element: {element}")

            
            if str(element).isalpha() and not element == "null":
                
                var_index = all_vars.index(element)

                
                for element2 in all_exponents:
                    #print(f"Element2: {element2} \n")

                    if element == element2:
                        
                        print(all_vars[var_index + 1])
                        print(f"Number: {all_exponents[index + 1]}")
                        
                        all_vars[var_index + 1] += all_exponents[index + 1]


                    index += 1
                index = 0

        #print("\n")

        for element in all_vars:
            
            if str(element).isalpha():
                vars_result.append(element)
                vars_result.append("^")

            else:
                vars_result.append(str(element))
            
            #print(f"Vars Ressult: {vars_result}")


        vars_result = "".join(vars_result)
        #print(f"Vars Ressult: {vars_result}")
        #print(f"All Vars: {all_vars}")

        
        result = f"{numbers_result}{vars_result}"
    
    #
    #
    #
    #


def divide(left, right):

    number_left = []
    number_right = []
    var_left = []
    var_right = []
    global number_adding
    global result

        

    if str(right).isnumeric() and str(left).isnumeric():
        result = int(left) / int(right)
        
    else:

        for stelle in str(left):

            if stelle.isnumeric():
                number_left.append(stelle)
                
            elif stelle.isalpha():
                var_left.append(stelle)

        for stelle in str(right):

            if stelle.isnumeric():
                number_right.append(stelle)
                
            elif stelle.isalpha():
                var_right.append(stelle)        
            
        var_left = sorted(var_left)
        var_right = sorted(var_right)

        if len(number_left) == 0:
            number_left.append("1")

        if len(number_right) == 0:
            number_right.append("1")

        if var_left == var_right:
            result =  int("".join(number_left)) / int("".join(number_right))
            #s.o.

        elif str(right).isnumeric() and not str(left).isnumeric():
            r1 = int("".join(number_left)) / int("".join(number_right))
            r2 = str("".join(var_left))
            result = f"{r1}{r2}"
            # was wenn 0a ??
            
        elif str(left).isnumeric() and not str(right).isnumeric():
            print("Wir können noch nicht gut Zahlen durch Variablen teilen. Dies wir zu Fehlern führen")
            # 1 / a ?!?!
            result = f"{left} / {right}"

        else:
            result = f"{left} / {right}"
            # wichtig ! noch falsch 11
            # was wenn geteilt 0 !!!




term = input("Schreibe jetzt deinen Term ! \t") 

term = term.replace(" ","")
print(term)

term = term.replace("+","_+_")
term = term.replace("-","_-_")
term = term.replace("*","_*_")
term = term.replace("/","_/_")

split_term = term.split("_")
print(split_term)

end_result = []

number_adding = 0

while "*" in split_term or "/" in split_term:

    if "/" in split_term:
        operator_index_divide = split_term.index("/")
    else:
        operator_index_divide = 999999999
    if "*" in split_term:
        operator_index_multiply = split_term.index("*")
    else:
        operator_index_multiply = 999999999

    if operator_index_divide < operator_index_multiply:
            operator_index = operator_index_divide
    elif operator_index_multiply < operator_index_divide:
        operator_index = operator_index_multiply
    
    operator = split_term[operator_index]
    left = split_term[operator_index - 1]
    right = split_term[operator_index + 1]

    if operator == "*":
        multiply(left, right)

    if operator == "/":
        divide(left, right)

    del split_term[operator_index + 1]
    del split_term[operator_index]
    del split_term[operator_index - 1]
    split_term.insert(operator_index - 1, result)
    print(split_term)
    print(number_adding)


while len(split_term) > 1:

    if "+" in split_term:
        operator_index_add = split_term.index("+")
    else:
        operator_index_add = 999999999
    if "-" in split_term:
        operator_index_substract = split_term.index("-")
    else:
        operator_index_substract = 999999999

    if operator_index_substract < operator_index_add:
            operator_index = operator_index_substract
    elif operator_index_add < operator_index_substract:
        operator_index = operator_index_add
    
    operator = split_term[operator_index]
    left = split_term[operator_index - 1]
    right = split_term[operator_index + 1]

    if operator == "+":
        add(left, right)

    if operator == "-":
        substract(left, right)


    del split_term[operator_index + 1]
    del split_term[operator_index]
    del split_term[operator_index - 1]
    split_term.insert(operator_index - 1, result)
    print(split_term)
    print(number_adding)

     
print(split_term) #
print(number_adding) #

end_term = str(split_term)
end_term = end_term.replace("[","")
end_term = end_term.replace("]","")
end_term = end_term.replace("'","")
end_term = end_term.replace(","," ")

if str(end_term).isnumeric():
    end_result = int(end_term) + number_adding
elif number_adding == 0:
    end_result = "".join(split_term)
else:
    if number_adding >= 0:
        end_result = f"{end_term} + {number_adding}"
    else:
        end_result= f"{end_term} {number_adding}"

    
print(f"Endergebniss: {end_result}")