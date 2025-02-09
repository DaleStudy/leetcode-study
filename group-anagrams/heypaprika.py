# Big-O 예측
# Time : O(k * nlog(n)) (k : strs 배열 수, n : strs 원소의 unique 단어 개수)
# Space : O(k + n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = {}
        num = 0
        dicted_list = []
        for s in strs:
            cur = str(sorted(Counter(s).items()))
            dicted_list.append(cur)
            if cur in count_dict:
                continue
            count_dict[cur] = num
            num += 1
        
        ans_list = [[] for _ in range(len(count_dict))]
        for k, v in count_dict.items():
            for i, dicted in enumerate(dicted_list):
                if dicted == k:
                    ans_list[v].append(strs[i])
        return ans_list

