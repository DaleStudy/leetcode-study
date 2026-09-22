class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            encoded += f"{len(s):03d}{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        decoded = []
        i = 0
        while i < len(s):
            s_start_idx = i + 3
            s_len = int(s[i:s_start_idx])
            decoded.append(s[s_start_idx:s_start_idx + s_len])

            i = s_start_idx + s_len

        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
