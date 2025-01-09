# Big-O 예측
# Time : O(n)
# Space : O(1)
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        new_str = "-!@$@#!_".join(strs)
        return new_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("-!@$@#!_")



strs = ["Hello","World"]
codec = Codec()
codec.decode(codec.encode(strs))

