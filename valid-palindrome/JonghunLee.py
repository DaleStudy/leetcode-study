import re


# Time Complexity O(n)
# - Both normal preprocessing and two-pointer comparisons have time complexity proportional to the length of the input string.
# Space Complexity O(n)
# - The space of the new string joined_string preprocessed from the input string is proportional to the length of the input string.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pre-processing using regular expression
        joined_string = re.sub(r"[^a-zA-Z]", "", s.lower())
        str_length = len(joined_string)


        # for loop n/2, two pointer for verify same or not
        for i in range(str_length // 2):
            end = str_length - i - 1
            if not self.check_palindrome(i, end, joined_string):
                return False

        return True

    def check_palindrome(self, i, end, joined_string) -> bool:
        left = joined_string[i]
        right = joined_string[end]

        if left == right:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()

    # test case
    test_string = [
        "A man, a plan, a canal: Panama",  # True (회문)
        "race a car",  # False (회문 아님)
        " ",  # True (빈 문자열도 회문으로 간주)
        "abba",  # True (회문)
        "abcba",  # True (회문)
    ]

    for index, test in enumerate(test_string):
        print(f"start {index} test")
        print(f"input : {test}")
        print(f"Is valid palindrome ? {solution.isPalindrome(test)}\n")
