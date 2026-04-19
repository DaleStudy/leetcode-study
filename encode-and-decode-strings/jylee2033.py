class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        # Encode each word with its length prefix and a "#"
        # ["C#", "&"] -> "2#C#1#&"
        encoded_str = ""
        
        for word in strs:
            encoded_str += f"{len(word)}#{word}"

        return encoded_str
        
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        # "2#C#1#&" -> ["C#", "&"]
        decoded_lst = []
        char_count = 0
        reading_word = False
        word = ""
        length_str = ""

        if str == "":
            return [""]

        for ch in str:
            if ch == "#" and not reading_word:
                # Finished reading the length prefix
                # Switch to word-reading mode
                char_count = int(length_str)
                length_str = ""
                reading_word = True

            elif not reading_word:
                # Accumulate digits for the length prefix
                length_str += ch

            else:
                # reading_word is True
                word += ch
                char_count -= 1

                if char_count == 0:
                    reading_word = False
                    decoded_lst.append(word)
                    word = ""

        return decoded_lst

# Time Complexity: O(N)
# Space Complexity: O(N)
