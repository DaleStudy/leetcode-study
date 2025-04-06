def topKFrequent(nums, k):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_frequency = sorted(frequency, key=lambda num: frequency[num])
    return sorted_frequency[-k:]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
