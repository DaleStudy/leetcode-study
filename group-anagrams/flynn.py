'''
풀이
- 두 단어가 anagram 관계라면 각 단어의 알파벳 수를 계산한 결과가 같을 것입니다
- get_key 함수를 이용해서 단어를 이루는 알파벳 수에 따라 고유한 key를 생성합니다
- key를 관리하는 해시맵인 key_map을 이용하여 현재 바라보고 있는 단어와 anagram인 단어가 있는지 확인합니다

Big O
- N: 배열 strs의 크기
- K: 배열 strs의 원소 중 가장 길이가 긴 문자열의 길이

- Time complexity: O(N * K)
  - 배열 strs를 순회합니다 -> N
  - 각 문자열마다 알파벳의 수를 세기 위해 한 번 순회합니다 -> K

- Space complexity: O(N)
  - 배열 strs의 원소 모두 고유한 key를 지니고 있을 수 있습니다
    이 경우 key_map의 크기는 N에 비례하여 선형적으로 증가할 수 있습니다 -> N
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(s: str) -> str:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            res = ""
            for c in count:
                res += str(c) + ","
            return res

        idx = 0
        key_map = {}
        res = []
        for s in strs:
            key = get_key(s)
            if key not in key_map:
                key_map[key] = idx
                idx += 1
                res.append([])
            res[key_map[key]].append(s)

        return res
