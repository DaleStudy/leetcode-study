class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    # TC : O(n) where n is the combined length of the string in the list of strings.
    # SC : O(S), where S is the sum of the lengths of all strings in strs
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    # TC : O(n) where n is the length of encoded string
    # SC : O(S), where S is the total length of the decoded strings.
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != ":":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + length + 1])
            i = j + 1 + length

        return res


def test_solution():
    solution = Solution()

    # Test case 1: Basic test case
    input_strs = ["hello", "world"]
    encoded = solution.encode(input_strs)
    decoded = solution.decode(encoded)
    print(f"Test case 1\nEncoded: {encoded}\nDecoded: {decoded}\n")

    # Test case 2: Empty list
    input_strs = []
    encoded = solution.encode(input_strs)
    decoded = solution.decode(encoded)
    print(f"Test case 2\nEncoded: {encoded}\nDecoded: {decoded}\n")

    # Test case 3: List with empty strings
    input_strs = ["", "", ""]
    encoded = solution.encode(input_strs)
    decoded = solution.decode(encoded)
    print(f"Test case 3\nEncoded: {encoded}\nDecoded: {decoded}\n")

    # Test case 4: List with mixed empty and non-empty strings
    input_strs = ["abc", "", "def"]
    encoded = solution.encode(input_strs)
    decoded = solution.decode(encoded)
    print(f"Test case 4\nEncoded: {encoded}\nDecoded: {decoded}\n")

    # Test case 5: List with special characters
    input_strs = ["he:llo", "wo:rld"]
    encoded = solution.encode(input_strs)
    decoded = solution.decode(encoded)
    print(f"Test case 5\nEncoded: {encoded}\nDecoded: {decoded}\n")


test_solution()
