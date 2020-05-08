'''
    队列：是一系列有序的元素的集合，心元素加入在队列的一端，这一端叫做"队尾(rear)"
            已有元素的移除发生在队列的另一端，叫做"対首(front)"，当一个元素被加入到队列之后，
            它就从尾部向対首前进，知道它成为下一个即将被移出队列的元素
    先进先出(FIFO):最新被加入的元素处于队尾，在队列中停留最长时间的元素处于対首
    --------------------
rear                    front
    --------------------

    抽象数据类型(ADT)：
        Queue() 创建一个空队列对象，无需参数，返回空的队列
        enqueue(item) 将数据项添加到队尾，无返回值
        dequeue() 从対首移出数据项，无需参数，返回值为対首数据项
        isEmpty() 是否队列为空，无需参数，返回值为布尔值
        size() 返回队列中的数据项的个数，无需参数

    通python list 实现队列

'''

# class Queue():
#     def __init__(self):
#         self.items = []
#     def enqueue(self,item):
#         self.items.insert(0,item)
#     def dequeue(self):
#         return self.items.pop()
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)
#
# q = Queue()
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print(q.size())
# print(q.isEmpty())
# print(q.dequeue())

'''
    马铃薯游戏
'''
from pythonds.basic.queue import Queue

# name_list = ['红','明','额','丽','马','王','李','赵','啦','啊','哦']
# num = 7
# def send_flower(name_list,num):
#     q = Queue()
#     for name in name_list:
#         q.enqueue(name)
#     while q.size() > 1:
#         for i in range(num):
#             q.enqueue(q.dequeue())
#         n = q.dequeue()
#         print(n)
#     return q.dequeue()
#
# print(send_flower(name_list,num))

'''
    模拟打印机
    平均每天任意一个小时有大约 10 个学生在实验室里,在这
    一小时中通常每人发起 2 次打印任务,每个打印任务的页数从 1 到 20 页不等。实验室中的打印机比较
    老旧，如果以草稿模式打印，每分钟可以打印 10 页；打印机可以转换成较高品质的打印模式，但每
    分钟只能打印 5 页。较慢的打印速度可能会使学生等待太长时间。应该采取哪种打印模式?
    
    学生对象 （等待时间 + 打印时间）
    打印任务（打印任务队列）
    打印机  （状态：打印中，空闲）
    
    1-20不等，随机数模拟
    
    总共10*2 = 20次打印任务，平均每三分钟产生一个打印任务
    在3分钟内的任意一秒钟产生一个打印任务的概率是：task/180，
    随机数模拟，如果产生的随机数是180，就可以认为生成了一个任务
    
    过程：
        1、创建一个打印任务队列，每个任务在生成是被赋予一个“时间戳”
        2、一个小时中的每一秒都需要判断
            是否有新的打印任务生成，如果有，把它加入打印机队列：
            如果打印机空闲并且队列不为空：
            1、从队列中拿出一个任务交给打印机
            2、从加入打印机时间 - 加入队列时间 = 等待时间
            3、将该任务的等待市价加入到一个列表中，方便后续时间，计算总的学生打印花费时间
            4、基于打印的也输的随机数，求出需要多长时间打印
        3、打印机工作中，对于打印机而言，就是工作了一秒，对于打印任务而言：它离打印结束又近了一秒
        4、打印任务完成，剩余时间为0，打印机进入空闲状态

'''











