from unittest import result


def DecimalToBinary(decimal, binary):
    if decimal == 0:
        return binary

    binary = str(decimal % 2) + binary
    return DecimalToBinary(decimal // 2, binary)

print(DecimalToBinary(121,""))