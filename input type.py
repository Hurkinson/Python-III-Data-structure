#Recall that input from a user is always in the form of a string. 
#Write a function called "input_type" that gets user input and 
#determines what kind of string the user entered. The user input
#will be supplied as an argument to the function like normal.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False". 
#  - Otherwise, you should return "string".


#Write your function here!
def input_type(astr):
    result =[]
    final="string"
    if astr == "True" or astr == "False":
        final = "boolean"
    elif astr.isdigit():
        final = "integer"     
    
    else:
        for c in astr:
            if ord(c) in range(48,58) or ord(c) == 46:
                result.append(c)
                #♠print(result)
                if len(result) == len(astr):
                    final = "float"
                    #print(result)
        
         
    return final

#---------------------------------------------------------------
def input_type(user_input):
    if user_input == "True" or user_input == "False":
        return "boolean"

    #Notice that we didn't use an else here. The only way
    #the next line is reachable is if line 13 didn't run,
    #so we don't need an else.
    
    try:
        int(user_input)
        
        #If user_input is not a string representing an
        #integer, then line 20 above will cause an error.
        #So, line 27 will only be reached if user_input
        #is a string holding an error.
        
        return "integer"
    
    except:
        
        #We can only reach this point if user_input was
        #neither "True" or "False" and if it caused an
        #error when casting to an integer. So, we try
        #to cast it to a float:
        
        try:
            float(user_input)
            
            #Return "float" if the above operation didn't
            #cause an error:
            
            return "float"
        
        except:
            
            #And return "string" if it did:
            
            return "string"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#string
#boolean
#float
#integer
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))
