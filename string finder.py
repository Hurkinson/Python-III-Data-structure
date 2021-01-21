#Write a function called string_finder. string_finder should
#take two parameters: a target string and a search string.
#The function will look for the search string within the
#target string.
#
#The function should return a string representing where in
#the target string the search string was found:
#
# - If search string is at the very beginning of target
#   string, then return "Beginning". For example:
#   string_finder("Georgia Tech", "Georgia") -> "Beginning"
#
# - If search string is at the very end of target string,
#   then return "End". For example:
#   string_finder("Georgia Tech", "Tech") -> "End"
#
# - If search string is in target string but not at the
#   very beginning or very end, then return "Middle. For
#   example:
#   string_finder("Georgia Tech", "gia") -> "Middle"
#
# - If search string is not in target string at all, then
#   return "Not found". For example:
#   string_finder("Georgia Tech", "Idaho") -> "Not found"
#
#Assume that we're only interested in the first instance
#of the search string if it appears multiple times in the
#target string, and that search string is definitely
#shorter than target string.
#
#Hint: Don't be surprised if you find that the "End" case
#is the toughest! You'll need to look at the lengths of
#both the target string and the search string.


#Write your function here!
def string_finder(qstr,target):
    if target in qstr:
    
        if target[0] == qstr[0]:
            return "Beginning"
        elif target[len(target)-1] == qstr[len(qstr)-1]:
            return "End"
        else:
            return "Middle"
    else:
        return "Not found"
    
#---------------------------------------------------

def string_finder(target, search):
    
    #Next, the best thing to do would be to go ahead and get
    #and store the index where search is found within
    #target. That's more efficient than calling find() a
    #bunch of times:
    
    index = target.find(search)
    
    #Now based on that index, we can decide where search
    #was found within target. First, find() returns -1 if
    #the string is not found, so if index is less than 0,
    #we can say "Not found":
    
    if index < 0:
        return "Not found"
    
    #Next, 0 is the index for the beginning of the string.
    #So, if index is 0, then search is at the beginning of
    #target:
    
    elif index == 0:
        return "Beginning"
    
    #Now things get trickier. For the search string to be
    #at the end of the target string, it has to be found
    #at an index earlier than the length of the target
    #string. Specifically, it has to be its own length
    #away from the end of the target string. So, we can
    #find that by subtracting the length of the search
    #string from the length of the target string.
    #
    #For example, "Georgia Tech" has 12 characters, and
    #"Tech" has 4 characters. For "Tech" to occur at the
    #end of "Georgia Tech", it must start at index 8,
    #which puts the locations of its characters at
    #indices 8, 9, 10, and 11 (which are the last four
    #indices of a 12-character string since Python is
    #0-indexed).
    
    elif index == len(target) - len(search):
        return "End"
    
    #Finally, the above conditions rule out everything
    #except search being in the middle of target. So,
    #we can return "Middle" if we reach here:
    
    else:
        return "Middle"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Beginning, Middle, End, Not found, each on their own
#line.
print(string_finder("Georgia Tech", "Georgia"))
print(string_finder("Georgia Tech", "gia"))
print(string_finder("Georgia Tech", "Tech"))
print(string_finder("Georgia Tech", "Idaho"))
