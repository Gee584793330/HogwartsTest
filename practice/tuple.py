# # 元组
# # tulp_test1=(1,2,3,4,5)
# # tulp_test2=1,2,3,4
# # print("tulp_test1 is:",tulp_test1)
# # print("tulp_test1 type is ",type(tulp_test1))
# #
# # print("tulp_test2 is:",tulp_test2)
# # print("tulp_test2 type is ",type(tulp_test2))
#
#
# # 元组的不可变特性
# a=(1,2,3,4,5,"a","a")
# print(a.count("a"))
# print(a.index(3))
#
#

"""集合"""

# a={1}
# b=set()
# print(type(a))
# print(type(b))

# a={1,2,3,4,5}
# b={1,3,5}
#
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# 集合会进行去重
# print({i for i in "sajdhsadjshaaaakhjskhdjhuqw"})
#
# c ="dsdsjksjkdjaakskdjk"
# print(set(c))

"""字典"""
dict_test={"a":1,"b":2}
dict_test2=dict(a=1,b=2)
print(dict_test)
print(dict_test2)

print(dict_test.values())
print(dict_test.keys())

print(dict_test.pop("a"))



