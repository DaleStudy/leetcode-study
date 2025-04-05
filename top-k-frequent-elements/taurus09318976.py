# 이 문제는 배열에서 가장 자주 등장하는 k개의 요소를 찾는 문제임
# 각 숫자의 1) 등장 횟수를 계산 -> 2) 등장 횟수에 따라 정렬 -> 3) 가장 빈번한 k개의 요소를 반환의 순서로 풀이 해야 함 


class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        #Use Counter if you are using Python3 and you want the number of occurrences for each element:
        count = Counter(nums)
        #most_common 메서드는 Counter 객체에서 요소들의 빈도를 분석하고 정렬할 때 매우 유용 
        #만일 매개변수 k가 없으면 모든 요소를 빈도수 순서대로 반환
        #기본적으로 빈도수가 높은 것부터 낮은 것 순서(내림차순)
        most_common_pairs = count.most_common(k)

        result = []
        for element, frequency in most_common_pairs:
            result.append(element)
        
        return result

        #시간 복잡도 분석
        #Counter(nums): O(n), 여기서 n은 배열의 길이
        #count.most_common(k): 내부적으로 모든 요소를 정렬하므로 O(m log m)이 소요됨. 여기서 m은 고유한 요소의 수(최악의 경우 m = n).
        #결과 리스트 구성: O(k)
        #전체 시간 복잡도: O(n + m log m) ≈ O(n log n) (최악의 경우)
        
        #공간 복잡도 분석
        #Counter 객체: O(m), 여기서 m은 고유한 요소의 수.
        #most_common 결과: O(k)
        #최종 결과 리스트: O(k)
        #전체 공간 복잡도: O(m + k) ≈ O(n) (최악의 경우)

        #다른 방식과의 비교
        #sorted와 딕셔너리 사용 방식:
            #시간 복잡도: O(n log n) - Counter 방식과 동일
            #공간 복잡도: O(n) - Counter 방식과 동일
        #힙(heap) 사용 방식:
            #시간 복잡도: O(n + m log k) ≈ O(n log k) - k가 작을 때 더 효율적
            #공간 복잡도: O(m + k) ≈ O(n)
        #버킷 정렬 방식:
            #시간 복잡도: O(n) - 가장 효율적
            #공간 복잡도: O(n)
        
        #결론
            #most_common 방식은 간결하고 가독성이 좋지만, 시간 복잡도 면에서는 버킷 정렬 방식보다 덜 효율적.
            #대부분의 실제 사례에서는 성능 차이가 미미하고, Python의 내장 함수들이 최적화되어 있어 most_common 방식도 충분히 빠름.
            #극도로 큰 데이터셋이나 성능이 매우 중요한 경우에는 버킷 정렬 방식을 고려할 수 있음.
            #most_common은 코드가 간결하고 직관적이라는 장점이 있음.
            #결론적으로, 작은 규모의 문제나 코드 가독성이 중요한 경우에는 most_common 방식이 좋은 선택이지만, 최고의 성능이 필요한 경우에는 버킷 정렬 방식이 더 효율적.
