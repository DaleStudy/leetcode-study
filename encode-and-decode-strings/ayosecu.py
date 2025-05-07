class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    - Time Complexity: O(N), N = All characters in strs
    - Space Complexity: O(N)
    """
    def encode(self, strs):
        # Encode Format: xx#str
        # xx:len(s)
        # strs = ["abc", "defg"]
        # Encoded String = 3#abc4#defg
        enc_list = []
        for s in strs:
            enc_list.append(f"{len(s)}#{s}")
        return "".join(enc_list)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    - Time Complexity: O(n), n = len(str)
    - Space Complexity: O(1), if output is excluded.
    """
    def decode(self, str):
        result = []

        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            n = int(str[i:j])
            i = j + 1
            result.append(str[i:i + n])
            i += n

        return result
    
tc = [
        (["lint","code","love","you"], "4#lint4#code4#love3#you"),
        (["we", "say", ":", "yes"], "2#we3#say1#:3#yes")
]

for i, (p1, p2) in enumerate(tc, 1):
    sol = Solution()
    r = sol.encode(p1)
    print(f"TC {i} - encode() is Passed!" if r == p2 else f"TC {i} - encode() is Failed! - Expected:{p2}, Result: {r}")
    r = sol.decode(p2)
    print(f"TC {i} - decode() is Passed!" if r == p1 else f"TC {i} - decode() is Failed! - Expected:{p1}, Result: {r}")
