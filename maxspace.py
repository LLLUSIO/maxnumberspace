import random

n = int(input("请输入个数"))

list_n = []
#重复执行n次
for i in range(n):
    #生成随机数
    num = random.randint(1,1000)
    list_n.append(num)
print("需要找最大值的列表是: ",list_n)

#默认存列表中的第一个数
maxs = list_n[0]
for  i in range(len(list_n)):
    #如果列表中有数字比maxs中的还大，则更新
    if list_n[i] > maxs:
        maxs = list_n[i]

# 新建一个列表用来存下标
list_maxs = []
for i in range(len(list_n)):
    # 找到最大数字后，将下标加入列表中
    if list_n[i] == maxs:
        list_maxs.append(i)

print("最大数字的下标在: ", list_maxs)
