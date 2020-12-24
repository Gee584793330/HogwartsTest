import os
# # os.mkdir("testdir")
# print(os.listdir("./"))
# # os.removedirs("testdir")
# print(os.getcwd())
#

os.path.exists("b")
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/1.TXT"):
    f=open("b/1.TXT","w")
    f.write("test112")
    f.close()

