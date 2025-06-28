/*
    minHeap이 항상 maxHeap보다 크거나 같도록 유지한다.
    addNum()
        - maxHeap에 새로 들어온 num을 포함한 최댓값을 minHeap으로 옮긴다
        - 처음엔 maxHeap과 minHeap의 크기 차이가 1이므로 if문에 들어가지 않지만
        - 이후 num이 minHeap으로 하나 더 넘어가게 되면 maxHeap과 minHeap의 크기 차이가 2가 되므로 
            if문에 들어가서 maxHeap쪽으로 minHeap의 최솟값을 옮긴다
        힙 삽입에 O(logn)이 걸리므로 시간복잡도는 O(logn)이다
    findMedian()
        - 두 힙의 top만 참조하면 되므로 시간 복잡도는 O(1)이다
    최소힙과 최대힙은 각각 전체 수의 절반씩을 저장한다.
    공간 복잡도는 O(n)이다
*/
class MedianFinder {
public:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    MedianFinder() {
    }
    
    void addNum(int num) {
        maxHeap.push(num);
        
        minHeap.push(maxHeap.top());
        maxHeap.pop();

        if (maxHeap.size() + 1 < minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        if (maxHeap.size() == minHeap.size())
            return (minHeap.top() + maxHeap.top()) / 2.0;
        return minHeap.top();
    }
};
