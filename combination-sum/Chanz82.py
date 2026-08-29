class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        combination = []
        def find_target(start, combination, target):

            if target == 0 : # 조합 생성 완료.
                result.append(combination.copy()) # pop 때문에 복사해서 append해야 함.
                return
            
            elif target < 0 or start >= len(candidates):
                return

            combination.append(candidates[start])
            find_target(start, combination, target-candidates[start]) # 현재 원소를 더 뽑는 경우
            combination.pop() # 현재 원소는 다시 조합에서 제거 후, 다음 원소를 뽑음
            find_target(start+1, combination, target) # 다음 원소를 뽑는 경우

        find_target(0, combination, target)

        return result
