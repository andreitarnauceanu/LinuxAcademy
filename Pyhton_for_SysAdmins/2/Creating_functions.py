def Display(message, count=1):
    for i in range(int(count)):
        print(message)

message = input('Message: ')
count = input('Count: ')
if count != "":
    Display(message, count)
else:
    Display(message)
