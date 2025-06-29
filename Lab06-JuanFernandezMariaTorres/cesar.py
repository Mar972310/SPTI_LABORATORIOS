def getIndex(abc , letter):
    return abc.index(letter)

def getLetter(abc, index):
    return abc[index]
    
def enc(k,abc, str):
    response = ""
    for i in range(len(str)):
        index_act = getIndex(abc,str[i])
        new_index = (index_act + k) % 26
        response += getLetter(abc,new_index)
    return response

def dec(k,abc,str):
    response = ""
    for i in range(len(str)):
        index_act = getIndex(abc,str[i])
        new_index = (index_act - k) % 26
        response += getLetter(abc,new_index)
    return response

def brute_force(abc,str):
    for i in range (1,26):

        print(dec(i,abc,str))

abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Excersice 1:
print(enc(8,abc,"KZIXDMUQCVMZBXMZBWDMZMTWJWJQVQ"))

#Excersice 2:
print(enc(15,abc,"SECURECOMMUNICATIONREQUIRESKEYS"))

#Excersice 3:
print(enc(4,abc,"MATHEMATICALPROOFBACKSENCRYPTION"))

#Excersice 1.1:
print("Excersice 1:")
brute_force(abc,"KZIXDMUQCVMZBXMZBWDMZMTWJWJQVQ")

#Excersice 2.1:
print("Excersice 2:")
brute_force(abc,"XTRJYXFDIJSYNHPJXXNTSJFWSFYNTS")

#Excersice 3.1:
print("Excersice 3:")
brute_force(abc,"GURDHVPXOEBJASBEQWHFGVAINYIRAG")



