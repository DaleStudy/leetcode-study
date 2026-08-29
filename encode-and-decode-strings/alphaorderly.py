"""
Time Complexity: O(n)
Space Complexity: O(n)

### Wrong Approach ( NEVER USE IT )
- Uses eval() on potentially untrusted input, which is a major security risk.
- If s or strs can be controlled or modified externally, arbitrary code execution is possible.
- This is for illustration only; never use eval for decoding in production code.

- Encodes by converting the list of strings to its string representation using str().
- Decodes by evaluating that string with eval(), reconstructing the original list.
"""
class Codec:
    def encode(self, strs: List[str]) -> str:
        return str(strs)

    def decode(self, s: str) -> List[str]:
        return eval(s)

"""
Time Complexity: O(n)
Space Complexity: O(n)

- Encodes the list of strings by prefixing each string with its length and a separator ("_"), then concatenating.
- Decodes by parsing each length, extracting the separated string accordingly.
- Does not use eval, so this approach is safe.
"""
class Codec:
    def encode(self, strs: List[str]) -> str:
        strs = [str(len(s)) + "_" + s for s in strs]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        N = len(s)
        index = 0
        size = 0

        word_part = False

        while index < N:
            ch = s[index]
            if not word_part:
                if ch == "_":
                    if size == 0:
                        ans.append("")
                    else:
                        word_part = True
                else:
                    size = (size * 10) + int(ch)
                index += 1
            else:
                ans.append(s[index : index + size])
                index += size
                size = 0
                word_part = False

        return ans
