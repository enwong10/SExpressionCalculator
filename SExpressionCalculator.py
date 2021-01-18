import sys

if __name__ == "__main__":
    #String formatting
    argumentStr = sys.argv[1].replace("(", "( ")
    argumentStr = argumentStr.replace(")", " )")

    #Split string into array by whitespace
    elementArr = argumentStr.split()

    #Error handling
    if not (elementArr[0] == "(" or elementArr[0].isdigit()):
        sys.exit("Invalid Input")

    #Initialize empty list to keep track of nested operations
    elementList = []
    
    for element in elementArr:
        #Case 1: Operation required
        if element == ")":
            #Pop variables from list
            var1 = elementList.pop()
            var2 = elementList.pop()
            operation = elementList.pop()

            #Execute operation and push result back to list
            if operation == "add":
                elementList.append(int(var1) + int(var2))
            elif operation == "multiply":
                elementList.append(int(var1) * int(var2))
            else: 
                sys.exit("Invalid Operation")
        
        #Case 2: Push valid elements to list
        elif element != "(":
            elementList.append(element)
    
    #Print element (result) in list
    print(elementList[0])
