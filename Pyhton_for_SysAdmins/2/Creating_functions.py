def Display(message, count=1):
    for i in range(count):
        print(message)

message = raw_input('Message: ')
count = raw_input('Count: ')
if count != "":
    Display(message, int(count))
else:
    Display(message)
