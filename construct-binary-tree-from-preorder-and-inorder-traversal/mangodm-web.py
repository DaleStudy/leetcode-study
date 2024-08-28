from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []

        for s in strs:
            encoded.append(s.replace("/", "//") + "/:")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        current_string = ""
        i = 0

        while i < len(s):
            if s[i : i + 2] == "/:":
                decoded.append(current_string)
                current_string = ""
                i += 2
            elif s[i : i + 2] == "//":
                current_string += "/"
                i += 2
            else:
                current_string += s[i]
                i += 1

        return decoded
