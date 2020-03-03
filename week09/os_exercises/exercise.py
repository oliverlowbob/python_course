fileName = input("Filename: ")
input1 = input("Write to file: ")


f = open(fileName+".txt", "w")
f.write (input1)
f.close()