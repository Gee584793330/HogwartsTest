f=open('1.txt')
# print(f.readable())
# # print(f.read())
# print(f.readline())
# print(f.readlines())
#
# f.close()
with open('1.txt') as f:
    while 1:
        line= f.readline()
        if line:
            print(line)
        else:
            break

