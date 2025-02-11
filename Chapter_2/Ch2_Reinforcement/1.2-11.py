'''
2-11. Adding Comments: Choose two of the programs you’ve written, and 
add at least one comment to each. If you don’t have anything specific to write 
because your programs are too simple at this point, just add your name and the 
current date at the top of each program file. Then write one sentence describing 
what the program does.
'''

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case

    #added a name "Jacob Reed" to the variable 'name'
name = ("Jacob Reed")

    #printing each statement in lowercase, uppercase and titlecase
print(name.lower())
print(name.upper())
print(name.title())

#  2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
    #Adding the name "-Michelle Hodkin" to the 'famous_person" variable
famous_person= ("-Michelle Hodkin")
    #Adding text to the 'message' variable
message = ("'I'll walk forever with stories inside me that the people I love the most can never hear.'")
    #creating an f-string, then using the variable 'message' and 'famous_person' to print a string
print(f" {message}\n{famous_person}")
