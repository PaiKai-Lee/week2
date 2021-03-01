#在函式中 使用迴圈 計算最小值到最大值之間，所有整數的總和。
def caculate(min,max):
    sum=0
    for i in range(min,max+1) :
       sum+=i
    print(sum)

def avg(data):
    sum=0
    num=len(data["employees"])
    for i in data["employees"]:
        sum+=i["salary"]
    print(sum/num)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
})




    
