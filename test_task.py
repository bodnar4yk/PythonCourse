nums=[0,1,1,2,3,4,4]
def removeDuplicates(nums):
    k=0
    for i in range(len(nums)):
        print(i)
        for j in range(i,len(nums)):
            if nums[j-1]==nums[j]:
                k+=1
                print(k)
                print(nums[j-1],nums[j])

removeDuplicates(nums)