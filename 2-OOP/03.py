class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名: %s 年龄：%s' % (self.name, self.age)  ###注意此处，return返回值返回什么字符串，打印对象的时候就显示什么字符串


def main():
    zhangsan = Person('张三', 19)
    print(zhangsan)


main()