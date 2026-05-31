class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = ""
        for word in strs:
            word_size = len(word)
            result += str(word_size) + "#" + word

        return result
    # input ["lint","code","love","you"]
    # output "4#lint4#code4#love3#you"

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
            while str[j] != "#": #find the position of '#'
                j += 1

            my_number = int(str[i:j])

            start = j + 1 # add 1 to skip '#'
            end = j + 1 + my_number

            result.append(str[start:end])
            i = end

        return result
    # input "4#lint4#code4#love3#you"
    # output ["lint","code","love","you"]
