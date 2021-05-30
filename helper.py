
def make_readable_list(message):
    words = []
    word = ""
    for i in range(0, len(readable_message) - 1):
        if ((int(readable_message[i]) >= 97 and int(readable_message[i]) <= 122)):
            word += readable_message
        else:
            words += word
            word = ""
    return words
