import os 
import random 
import itertools
import threading
import time
import sys
import shutil


# define a list of characters that will be used to generate random file names
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', '0', '1', '2', '3', '4', '5', '6', '7',
 '8', '9']

# join the current directory and the file name to get the full path of the original image
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Maxwell.png')

# check if the folder "Maxwell" exists in the current working directory, if not create it
save_path = os.path.join(os.getcwd(), "Maxwell")
if not os.path.exists(save_path):
    os.makedirs(save_path)

# defines animate
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

# starts the thread for animate
t = threading.Thread(target=animate)
t.start()

# Creates a infinte loop
while True:

    # generate a random string of 10 characters from the list1
    rand_str = ''.join(random.sample(list1, 10))

    # save the image with the random string as the file name
    shutil.copy2(path, os.path.join(save_path, rand_str + '.png'))
