
print("nichts3")

class var:

    def add(left, right):

        number_left = []
        number_right = []
        var_left = []
        var_right = []
        global number_adding
        global result

        if str(left).isnumeric():
            number_adding += float(left)
            result = right
            
        if str(right).isnumeric():
            number_adding += float(right)
            result = left

        if str(right).isnumeric() and str(left).isnumeric():
            result = 0

        if not str(right).isnumeric() and not str(left).isnumeric():

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
                r1 = float("".join(number_left)) + float("".join(number_right))
                r2 = str("".join(var_left))
                result = f"{r1}{r2}"

            else:
                result = f"{left} + {right}"
                # wichtig ! noch falsch

    def substract(left, right):

        number_left = []
        number_right = []
        var_left = []
        var_right = []
        global number_adding
        global result

        if str(left).isnumeric():
            number_adding += float(left)
            r1 = str("".join(right))
            result = f"-{r1}"
            print("Wir können noch nicht gut Variablen von Zahlen subtrahieren. Dies wir zu Fehlern führen")
            # wir können nicht variablen subtrahieren, sehr schlecht
            
        if str(right).isnumeric():
            number_adding -= float(right)
            result = left

        if str(right).isnumeric() and str(left).isnumeric():
            result = 0

        if not str(right).isnumeric() and not str(left).isnumeric():

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
                if float("".join(number_left)) - float("".join(number_right)) == 0:
                    result = 0

                else:
                    r1 = float("".join(number_left)) - float("".join(number_right))
                    r2 = str("".join(var_left))
                    result = f"{r1}{r2}"

            else:
                result = f"{left} - {right}"
                # wichtig ! noch falsch 2



    def multiply(left, right):

        number_left = []
        number_right = []
        var_left = []
        var_right = []
        global number_adding
        global result

        

        if str(right).isnumeric() and str(left).isnumeric():
            # eig result = 0
            # eig number_adding += float(left) * float(right)
            # aber dumm:
            result = float(left) * float(right)

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
                r1 = float("".join(number_left)) * float("".join(number_right))
                r2a1 = str("".join(var_left))
                r2 = f"{r2a1}^2"
                result = f"{r1}{r2}"
                # macht noch fehler (prog von mario)

            elif str(right).isnumeric() and not str(left).isnumeric():
                r1 = float("".join(number_left)) * float("".join(number_right))
                r2 = str("".join(var_left))
                result = f"{r1}{r2}"
            
            elif str(left).isnumeric() and not str(right).isnumeric():
                r1 = float("".join(number_left)) * float("".join(number_right))
                r2 = str("".join(var_right))
                result = f"{r1}{r2}"

            else:
                result = f"{left} * {right}"
                # wichtig ! noch falsch 11
                # was wenn mal 0 !!!

    def divide(left, right):

        number_left = []
        number_right = []
        var_left = []
        var_right = []
        global number_adding
        global result

        

        if str(right).isnumeric() and str(left).isnumeric():
            # eig result = 0
            # eig number_adding += float(left) / float(right)
            # aber dumm:
            result = float(left) / float(right)
            # /0 ?!?!
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
                result =  float("".join(number_left)) / float("".join(number_right))
                #s.o.

            elif str(right).isnumeric() and not str(left).isnumeric():
                r1 = float("".join(number_left)) / float("".join(number_right))
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
        var.multiply(left, right)

    if operator == "/":
        var.divide(left, right)

    del split_term[operator_index + 1]
    del split_term[operator_index]
    del split_term[operator_index - 1]
    split_term.insert(operator_index - 1, result)
    print(split_term)


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
        var.add(left, right)

    if operator == "-":
        var.substract(left, right)


    del split_term[operator_index + 1]
    del split_term[operator_index]
    del split_term[operator_index - 1]
    split_term.insert(operator_index - 1, result)
    print(split_term)

     
print(split_term)
print(number_adding)