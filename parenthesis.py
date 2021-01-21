#Write a function called "in_parentheses" that accepts a 
#single argument, a string representing a sentence that
#contains some words in parentheses. Your function should
#return the contents of the parentheses.
#
#For example:
#
# in_parentheses("This is a sentence (words!)") -> "words!"
#
#If no text appears in parentheses, return an empty string.
#Note that there are several edge cases introduced by this:
#all of the following function calls would return an empty
#string:
#
# in_parentheses("No parentheses")
# in_parentheses("Open ( only")
# in_parentheses("Closed ) only")
# in_parentheses("Closed ) before ( open")
#
#You may assume, however, that there will not be multiple
#open or closed parentheses.


#Write your function here!
def in_parentheses(astr):
    result = ""
    if "(" in astr:
        if ")" in astr:
            start= astr.find("(")+1
            #print(start)
            end= astr.find(")")
            #print(end)
            result= astr[start:end]
            
            
        else: 
            result = ""     
    else: 
        result = ""   
        
    return result
    

#☺-------------------------------------------------------------

'''#There are multiple ways you could do this, but as before,
#each one is short, so we'll cover them all in one file. If
#you want to test out one function in particular, comment
#out or delete the other two (this file will be restored if
#you resubmit your code).
#
#First, the most straightforward way is probably to check
#if there is a valid set of parentheses, then return the
#string inside them if so:

def in_parentheses(sentence):
    
    #First we check if both parentheses are present:
    
    if "(" in sentence and ")" in sentence:
        
        #Then we check if they're in the right order:
        
        if sentence.find("(") < sentence.find(")"):
            
            #If we get here, then it's a valid set,
            #and we can return the substring from
            #the index of ( to the index of ):
            
            return sentence[sentence.find("(") : sentence.find(")")]
    
    #The only way to get to this next line is if the return
    #on line 25 did not run, so we can return a blank
    #string here:
    
    return ""


#However, it feels like that could be simpler. If we had
#gotten rid of the conditionals altogether, line 25 on
#its own works, except it behaves weirdly if the
#parentheses don't both appear because find() returns -1
#if the search argument isn't present. It works fine for
#the case where the parentheses are out of order,
#though because out-of-order the indices yield an empty
#string.
#
#Ideally, we want an operation that just fails if both
#parentheses aren't there... and we have one! The string
#class also has an index() method that works identically
#to find(), except it raises an error if the search
#argument isn't found instead of returning -1. So, we
#can just try the operation from line 25 (with index()
#instead of find() this time), and return "" if we find
#an error.
    

def in_parentheses(sentence):
    try:
        return sentence[sentence.index("(") + 1:sentence.index(")")]
    except ValueError:
        return ""


#There are still other ways you could do this. For
#example, after the initial checks, we could split
#the string first by "(", then split the second
#string that results by ")". The first string from
#the second operation would be the contents of the
#parentheses.
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (including the blank lines):
#words!
#
#as he is doing right now
#
#
#!'''

print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))
