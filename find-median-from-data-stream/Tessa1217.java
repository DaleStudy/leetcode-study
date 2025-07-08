import java.util.PriorityQueue;

class MedianFinder {

    // 작은 수 범위 저장하는 힙
    private PriorityQueue<Integer> smallHeap;

    // 큰 수 범위 저장하는 힙
    private PriorityQueue<Integer> largeHeap;

    public MedianFinder() {
        smallHeap = new PriorityQueue<>((a, b) -> b - a);
        largeHeap = new PriorityQueue<> ((a, b) -> a - b);
    }

    public void addNum(int num) {
        // 작은 수 범위에 삽입
        smallHeap.offer(num);
        // 작은 수 범위에서 최댓값을 뽑아 큰 수 범위로 이동
        largeHeap.offer(smallHeap.poll());

        // 만약 작은 수 범위의 개수가 큰 수 범위보다 작다면
        if (smallHeap.size() < largeHeap.size()) {
            // 큰 수 범위에서 최솟값을 뽑아 작은 수 범위로 이동
            smallHeap.offer(largeHeap.poll());
        }
    }

    public double findMedian() {
        // 짝수 개일 경우
        if (smallHeap.size() == largeHeap.size()) {
            // 작은 수 범위 힙의 최댓값 + 큰 수 범위 힙의 최솟값의 평균
            return (smallHeap.peek() + largeHeap.peek()) / 2.0;
        }
        // 작은 수 범위 힙의 최댓값
        return smallHeap.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

