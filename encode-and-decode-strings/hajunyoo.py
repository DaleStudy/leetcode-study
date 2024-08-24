class Solution1:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # time complexity: O(n)
    # space complexity: O(1)
    def encode(self, strs):
        return ":;".join(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    # time complexity: O(n)
    # space complexity: O(1)
    def decode(self, str):
        return str.split(":;")