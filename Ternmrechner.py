


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
            r1 = int("".join(number_left)) * int("".join(number_right))
            r2a1 = str("".join(var_left))
            r2 = f"{r2a1}^2"
            result = f"{r1}{r2}"
            # macht noch fehler (prog von mario)  <---

        elif not str(right).isnumeric() and not str(left).isnumeric(): # also unten else
            r1 = int("".join(number_left)) * int("".join(number_right))
            all_var_list = [] # krass selbst
            all_var_list.append("".join(var_left))
            all_var_list.append("".join(var_right))
            all_var_list = sorted(all_var_list)
            print(all_var_list)
            r2 = "".join(all_var_list)
            result = f"{r1}{r2}"
            # macht noch fehler selbst (prog von mario)  <---

        elif str(right).isnumeric() and not str(left).isnumeric():
            r1 = int("".join(number_left)) * int("".join(number_right))
            r2 = str("".join(var_left))
            result = f"{r1}{r2}"
        
        elif str(left).isnumeric() and not str(right).isnumeric():
            r1 = int("".join(number_left)) * int("".join(number_right))
            r2 = str("".join(var_right))
            result = f"{r1}{r2}"

        else:
            result = f"{left} * {right}"
            # wichtig ! noch falsch 11
            # was wenn mal 0 !!!
            #
            #auch siehe oben prog von mario

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
