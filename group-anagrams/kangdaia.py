class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        단어 목록에서 애너그램끼리 그룹화해서, 그룹화된 단어 목록을 반환하는 함수.

        N은 단어의 개수, M은 단어의 최대 길이로 가정할 때,
        시간 복잡도: O(N * M log M)
        공간 복잡도: O(N * M)

        Args:
            strs (list[str]): 단어 목록

        Returns:
            list[list[str]]: 애너그램 그룹화된 단어 목록
        """
        seen = dict()
        for st in strs:
            st_key = "".join(sorted(st))
            if st_key in seen:
                seen[st_key].append(st)
            else:
                seen[st_key] = [st]
        return list(seen.values())
