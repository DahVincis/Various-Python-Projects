#####################  Two Sum  ###########################

nums = [2,7,11,15]

for x in nums:
    for y in range(nums[1]):
        if x + y == 9:
            print (nums.index(x),nums.index(y))