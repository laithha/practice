nums = [2, 4, 3, 5, 1, 6]
target = 7



for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"({nums[i]}, {nums[j]})")