class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        first_letter_dict = {}
        for word in wordDict:
            first_letter_dict.setdefault(word[0], []).append(word)

        last_letter_dict = {}
        for word in wordDict:
            last_letter_dict.setdefault(word[-1], []).append(word)

        for word in wordDict:
            isSuccess = True
            for small_s in s.split(word):
                if small_s == "":
                    continue
                if not self.dfs(small_s, 0, first_letter_dict, last_letter_dict):
                    isSuccess = False

            if isSuccess:
                return True

        return False

    def dfs(self, s: str, i, first_letter_dict, last_letter_dict):
        if i == len(s):
            return True

        if s[i] not in first_letter_dict or s[-1] not in last_letter_dict:
            return False

        for word in first_letter_dict[s[i]]:
            if not s[i:].startswith(word):
                continue

            if self.dfs(s, i + len(word), first_letter_dict, last_letter_dict):
                return True

        return False
