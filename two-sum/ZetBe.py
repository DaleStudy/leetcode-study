'''
문제: 배열 중에서 두 수를 더해서 타겟 넘버가 되는 인덱스를 반환하라
    한 인덱스를 두번 사용할 수 없으며, 답은 하나만 존재한다.
풀이: 딕셔너리를 이용하여 각 숫자의 인덱스를 저장한 후, 
    타겟 넘버에서 각 숫자를 뺀 값이 딕셔너리에 있는지 확인
    그리고 그 숫자가 두 번 이상 등장하는지 확인
    (절반으로 나누어 떨어지는 경우 고려)

시간복잡도: O(n)
딕셔너리에 각 숫자를 저장하는데 O(n), 겹치지 않은 수를 탐색하는데 최악의 경우 O(n)
각 숫자에 대해 타겟 넘버에서 뺀 값이 딕셔너리에 있는지 확인하는데 O(1)이므로, 전체 시간복잡도는 O(n)

공간복잡도: O(n)
딕셔너리에 각 숫자를 저장하는데 O(n)의 공간이 필요하므로 전체 공간복잡도는 O(n)

사용한 자료구조: 딕셔너리

일반 리스트를 사용하여 탐색할 경우, 시간복잡도가 O(n^2)이 될 수 있다.
최악의 경우, n*(n-1)/2번의 탐색이 필요한데, 이는 결국 O(n^2)이다.
'''

# 추가로 코드리뷰를 통해 가독성 개선한 코드 
'''
for i in range(len(nums)):
    if target - nums[i] in d:
        return [d[target-nums[i]][0], i]
    if nums[i] not in d:
        d[nums[i]] = [i]
            
    else:
        
        d[nums[i]] += [i]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answ = []
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]] += [i]
        print(d)
        for i in d.keys():
            if target-i in d and len(d[target-i]) == 1 and target != i*2:
                answ = [d[target-i][0], d[i][0]]
                return answ
            if target-i in d and len(d[target-i]) >= 2 and target == i*2:
                answ = [d[target-i][0], d[i][1]]
                return answ

