class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            encoded_strs += str(len(s))
            encoded_strs += "#"
            for char in s:
                encoded_strs += char
        return encoded_strs
                
    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_strs = []

        idx = 0
        while idx < len(s):
            end = idx + 1
            while s[end] != "#":
                end += 1
            length = s[idx:end]
            idx = end
            decoded_str = ""
            for i in range(int(length)):
                idx += 1
                decoded_str += s[idx]
            idx += 1
            decoded_strs.append(decoded_str)
        return decoded_strs


