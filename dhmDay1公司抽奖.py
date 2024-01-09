import random     #引入random库
member = list()    #member列表用于存放员工号信息
reward = ["三斤苹果", "iphone14手机", "泰国5日游+手术费报销"]     #reward用于有序存放一二三等奖奖品信息
rewardnember = [30, 6, 3]           #设置每次抽奖数量
k = list()
for i in range(1, 301):                      #循环加入300个员工的员工号信息
    member.append(i)
for i in range(0, 3):            #设置循环进行三次抽奖
    k = random.sample(member, rewardnember[i])   #假设300个员工的编号为1到300，从1到300随机一个员工号作为中奖人
    member = [x for x in member if x not in k]            #移除已获奖员工信息避免重复获奖
    print(f"第{i+1}次抽奖：恭喜员工号为{k}的{rewardnember[i]}位员工中{3-i}等奖:{reward[i]}")         #打印显示谁中几等奖，其中第一次三等奖所以与抽奖次数倒序，所以3 -i

