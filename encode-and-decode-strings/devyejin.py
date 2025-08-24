class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        result = ""
        for s in strs:
            result += str(len(s)) + "@" + s
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        result = []
        i = 0
        while i < len(str):
            j = i
            # 시작점 아닌 경우
            while str[j] != "@":
                j += 1
            # 시작점인 경우
            length = int(str[i:j])
            word = str[j + 1: j + 1 + length]
            result.append(word)
            i = j + 1 + length
        return result
