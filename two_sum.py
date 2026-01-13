# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:


nums=[3,0,3,3]
#nums=[3,2,4]
target=6

# def twoSum(nums,target):
#     for i in range(0,len(nums), 1):
#         c=nums.copy()
#         c.remove(nums[i])
#         for n in range(0,len(c), 1): 
#             if nums[i]+c[n]==target and i<=n:
#                 print(nums[i], c[n])
#                 index_value=[i, n+1]
#                 index_value.sort()
#     return index_value

# #print(nums.index(3))
# print(twoSum(nums,target))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums), 1):
            c=nums.copy()
            c.remove(nums[i])
            for n in range(0,len(c), 1):
                if nums[i]+c[n]==target:
                    print(nums[i], c[n])
                    index_value=[i, n+1]
                    index_value.sort()
                    return index_value

def twoSum(nums,target):
    pair_index={}
    for index,element in enumerate(nums):
        c=target-element
        if c in pair_index.keys():
            print(index,pair_index[c])
            return [index,pair_index[c]]
        else:
            pair_index[element]=index
            print("not exist")


# a={1:0,"dd":5}
# print(a.keys())
twoSum(nums,target)