#이 문제는 1)현재 합이 target과 같으면 결과에 추가 후 되돌아감, 2) 현재 합이 target을 초과하면 더 이상 진행하지 않고 되돌아감, 
#3) 각 candidate에 대해 recursive하게 시도

class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        #결과를 저장할 리스트
        result = []
        
        #start: 현재 선택할 수 있는 candidate의 시작 인덱스
        #current: 현재까지 선택한 숫자들의 리스트
        #current_sum: 현재까지 선택한 숫자들의 합
        def backtrack(start, current, current_sum):
            #현재 합이 target과 같으면 현재 조합을 결과에 추가 후 되돌아감
            if current_sum == target:
                result.append(current.copy()) 
                return
            #현재 합이 target을 초과하면 더 이상 진행하지 않고 되돌아감
            if current_sum > target:
                return
            
            #start 파라미터를 사용하여 중복 조합이 생기지 않도록 이전에 선택한 숫자부터 다시 시작
            for i in range(start, len(candidates)):
                #현재 candidate 선택
                current.append(candidates[i])
                #recursive 호출 : i를 그대로 전달하여 같은 숫자를 무한반복하여 사용할 수 있음. 
                backtrack(i, current, current_sum + candidates[i])
                #마지막에 선택한 숫자 제거
                current.pop()
        
        #백트래킹 시작
        backtrack(0, [], 0)
        #모든 가능한 조합 반환
        return result


# 테스트 케이스
solution = Solution()

# 테스트 1
test1_candidates = [2,3,6,7]
test1_target = 7
print(f"Expected: [[2,2,3],[7]]")
print(f"Result: {solution.combinationSum(test1_candidates, test1_target)}")

# 테스트 2
test2_candidates = [2,3,5]
test2_target = 8
print(f"Expected: [[2,2,2,2],[2,3,3],[3,5]]")
print(f"Result: {solution.combinationSum(test2_candidates, test2_target)}")

# 테스트 3
test3_candidates = [2]
test3_target = 
print(f"Expected: []")
print(f"Result: {solution.combinationSum(test3_candidates, test3_target)}") 


#시간 복잡도: O(2^target)
    #각 단계에서 숫자를 선택하거나 선택하지 않는 두 가지 선택지가 있음
    #최악의 경우, target을 만들기 위해 모든 가능한 조합을 시도해야 함.
    #예를 들어 candidates = [1], target = 10일 때:
    #[1,1,1,1,1,1,1,1,1,1]까지 시도해야 함
    #이는 2^10에 가까운 경우의 수가 발생
#공간 복잡도: O(target)
    #각 재귀 호출마다 새로운 스택 프레임이 생성됨
    #최대 깊이는 target을 가장 작은 숫자로 나눈 값임
    #예를 들어 target = 7, 리스트 내 가장 작은 숫자 = 2일 때
    #7/2 = 3.5 → 최대 3번의 재귀 호출
    #[2,2,3]을 만들 때 3번의 재귀 호출
    #공간 복잡도는 target 값에 비례하여 증가하므로 O(target)임
    #이는 target이 커질수록 더 많은 메모리가 필요하다는 것을 의미함
