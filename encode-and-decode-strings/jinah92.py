# O(N) times, O(1) spaces
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded_str = ""
        for str in strs:
            encoded_str += f"{len(str)}:{str}"
        return encoded_str

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        list_strs, start = [], 0
        while start < len(str):
            offset = str.find(":", start)
            s_length = int(str[start:offset])
            list_strs.append(str[offset+1:offset+1+s_length])
            start = offset+1+s_length
        return list_strs
