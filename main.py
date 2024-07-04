import string
import random
import array

length = int(input("Passwd length: "))


# Define characters
DIGITS = string.digits
LOW_CASE = string.ascii_lowercase
UP_CASE = string.ascii_uppercase
PUNC = string.punctuation


# Combine all characters
combined = DIGITS + UP_CASE + LOW_CASE + PUNC


# Choice random character from defineds
rand_digit = random.choice(DIGITS)
rand_up = random.choice(UP_CASE)
rand_low = random.choice(LOW_CASE)
rand_punc = random.choice(PUNC)

# Create temporary password from randomly choosed
tempwd = rand_digit + rand_up + rand_low + rand_punc

# Temporary passwd redefining with combined characters
# ALGORITHM.
for i in range(length - 4):
    tempwd = tempwd + random.choice(combined)
    tempwd_list = array.array('u', tempwd)
    random.shuffle(tempwd_list)

pwd = ""
for x in tempwd_list:
    pwd = pwd + x

print(pwd)