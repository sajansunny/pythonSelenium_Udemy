file = open('test.txt')
#print(file.read())          # To read whole file
#print(file.read(2))         # To print first 2 characters
#print(file.readline())      # To print first line from the file
#print(file.readline())      # Curser will move to second line and print the value

# line = file.readline()      # To print whole file by using readline()
# while line != "":
#     print(line)
#     line = file.readline()

for line in file.readlines():   # To print whole file using readlines()
    print(line)

file.close()
