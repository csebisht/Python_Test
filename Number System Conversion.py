# binary
# Decimal
# Octal
# HexDecimal

def binarytodeciaml(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


num1 = int(input("please Enter the Value"))
num2 = bin(num1).replace("0b", " ")
print("Binary conversion of ", bin(num1), "is", binarytodeciaml(int(num2)))
