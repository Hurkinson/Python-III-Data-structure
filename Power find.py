def powerfind (sequence, target):
    if target in sequence:
        count = 0
        currloc = sequence.find(target)
        while currloc >= 0:
            count += 1
            print("{0} found at index {1}!".format(target,currloc))
            
            currloc = sequence.find(target,currloc+1)
        result = "There is {0} iteration(s) of '{2}' in {1}!".format(count,sequence,target)    
    else:
        result = "{0} was not found within {1}!".format(target, sequence)
    
    return result


print(powerfind("ABCDEFABCDEFABCDEFABCDEFABCDEF", "DEF"))
print(powerfind("ABCDEF", "GHI"))