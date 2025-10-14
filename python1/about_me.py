#!/usr/bin/env python3
import sys
my_name = "Anastasia"
favorite_color = "Yellow"
favorite_activity = "Painting"
favorite_animal = "Hedgehog"
print(f'''My name is: {my_name}
My favorite color: {favorite_color}
My favorite activity: {favorite_activity}
My favorite animal: {favorite_animal}''')
name = sys.argv[1]
color = sys.argv[2] 
animal = sys.argv[3]
activity = sys.argv[4]
print('My name is:', name, 'My favorite color:', color, 'My favorite animal:', animal, 'My favorite activity is:', activity)
