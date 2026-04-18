class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = ""

        delimiter = ":;"

        for i, str in enumerate(strs):
            result = result + str
            if i != len(strs):
                result = result + delimiter
        
        print(result)

        return result
            
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        result = []

        i = 0 
        delimiter = ":;"

        while i < len(str):

            j = i
            while j < len(str) - 1:
                if str[j:j+2] == delimiter:
                    result.append(str[i:j])
                    break
                else:
                    j = j + 1

            i = j + 2
        
        return result
