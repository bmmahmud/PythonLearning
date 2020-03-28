##### Remove Duplicates from Array
## 3.1
# def remove_duplicates(nums):
#     unique_nums = []
#     unique_nums.append(nums[0])

#     n = len(nums)
#     for i in range(1,n):
#         if nums[i] != nums[i-1]:
#             unique_nums.append(nums)
#     return len(unique_nums)

## 3.2
def remove_duplicates(nums):
    unique_nums = (set(nums))
    return unique_nums

nums = [6,6,6,6,2,3,4,5,5]
print(remove_duplicates(nums))

