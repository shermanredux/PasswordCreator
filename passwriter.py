import secrets

dictionary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$^&*()-=_+?'

def create(pass_word, pass_length):
    for i in range(pass_word):
        list = []
        for i in range(pass_length):
            characters = secrets.choice(dictionary)
            list.append(characters)
        passwords = ''.join(list)
        print(passwords)
    return passwords


create(int(10),int(33))

