#在函式中 使用迴圈 計算最小值到最大值之間，所有整數的總和。
def calculate(min,max):
    sum=0
    for i in range(min,max+1) :
        sum+=i
    print(sum)
print("要求一:")
calculate(1, 3)
calculate(4, 8)

def avg(data):
    sum=0
    num=len(data["employees"])
    for i in data["employees"]:
        sum+=i["salary"]
    print(sum/num)

print("\n要求二:")
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

#找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
#兩兩相乘(不重複相乘)後放入列表中,使用max函式將最大值取出
def maxProduct(nums):
    num=[]
    for i in range(0,len(nums)-1):#提取每個元素(被乘數),倒數第二個元素已與最後一個元素相乘,故在此不再提取
        for j in range(i+1,len(nums)): #提取被乘數後的元素值(乘數)
            num.append(nums[i]*nums[j])#相乘後放入列表中
    print(max(num))#提取列表中最大值    

print("\n要求三:")
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])

def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if target==nums[i]+nums[j]:
                return[i,j]
print("\n要求四:")
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
