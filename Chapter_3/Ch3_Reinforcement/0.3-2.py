'''
 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each mes
sage should be the same, but each message should be personalized with the 
person’s name.
'''

names = ["Mario", "Luigi", "Donkey Kong", "Bowser"]

for index, name in enumerate(names, start=1):
    print(f"Hello {name}, did you know in my sheet you were at number {index}. Pretty Interesting to me!")

    
