#Write a function called to_metric. to_metric should take
#as input one parameter, a string. The string will represent
#a quantity in imperial volume units, such as "7 cups", "2
#tablespoons", or "8 gallons". to_metric should return the
#equivalent number of milliliters as a float. Round the
#result two two decimal places.
#
#The possible imperial units to handle and their conversion to
#milliliters are:
#
# - gallons: 4546.09 milliliters
# - quarts: 1136.52 milliliters
# - pints: 568.26 milliliters
# - cups: 236.59 milliliters
# - ounces: 28.41 milliliters
# - tablespoons: 14.79 milliliters
# - teaspoons: 4.93 milliliters
#
#Return only the float representing the number of milliliters,
#not the label. For example:
#
#to_metric("7.0 cups") -> 1656.13
#to_metric("2.0 tablespoons") -> 29.58
#to_metric("8.0 gallons") -> 36368.72
#
#You may assume that the string will be formatted like the
#strings above: a decimal number, then a space, then one of
#the following words: cgallons, quarts, pints, cups, ounces,
#tablespoons, teaspoons


#Add your code here!
def to_metric (arg):
    units = {"gallons":4546.09,
             "quarts": 1136.52,
             "pints": 568.26,
             "cups": 236.59,
             "ounces": 28.41,
             "tablespoons": 14.79,
             "teaspoons": 4.93
             }
    
    U_L= arg.split()
    
    result = round(units[U_L[1]]*float(U_L[0]),2)
    
    return result
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1656.13
#29.58
#36368.72
print(to_metric("7.0 cups"))
print(to_metric("2.0 tablespoons"))
print(to_metric("8.0 gallons"))

