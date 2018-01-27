MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Would you like to encrypt or decrypt a message?')
        mode = input().lower()
        print (mode)
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

