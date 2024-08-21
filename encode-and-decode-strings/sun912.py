"""
TC: O(n)

"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""
        for str in strs:
            result += str(len(str)) + "#" + str
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        result = []
        idx = 0
        while idx < len(str):
            temp_idx = idx
            while str[temp_idx] != "#":
                temp_idx += 1
            length = int(str[idx:temp_idx])
            result.append(str[temp_idx+1:temp_idx+length+1])
            idx = temp_idx + length + 1
        return result
