
def make_readable_list(message):
    words = []
    word = ""
    for i in range(0, len(message) - 1):
        if ((int(readable_message[i]) >= 97 and int(message[i]) <= 122)):
            word += message
        else:
            words += word
            word = ""
    return words
