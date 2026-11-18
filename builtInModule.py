import math
print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.ceil(6.3))
print(math.floor(6.9))

import random
print(random.randint(1,100))

a = [1,2,3,4,5]
random.shuffle(a)
print(a)

import time
print(time.time())
#current time
print(time.ctime())

#for delay
print("hello")
time.sleep(3)
print("world!")

import os
#for current working directory
print(os.getcwd())
#list all the files of the current directory
print(os.listdir())