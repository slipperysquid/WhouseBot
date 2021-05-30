
def make_readable_list(message):
    words = []
    word = ""
    for i in range(0, len(message)):
        if ((ord(message[i]) >= 97 and ord(message[i]) <= 122)):
            word += message[i]
            if(i == len(message)):
                words.append(word)
        else:
            words.append(word)
            word = ""
    
    return words
