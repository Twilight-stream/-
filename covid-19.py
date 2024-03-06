from datetime import datetime
from datetime import timedelta

date = input("请输入今天的日期：")
num = int(input("请问你要查询几个人："))
lis = []
ans = []

while num>0 :
    count = input("请输入已经接种了几针：")
    if count == 0:
        print("请在今天之内接种")
        lis.append({count:date})
    else :
        latest = input("请输入最近一次的接种日期：")
        lis.append({count:latest})
    num -= 1

cur = datetime.strptime(date, "%Y-%m-%d")
for item in lis:
    for key in item:
        if int(key) == 1:
            fur = datetime.strptime(item[key], "%Y-%m-%d")+timedelta(days=30)
            if cur >= fur:
                ans.append({True: fur.strftime('%Y-%m-%d')})
            else:
                ans.append({False: fur.strftime('%Y-%m-%d')})
        if int(key) == 2:
            fur = datetime.strptime(item[key], "%Y-%m-%d")+timedelta(days=180)
            if cur >= fur:
                ans.append({True: fur.strftime('%Y-%m-%d')})
            else:
                ans.append({False: fur.strftime('%Y-%m-%d')})
        if int(key) == 0:
            ans.append({True:date})
        if int(key) >= 3:
            print("已完成所有接种")
print(ans)









