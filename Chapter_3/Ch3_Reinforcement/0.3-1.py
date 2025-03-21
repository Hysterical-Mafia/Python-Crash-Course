'''
3-1. Names: Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time.
'''

names = ["Mario", "Luigi", "Donkey Kong", "Bowser"]

for index, name in enumerate(names, start=1):
    print(f"Number {index}: {name}")

    
