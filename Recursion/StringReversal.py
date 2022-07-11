from tokenize import String


def StringReversal(string):
    if string == "":
        return ""
    return StringReversal(string[1:]) + string[0]

print(StringReversal("hello"))