def maxZeros(nums):
    zero=[]
    count=0
    for i in range(0,len(nums)):
        if nums[i]==0:
            count+=1
            if i == len(nums)-1:
                zero.append(count)
        else:
            zero.append(count)
            count=0
    print(max(zero))
    
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([1, 1, 0, 0, 0 ,1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])# 得到 14