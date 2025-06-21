class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 시간복잡도 O(n log n), 공간복잡도 O(n)
        
        intervals.sort()   # 정렬
        answer = []

        for i in intervals:
            
            # answer가 비어있거나 answer의 맨 뒤 값이 i의 첫 번째 값보다 작을 경우(겹치지않는경우) answer에 i추가
            if not answer or answer[-1][1] < i[0]:
                answer.append(i)

            # 값이 겹치는 경우 합치기(더 큰 값으로 업데이트)
            else:
                answer[-1][1] = max(answer[-1][1],i[1])

        return answer
