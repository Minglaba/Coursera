# equal: ==
# not equal: !=
# greater than: >
# less than: <
# greater than or equal to: >=
# less than or equal to: <=





# Inequality Sign

i = 2
i != 6
# this will print true


# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"


# Compare characters

'B' > 'A'




# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
    
    
    
    # Write your code below and press Shift+Enter to execute
album_year = 1991
if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print(album_year)
else:
    print("no data")
