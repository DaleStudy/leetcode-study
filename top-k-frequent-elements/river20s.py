class Solution(object):
    def topKFrequent(self, nums, k):
        """
        주어진 정수 리스트에서 각 숫자의 등장 빈도를 계산한 후,
        빈도수가 높은 순서대로 상위 k개의 숫자를 반환합니다.
        
        :param nums: 정수로 이루어진 리스트
        :param k: 반환할 상위 빈도 숫자의 개수
        :return: 빈도수가 높은 순서대로 정렬된 상위 k개 숫자의 리스트
        """
        freq = {} # 각 숫자 등장 횟수를 저장하는 딕셔너리 
        # 리스트의 각 숫자 등장 횟수를 누적 저장
        for num in nums:
            # num이 freq에 있다면 기존 값에 1을 더하고, 없으면 0에서 1을 더함
            freq[num] = freq.get(num, 0) + 1
        
        # freq의 키들을 등장 횟수 기준 내림차순 정렬
        sorted_list = sorted(freq, key=freq.get, reverse=True)
        # 정렬된 리스트에서 top-k개 숫자를 반환
        return sorted_list[:k]
