

#Python script for decoding ROT13 cipher
# By => Ahmed Kamal

x = input("Enter The Cipher > ")
x1 = x.lower()
a1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
a2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in x1 :
    if i in a1:
        print (a2[a1.index(i)] , end="")
    elif i in a2:
        print(a1[a2.index(i)] , end="")
    else:
        print(i , end="")

