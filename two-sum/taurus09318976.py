#이 문제는 결국 value 와 합쳤을 때 target이 되는 보수를 구해야 함 
class Solution:
    def twoSum(self, nums: List[int], target: int):
        array = {}
        
        #enumerate(nums)를 사용하여 배열의 각 요소와 그 인덱스를 동시에 가져옴
        #i는 인덱스, value는 해당 위치의 값
        #Example 1의 경우:
        #i=0, value = 2
        ##i=1, value = 7 
        for i, value in enumerate(nums):
            #diff = 9 - 2 = 7
            ##diff = 9 - 7 = 2 
            diff = target - value
            #diff(7)이 array딕셔너리에 있는지 확인 -> 빈 딕셔너리이므로 없음
            ##diff(2)이 array딕셔너리에 있는지 확인 -> 있음 array[2] = 0
            if diff in array:
                ##return (0, 1) 반환. 루프 종료.
                return (array[diff], i)
            #현재 array = {2:0}
            array[value] = i
        return


    #시간복잡도
        #이 알고리즘은 해시맵(딕셔너리)을 활용하여 배열을 한 번만 순회하므로 O(n) 시간 복잡도로 문제를 해결
        #각 숫자를 처리하면서 현재 숫자와 더해서 target이 되는 값(diff)이 이미 처리된 숫자들 중에 있는지 확인
        #있다면 두 숫자의 인덱스를 반환
        #없다면 현재 숫자와 인덱스를 딕셔너리에 저장하고 다음 숫자로 넘어감
    
    #공간 복잡도 분석:
        #최악의 경우, 배열의 모든 요소를 딕셔너리에 저장해야 함
        #예를 들어, 답이 배열의 마지막 두 요소에 있다면 n-2개의 요소를 딕셔너리에 저장해야 함
        #이는 O(n)의 추가 공간을 필요로 합니다.
        #i, value, diff 등과 같은 변수들은 상수 공간만 차지하므로 이는 O(1)의 공간을 필요로 함
        #따라서 전체 공간 복잡도는 O(n) + O(1) = O(n)입니다.
        #이 알고리즘은 시간 복잡도를 O(n)으로 개선하기 위해 O(n)의 추가 공간(딕셔너리)을 사용하는 시간-공간 트레이드오프의 예임.  
        #O(n²) 시간 복잡도의 브루트 포스 접근법과 비교하면, 시간을 절약하기 위해 약간의 추가 공간을 사용하는 것임.
 
