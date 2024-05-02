# 문제: https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums) -> bool:
    done = set()
    for num in nums:
        if num in done:
            return True
        done.add(num)
    return False


# 시간복잡도: O(n)
# 공간복잡도: O(n)

print((containsDuplicate([1, 2, 3, 1]) is True))
print((containsDuplicate([1, 2, 3, 4]) is False))
print((containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True))
