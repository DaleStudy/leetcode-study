class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev, curr = 1, 1

        for i in range(1, len(s)):
            temp = curr

            if s[i] == "0":
                if s[i - 1] in ("1", "2"):
                    curr = prev
                else:
                    return 0
            else:
                two_num = int(s[i - 1] + s[i])
                is_two_num_decoded = 10 <= two_num <= 26
                if is_two_num_decoded:
                    curr += prev
            
            prev = temp

        return curr


# Time Complexity: O(n)
# - The loop iterates through the string once, where n is the length of the string.

# Space Complexity: O(1)
# - Only two variables (prev and curr) are used, independent of the input size.
