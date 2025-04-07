from collections import Counter


def top_k_frequent(nums, k):
    # Count the frequency of each number in the input list
    counter = Counter(nums)

    # Find the maximum frequency among all numbers
    max_freq = max(counter.values())

    # Create a list of empty lists (buckets) where index represents frequency
    buckets = [[] for _ in range(max_freq + 1)]

    # Place each number into the bucket corresponding to its frequency
    for num, freq in counter.items():
        buckets[freq].append(num)

    # Initialize an empty list to store the result
    result = []

    # Iterate over the buckets in reverse order (from highest frequency to lowest)
    for freq in range(max_freq, 0, -1):
        # Add all numbers in the current bucket to the result
        result.extend(buckets[freq])

        # If we have collected at least k elements, return the first k elements
        if len(result) >= k:
            return result[:k]
