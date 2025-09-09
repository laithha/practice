nums = [1, 3, 2, 3, 4, 1, 3]

def mostFrequent(nums: list[int]) -> int:
    counts = {}
    max_count = 0
    most_freq = None
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > max_count:
            max_count = counts[num]
            most_freq = num
    
    return most_freq

print(mostFrequent(nums)) 
