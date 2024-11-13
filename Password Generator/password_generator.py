import random
import string


for i in range(4):
    char = string.ascii_letters + string.digits + string.ascii_uppercase + string.punctuation
    password_length = random.randint(9, 13) #  this can be used to generate random password with different lengths and we can use this in k perameter down here 
    random_char = random.choices(char, k= password_length)
    #password = ''.join(random.sample(char, 13)) we can use this only wnen we want the length of the password similar
    password = ''.join(random_char)
    print(password)
