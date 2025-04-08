def longestConsecutive(nums):
    longest = 0

    for num in nums:
        length = 1
        while num + length in nums:
            length += 1
        longest = max(longest, length)

    return longest
