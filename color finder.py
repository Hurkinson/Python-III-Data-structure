#This one is a challenge. There's a lot going on: splitting
#up strings, removing unnecessary characters, converting to
#integers, and running a big conditional. Our solution to
#this is 34 lines -- you can do it!
#
#In web development, it is common to represent a color like 
#this:
#
#  rgb(red_val, green_val, blue_val)
#
#where red_val, green_val and blue_val would be substituted 
#with values from 0-255 telling the computer how much to 
#light up that portion of the pixel. For example:
#
# - rgb(255, 0, 0) would make a color red. 
# - rgb(255, 255, 0) would make yellow, because it is equal 
#   parts red and green. 
# - rgb(0, 0, 0) would make black, the absence of all color.
# - rgb(255, 255, 255) would make white, the presence of all
#   colors equally.
#
#Don't let the function-like syntax here confuse you: here,
#these are just strings. The string "rgb(0, 255, 0)"
#represents the color green.
#
#Write a function called "find_color" that accepts a single 
#argument expected to be a string as just described. Your
#function should return a simplified version of the color
#that is represented according to the following rules:
#
# If there is more red than any other color, return "red".
# If there is more green than any other color, return "green".
# If there is more blue than any other color, return "blue".
# If there are equal parts red and green, return "yellow".
# If there are equal parts red and blue, return "purple".
# If there are equal parts green and blue, return "teal".
# If there are equal parts red, green, and blue, return "gray".
# (even though this might be white or black).


#Write your function here!
def find_color (astr):
    a= astr.replace("rgb(","")
    a= a.replace(")","")
    a= a.replace(",","")
    c_L= a.split()
    rgb = {"red":int(c_L[0]),"green":int(c_L[1]),"blue":int(c_L[2])}
    
        
    if rgb["red"] == rgb["green"] and rgb["red"] == rgb["blue"]:
        return "gray"
    
    elif rgb["red"] > rgb["green"] and rgb["red"] > rgb["blue"]:
        return "red"    
    elif rgb["green"] > rgb["red"] and rgb["green"] > rgb["blue"]:
        return "green"
    elif rgb["blue"] > rgb["red"] and rgb["blue"] > rgb["green"]:
        return "blue"
    
    elif rgb["red"] == rgb["green"] and int(rgb["red"] + rgb["green"]) > 0:
        return "yellow"
    elif rgb["blue"] == rgb["red"] and int(rgb["blue"] + rgb["red"]) > 0:
        return "purple"
    elif rgb["green"] == rgb["blue"] and int(rgb["green"] + rgb["blue"]) > 0:
        return "teal"
    
#-----------------------------------------------------

def_find_color(color_string):
    
    #Now, my first goal is to get rid of the extraneous
    #information. I know that I don't care about the first
    #four or last character:
    
    color_string = color_string[4:-1]
    
    #Now, my string is just the comma-separated part. Now,
    #I could use the split() method, but that gives me a
    #list of strings, and we haven't covered lists yet.
    #So, instead, I'll use string slicing. I know that the
    #red value is the substring from the beginning of the
    #string to the first comma:
    
    red_string = color_string[:color_string.find(",")]
    
    #That gives me the substring representing the red
    #color. Now, to get the green, I want the part between
    #the two commas. I could find the index of the first
    #comma, then search only after that index; or, I could
    #just get rid of the first part of the string up to
    #the first comma. Let's do the latter.
    
    color_string = color_string[color_string.find(",") + 1:]
    
    #Line 22 found the substring from the beginning until
    #the index of ","; line 31 found the rest of the
    #string. The +1 is to skip over the comma itself. So,
    #now color_string has just one comma: before it is the
    #blue value, and after it is the green value. So, we can
    #pull those out easily using the  same lines of code as
    #above. green is now the first value, so the code from
    #line 22 works for green, and blue is now the rest of the
    #string, so the code from line 31 works for blue.
    
    green_string = color_string[:color_string.find(",")]
    blue_string = color_string[color_string.find(",") + 1:]
    
    #Check out sample_answer_2.py for an example using split()
    #for this part instead.
    #
    #Ok, so now we have three strings: one for red, one for
    #green, one for blue. We need to compare their numeric
    #values, though, so we need to cast them to integers.
    #
    #Let's be clever for a second and do that in one compact
    #line:
    
    red, green, blue = int(red_string), int(green_string), int(blue_string)
    
    #Don't let that confuse you: this is exactly the same
    #as saying:
    #red = int(red_string)
    #green = int(green_string)
    #blue = int(blue_string)
    #
    #In Python, using commas on the left and right side of
    #the expression tells Python to assign the values in
    #order on the right to the variables in order on the
    #left.
    #
    #So, now red, green, and blue are our integer values
    #for each color. All that's left is the conditional.
    #Note, though, that if you do the conditional in the
    #wrong order, this can get complicated: you should
    #first check if one number is higher than both the
    #others before checking if two are equal. After all,
    #if red is bigger than both green and blue, then it
    #doesn't matter if green and blue are equal.
    
    if red > green and red > blue:
        return "red"
    elif green > red and green > blue:
        return "green"
    elif blue > green and blue > red:
        return "blue"
    
    #Now we know that if two colors are equal, they're
    #also greater than the third: if the third was
    #greater, it would have been caught by the
    #conditional above.
    #
    #What next? Well, if we check individual pairs,
    #then we'll see that two are equal before seeing if
    #all three are equal. So, we should check all three
    #first:
    
    elif red == green and red == blue:
        return "gray"
    
    #At this point, we know all three aren't equal
    #(because if they were, line 93 would have run). We
    #also know that no one color is greater than both
    #others (because if it was, either line 76, 78, or
    #80 would have run). So, it must be that exactly two
    #are equal. So, we check each pair:
    
    elif red == green:
        return "yellow"
    elif red == blue:
        return "purple"
    elif green == blue:
        return "teal"
    
    #There are lots of other ways we could have done this
    #though. We could have used nested conditionals for
    #the reasoning at the end, or we could have used
    #replace() and split() to get the numbers out of the
    #original string. split() would have been easier,
    #actually, but it would require using lists, which
    #we'll cover in the next chapter.
            
#-------------------------------------------------------------------

def find_color(color_string):
    
    color_string = color_string[4:-1]
    
    #Now, color_string is a string with three numbers
    #separated by two commas. So, we can split by
    #commas...
    
    cs_split = color_string.split(",")
    
    #And now, strings for red, green, and blue are the
    #first, second, and third items in the list:
    
    red, green, blue = int(cs_split[0]), int(cs_split[1]), int(cs_split[2])
    
    #And that's all! split() gave us a list of three
    #strings, and we can access each item in that
    #list using the same syntax we use to access
    #individual characters from a string: cs_split[0]
    #gave the first string, cs_split[1] gave the second,
    #and so on.
    
    if red > green and red > blue:
        return "red"
    elif green > red and green > blue:
        return "green"
    elif blue > green and blue > red:
        return "blue"
    elif red == green and red == blue:
        return "gray"
    elif red == green:
        return "yellow"
    elif red == blue:
        return "purple"
    elif green == blue:
        return "teal"
    
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: red, purple, gray, each on their own line.
print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(217, 217, 217)"))
