# 通过class 进行类的定义

class Person:
    # 类变量
    name = "default"
    age = 0
    gender = 'male'
    weight = 0
    # 构造方法，在类实例化时候被调用
    def __init__(self,name,age,gender,weight):
        # self.变量名访问到的是
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight

    # def set_param(self,name):
    #     self.name=name
    #
    # def set_age(self,age):
    #     self.age=age

    def eat(self):
        print("eating")

    def play(self):
        print("Playing")

    def jump(self):
        print("Jumping")

# 类方法和实例方法的使用



# zs = Person('张三',20,'男',213)
#
#
# print(f"名字是：{zs.name},年龄是：{zs.age},性别是:{zs.gender},体重是:{zs.weight}")
#
# ls=Person('李四',12,'女',100)
# print(f"名字是：{ls.name},年龄是：{ls.age},性别是:{ls.gender},体重是:{ls.weight}")
