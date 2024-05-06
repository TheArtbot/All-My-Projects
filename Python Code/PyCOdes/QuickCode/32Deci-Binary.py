import math

def convert(decimal = 0):
    binary = ""
    
    while decimal > 0:
        #print("decimal:",decimal,"\nBinary:",binary)
        if decimal%2 == 0: binary = "0" + binary; decimal /= 2
        else: binary = "1" + binary; decimal = (decimal - 1)/2
    
    
    while len(binary) < 32:
        binary = "0" + binary
    
    parts = (binary[0:20],binary[20:])
    print(parts)
    
    pageNum = 0
    offset = 0
    for i,b in enumerate(parts[0]):
        n = len(parts[0]) - i - 1
        if b == '1': pageNum += pow(2,n)
    for i,b in enumerate(parts[1]):
        n = len(parts[1]) - i - 1
        if b == '1': offset += pow(2,n)
    
    print(pageNum,offset)
    
    return binary

while True:
    print("This will convert a decimal number into a 32 bit binnary number")
    ans = ""
    while not(ans.isdigit()):
        ans = input("Please enter a decimal: ")

    print("Binary 32 bit value:",convert(int(ans)))
        