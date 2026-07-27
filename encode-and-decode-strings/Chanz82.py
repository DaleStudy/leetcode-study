class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for plain_string in strs:
            encoded_string = encoded_string + str(len(plain_string)) + ";" + plain_string

        #print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_str_list = []
        idx = 0
        while idx < len(s):
            idx_del = s.index(";", idx)
            #print(s[idx:idx_del])
            size = int(s[idx:idx_del])
            start_idx = idx_del+1
            decoded_str_list.append(s[start_idx:start_idx+size])
            idx = start_idx + size
        return decoded_str_list
