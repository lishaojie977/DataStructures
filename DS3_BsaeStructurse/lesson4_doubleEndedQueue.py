'''
    栈：后进先出（顶部进底部出）
    队列：先进先出（队尾进，対首出）

    双端队列(Deque)：一系列元素的有序集合，其两端成为対首(front)和队尾(rear)，元素在到达两端之前始终位于双端队列中
    与队列不同的地方在于：双端队列对元素的添加和删除限制不那么严格，元素可以从两端插入，也可以从两端删除
    总结来说：双端队列拥有栈和队列各自拥有的所有功能

    抽象数据类型(ADT)
        Deque() 创建一个空双端队列，无参数，返回值为Deque对象
        addFront(item)  在対首插入一个元素，参数为待插入元素，无返回值
        addRear(item)   在対尾插入一个元素，参数为待插入元素，无返回值
        removeFront()   在対首移出一个元素，无参数，返回改移出的元素，双端队列会被改变
        removeRear()    在队尾移出一个元素，无参数，返回改移出的元素，双端队列会被改变
        isEmpty()       判断双端队列是否为空，无参数，返回布尔值
        size()          返回双端队列中数据项的个数，无参数，返回值为整型数值

    Python3实现ADT:

'''
# class Deque:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)
#     def addFront(self,item):
#         self.items.append(item)
#     def addRear(self,item):
#         self.items.insert(0,item)
#     def removeFront(self):
#         return self.items.pop()
#     def removeRear(self):
#         return self.items.pop(0)


# d = Deque()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addRear('cat')
# d.addRear(True)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.removeRear())
# print(d.removeFront())








from pythonds.basic.deque import Deque

def palChecker(aString):
    charDeque = Deque()
    for ch in aString:
        charDeque.addFront(ch)
    # print(charDeque.size())

    stillEqual = True
    while charDeque.size() > 1 and stillEqual:
        first_ch = charDeque.removeFront()
        last_ch = charDeque.removeRear()

        if first_ch != last_ch:
            stillEqual = False

    return stillEqual

print(palChecker('madam'))
print(palChecker('lalalalal'))
print(palChecker('hot'))





