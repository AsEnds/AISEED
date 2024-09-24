
# Python初级速成课程（3天）

## 课程目标
- 快速掌握Python的基本语法和核心概念
- 熟练使用Jupyter Notebook进行编程和测试
- 能够编写简单的Python程序，包括函数和类

## 课程安排
### 第一天：Python基础与环境搭建
1. 引言与环境搭建
2. Python基础语法

### 第二天：数据结构和控制流程
1. 数据结构
2. 控制流程

### 第三天：函数、模块和面向对象编程
1. 函数
2. 模块与包
3. 文件操作
4. 面向对象编程入门
5. 综合练习

## 课程安排

### 第一天：Python基础与环境搭建

#### 1. 引言与环境搭建

##### 1.1 Python简介
- Python的特点：简洁、易读、跨平台
  - 类比：如果编程语言是交流工具，Python就像是一种简单易懂的国际语言，容易学习，适用范围广。
- 应用领域：Web开发、数据分析、人工智能等
  - 类比：Python就像一把瑞士军刀，可以用于多种不同的任务。

##### 1.2 安装与配置
- 安装Anaconda发行版
  - 类比：Anaconda就像是一个预装了各种工具的工具箱，让你开箱即用。
- 配置并熟悉Jupyter Notebook的使用
  - 类比：Jupyter Notebook就像是一个智能笔记本，可以同时记录笔记和运行代码。

##### 1.3 Jupyter Notebook快速入门
- 创建、运行和保存Notebook
- Markdown与代码单元的使用
  - 类比：Notebook中的单元格就像是乐高积木，可以自由组合文本说明和代码。

#### 2. Python基础语法

##### 2.1 变量和数据类型
```python
# 变量：想象成带标签的盒子，可以存放不同类型的数据
age = 25  # 整数，类比：计数的数字
height = 1.75  # 浮点数，类比：带小数点的测量值
name = "张三"  # 字符串，类比：文本信息
is_student = True  # 布尔值，类比：开关状态（开/关）
empty_value = None  # None类型，类比：空盒子

print(f"年龄: {age}, 类型: {type(age)}")
print(f"身高: {height}, 类型: {type(height)}")
print(f"姓名: {name}, 类型: {type(name)}")
print(f"是否为学生: {is_student}, 类型: {type(is_student)}")
print(f"空值: {empty_value}, 类型: {type(empty_value)}")
```

##### 2.2 基本输入输出
```python
# print()函数的使用
print("Hello, World!")

# input()函数获取用户输入
user_input = input("请输入您的名字：")
print(f"您好，{user_input}!")
```

##### 2.3 运算符与表达式
```python
a, b = 10, 3
print(f"a + b = {a + b}")  # 加法
print(f"a - b = {a - b}")  # 减法
print(f"a * b = {a * b}")  # 乘法
print(f"a / b = {a / b}")  # 除法
print(f"a // b = {a // b}")  # 整除
print(f"a % b = {a % b}")  # 取余
print(f"a ** b = {a ** b}")  # 幂运算

print(f"a == b: {a == b}")  # 等于
print(f"a != b: {a != b}")  # 不等于
print(f"a > b: {a > b}")    # 大于
print(f"a < b: {a < b}")    # 小于

x, y = True, False
print(f"x and y: {x and y}")  # 与
print(f"x or y: {x or y}")    # 或
print(f"not x: {not x}")      # 非
```

### 第二天：数据结构和控制流程

#### 3. 数据结构

##### 3.1 字符串（String）
```python
text = "Hello, Python!"
print(f"原始字符串: {text}")
print(f"大写: {text.upper()}")
print(f"小写: {text.lower()}")
print(f"分割: {text.split(', ')}")
print(f"替换: {text.replace('Python', 'World')}")

# f-strings（Python 3.6+）
name = "李四"
age = 30
print(f"{name}今年{age}岁。")
```

##### 3.2 列表（List）
```python
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")
print(f"水果列表: {fruits}")
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")

fruits.sort()
print(f"排序后: {fruits}")

# 列表切片和遍历
print(f"前两个水果: {fruits[:2]}")
for fruit in fruits:
    print(fruit)
```

##### 3.3 元组（Tuple）
```python
coordinates = (10, 20)
x, y = coordinates  # 元组解包
print(f"x = {x}, y = {y}")
```

##### 3.4 字典（Dictionary）
```python
person = {"name": "王五", "age": 35, "city": "北京"}
print(f"人物信息: {person}")
print(f"姓名: {person['name']}")

print(f"键: {person.keys()}")
print(f"值: {person.values()}")
print(f"键值对: {person.items()}")
```

##### 3.5 集合（Set）
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"并集: {set1 | set2}")
print(f"交集: {set1 & set2}")
print(f"差集: {set1 - set2}")
```

#### 4. 控制流程

##### 4.1 条件判断
```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

##### 4.2 循环语句
```python
# for循环
for i in range(5):
    print(i, end=" ")
print()

# while循环
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# break和continue
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
```

##### 4.3 列表推导式
```python
squares = [x**2 for x in range(10)]
print(f"0到9的平方: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"0到9中偶数的平方: {even_squares}")
```

### 第三天：函数、模块和面向对象编程

#### 5. 函数

##### 5.1 函数的定义与调用
```python
def greet(name):
    return f"你好，{name}!"

print(greet("张三"))
```

##### 5.2 参数类型
```python
def introduce(name, age, city="北京"):
    return f"{name}今年{age}岁，来自{city}。"

print(introduce("李四", 30))  # 位置参数
print(introduce(age=25, name="王五"))  # 关键字参数
print(introduce("赵六", 40, "上海"))  # 使用默认参数
```

##### 5.3 作用域
```python
global_var = "我是全局变量"

def test_scope():
    local_var = "我是局部变量"
    print(local_var)
    print(global_var)

test_scope()
print(global_var)
# print(local_var)  # 这行会报错，因为local_var是局部变量
```

#### 6. 模块与包

##### 6.1 模块的导入
```python
import math
print(f"圆周率: {math.pi}")

from random import randint
print(f"1到10的随机数: {randint(1, 10)}")
```

##### 6.2 自定义模块
创建一个名为`my_module.py`的文件，内容如下：
```python
def say_hello(name):
    return f"Hello, {name}!"

PI = 3.14159
```

使用自定义模块：
```python
import my_module

print(my_module.say_hello("Python"))
print(f"PI值: {my_module.PI}")
```

#### 7. 文件操作

##### 7.1 文件读写基础
```python
# 写入文件
with open("example.txt", "w") as file:
    file.write("这是第一行。\n")
    file.write("这是第二行。\n")

# 读取文件
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

##### 7.2 上下文管理
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

#### 8. 面向对象编程入门

##### 8.1 类和对象
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁。"

student1 = Student("张三", 20)
print(student1.introduce())
```

##### 8.2 类的属性和方法
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(f"矩形面积: {rect.area()}")
print(f"矩形周长: {rect.perimeter()}")
```

#### 9. 综合练习

##### 9.1 项目实践：简单通讯录程序
```python
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}: 电话 {self.phone}, 邮箱 {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"已添加联系人: {contact.name}")

    def display_contacts(self):
        if not self.contacts:
            print("通讯录为空")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

# 主程序
address_book = AddressBook()

while True:
    print("\n1. 添加联系人")
    print("2. 显示所有联系人")
    print("3. 搜索联系人")
    print("4. 退出")
    
    choice = input("请选择操作 (1-4): ")
    
    if choice == '1':
        name = input("请输入姓名: ")
        phone = input("请输入电话: ")
        email = input("请输入邮箱: ")
        contact = Contact(name, phone, email)
        address_book.add_contact(contact)
    elif choice == '2':
        address_book.display_contacts()
    elif choice == '3':
        name = input("请输入要搜索的姓名: ")
        contact = address_book.search_contact(name)
        if contact:
            print(contact)
        else:
            print("未找到该联系人")
    elif choice == '4':
        print("感谢使用，再见!")
        break
    else:
        print("无效选择，请重新输入")
```

##### 9.2 课程总结
- 回顾重点内容
- 答疑解惑
- 指导学生独立完成练习

## 结语

这个Python初级速成课程涵盖了Python编程的基础知识，从基本语法到面向对象编程的入门。通过这三天的学习，您应该能够理解Python的核心概念并开始编写简单的程序。

为了进一步提高您的Python技能，建议：
1. 继续练习和编写更多的Python程序
2. 阅读Python官方文档和其他高质量的学习资源
3. 参与开源项目或解决实际问题
4. 探索更高级的主题，如数据分析、Web开发或机器学习

记住，编程技能的提升需要时间和实践。保持耐心，持续学习，您一定会在Python编程的道路上取得进步。

祝您的Python学习之旅愉快且富有成效！
