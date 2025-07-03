/*
	정렬에 O(nlogn), 힙 삽입 및 삭제에 O(logn) 소요되므로 전체 시간 복잡도는 O(nlogn)
	최대 n개의 회의가 있을 수 있으므로 공간 복잡도는 O(n)
*/
class Solution {
public:
    int minMeetingRooms(vector<Interval> &intervals) {
        if (intervals.empty())
            return 0;

        sort(intervals.begin(), intervals.end()); // 시작 시간 기준 정렬
        priority_queue<int, vector<int>, greater<int>> minHeap; // 최소힙에 회의 종료 시간 저장

        minHeap.push(intervals[0][1]);
        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start >= minHeap.top())  // 재사용 가능할 때 pop
                minHeap.pop();
            minheap.push(end); // 새로운 회의 종료시간 힙에 추가
        }
        return minHeap.size();
    }
};
