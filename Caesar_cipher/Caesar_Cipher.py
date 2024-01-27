import random as r
from ccart import symbols
print(symbols[0])
def encode_mess():
    print(symbols[1])
    mess=input("Enter your message")
    shift=r.randint(5,20)
    encrypted=""
    for i in mess:
        encrypted+=chr(ord(i)+shift)
    print(f"The encrypted message is {encrypted} and the key is {shift*2}")
def decode_mess():
    print(symbols[2])
    mess = input("Enter your message")
    shift= int(int(input("Enter the key "))/2)
    decrypted=""
    for i in mess:
        decrypted+=chr(ord(i)-shift)
    print(f"The decrypted message is {decrypted}")


while True:
    choice=input("Enter encode to encode your message or decode to decode a message \n").lower()

    if choice == "encode":
        encode_mess()
    elif choice == "decode":
        decode_mess()
    x=input("restart:y,n")
    if x=="n":
        exit()
