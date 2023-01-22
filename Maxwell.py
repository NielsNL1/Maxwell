from PIL import Image
import random

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z', '0', '1', '2', '3', '4', '5', '6', '7',
 '8', '9']

# Open the original image
with Image.open("Maxwell.png") as original_image:

  # Create a copy of the image
    duplicate_image = original_image.copy()

 # Convert the image to RGB mode
duplicate_image = duplicate_image.convert("RGB")

while True:
   
   randomlist1 = (random.choice(list1))
   randomlist2 = (random.choice(list1))
   randomlist3 = (random.choice(list1))
   randomlist4 = (random.choice(list1))
   randomlist5 = (random.choice(list1))
   randomlist6 = (random.choice(list1))
   randomlist7 = (random.choice(list1))
   randomlist8 = (random.choice(list1))
   randomlist9 = (random.choice(list1))
   randomlist10 =(random.choice(list1))

   duplicate_image.save(randomlist1 + randomlist2 + randomlist3 + randomlist3 + randomlist4 + randomlist5
    + randomlist6 + randomlist6 + randomlist7 + randomlist8 + randomlist9 + randomlist10 + '.jpg')
