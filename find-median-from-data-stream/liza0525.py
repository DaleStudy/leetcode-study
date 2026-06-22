import heapq

# 7기 풀이
class MedianFinder:
    # 공간 복잡도: O(n)
    # - 각각의 힙은 추가되는 수의 개수의 공간을 사용
    def __init__(self):
        self.pre_list = []  # 앞쪽 구간, 최대 힙으로
        self.post_list = []  # 뒤쪽 구간, 최소 힙으로

    # 시간 복잡도: O(log n)
    # - 힙을 사용하여 앞쪽 구간 및 뒤쪽 구간에 새로운 원소를 넣기 때문에, 메소드 호출 때마다 각 배열의 크기에 시간 복잡도가 정해진다.
    # 공간 복잡도: O(1)
    # - 해당 메소드에서는 클래스 멤버 변수 사용하는 것 이외에는 몇 개의 변수만 이용
    def addNum(self, num: int) -> None:
        if not self.pre_list or num < -self.pre_list[0]:
            # 앞쪽 구간에 값을 넣을 경우
            # num이 pre_list의 최댓값보다 작을 때 pre_list에 heappush를 한다.
            # 최대힙 구현을 하기 위해 마이너스 값으로 넣는다.
            heapq.heappush(self.pre_list, -num)
        else:
            # 뒤쪽 구간에 값을 넣을 경우
            # num이 post_list의 최솟값보다 클 때 post_list에 heappush를 한다.
            heapq.heappush(self.post_list, num)

        pre_len, post_len = len(self.pre_list), len(self.post_list)

        # 힙의 크기 차이가 2 이상 날 때는 중간값 조정을 해주기 위해 요소를 다른 쪽으로 옮겨준다.
        if pre_len == post_len + 2:
            # pre_list에 요소가 몰린 경우이므로,
            # pre_list의 최댓값을 pop한 후 post_list의 최솟값으로 push한다.
            heapq.heappush(
                self.post_list,
                -heapq.heappop(self.pre_list)
            )
        elif post_len == pre_len + 2:
            # post_list에 요소가 몰린 경우이므로,
            # post_list의 최솟값을 pop한 후 pre_list의 최댓값으로 push한다.
            heapq.heappush(
                self.pre_list,
                -heapq.heappop(self.post_list)
            )

    # 시간 복잡도: O(1)
    # - 각 힙에서의 최솟값 또는 최대값에 접근하는 정도 + 간단한 중간값 계산
    # 공간 복잡도: O(1)
    # - 해당 메소드에서는 클래스 멤버 변수 사용하는 것 이외에는 몇 개의 변수만 이용
    def findMedian(self) -> float:
        pre_len, post_len = len(self.pre_list), len(self.post_list)
        
        if pre_len > post_len:
            # pre_list의 길이가 더 큰 경우에는 중간값이 pre_list에 있으므로
            # pre_list의 최댓값을 return
            return -self.pre_list[0]
        elif pre_len < post_len:
            # post_list의 길이가 더 큰 경우에는 중간값이 post_list에 있으므로
            # post_list의 최솟값을 return
            return self.post_list[0]
        else:
            # 두 힙의 길이가 같은 경우에는
            # pre_list의 최댓값과 post_list의 최솟값의 평균값을 return
            return (-self.pre_list[0] + self.post_list[0]) / 2
