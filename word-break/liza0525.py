# 7기 풀이
# 시간 복잡도: 시간복잡도: O(n * m)
# - n은 s의 길이, m은 wordDict의 평균 단어 길이
# - 각 인덱스마다 wordDict를 순회하므로
# 공간 복잡도: 공간복잡도: O(n)
# - memo에 최대 n개의 인덱스를 저장
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = set()

        def dfs(i):
            if i == len(s):
                # i가 s의 길이가 되면 모든 탐색이 성공으로 끝났기 때문에
                # True로 반환
                return True

            memo.add(i)  # 해당 인덱스에 대해서는 방문을 했기 때문에 memo
            for word in wordDict:
                if i + len(word) in memo:
                    # i + len(word)가 memoization해둔 인덱스라면 이미 성공한 케이스므로 통과
                    continue

                if i + len(word) > len(s):
                    # i + len(word)가 len(s)보다 크면 탐색을 더이상 할 수 없으므로 continue
                    continue

                # 아직 방문을 하지 않은 index라면 단어를 slice하여 실제로 wordDict에 있는지 확인 
                if s[i:i + len(word)] in wordDict:
                    # 다음 인덱스 i + len(word)로 dfs 탐색
                    check = dfs(i + len(word))
                    if check:
                        # 모든게 성공되었을 땐 True 반환
                        return True

            return False

        return dfs(0)
