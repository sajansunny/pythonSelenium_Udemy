ItemsInCart = 0

# if ItemsInCart != 2:
#     raise Exception("Items in cart not equal to 2")

# assert (ItemsInCart == 2)

# try:
#     with open('test1.txt', 'r') as reader:
#         reader.read()
# except:
#     print("Exception handled")

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Clearing the resources")


