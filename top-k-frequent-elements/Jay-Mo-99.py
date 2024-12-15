        #해석
        #nums를 dictionary로 전환한다. nums의 기존 element가 key, element의 갯수를 value값으로 지정한다.
        #value값이 큰 순서대로 dictionary의 요소를 정렬한다
        #그중 0에서 k-1까지의 key값만을 반환한다. 

        #Big O
        #N: 주어진 list의 길이 nums (Length of the input list nums)
        #M: count 딕셔너리의 고유한 key 의 갯수 

        #Time Complexity: O(NLogN)
        #- count: N의 길이에 기반하여 생성된다 : O(N)
        #- sorted_count: 파이썬의 sorted 메소드는 Timesort 알고리즘 기반의 비교 기반 정렬 알고리즘 
        #                리스트의 길이가 M이면 sorted()는 요소들을 쪼개고 병합하여 정렬한다. 대략 M개의 요소를 logM번 비교 

        #Space Complexity: O(N)
        #- count: M개에 기반하여 Dictionary 공간 저장: O(M)
        #- sorted_count: count.items의 갯수에 기반하여 공간 저장 : O(M)
        #- dic_count: 상위 요소 갯수(k개) 만큼 저장 : O(k)
        #- 최종: O(N) + O(M) + O(k): k는 최대 M개 만큼 가능하고 M은 최대 N개만큼 가능하다. 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #Create dictionary which have a key(element of nums) and value(count num of the element)
        count = {}
        for i in nums:
            try: count[i] += 1
            except: count[i] = 1
        
        #Sort depends on the value descending order
        sorted_count = sorted(count.items(),key=lambda x:x[1],reverse=True)
        #k까지의 요소만을 dictionary data type으로 convert 
        dic_count = dict(sorted_count[:k])
        #Return keys 
        return dic_count.keys()



