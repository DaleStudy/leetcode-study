/*
# Time Complexity: O(nlogn)
# Space Complexity: O(nlogn)

*/
class MedianFinder {

    private PriorityQueue<Integer> pq1; // 1번째 ~ 가운데 원소 (max heap)
    private PriorityQueue<Integer> pq2; // 가운데+1번째 ~ 마지막 원소 (min heap)

    public MedianFinder() {
        pq1 = new PriorityQueue<>(Collections.reverseOrder());
        pq2 = new PriorityQueue<>();
    }

    public void addNum(int num) {

        if (pq1.size() == pq2.size()) {
            if (pq1.peek() == null || pq1.peek() >= num) {
                pq1.add(num);
            } else {
                pq2.add(num);
                pq1.add(pq2.poll());
            }
        } else {
            if (pq1.peek() == null || pq1.peek() >= num) {
                pq1.add(num);
                pq2.add(pq1.poll());
            } else {
                pq2.add(num);
            }
        }
    }

    public double findMedian() {
        if (pq1.size() == pq2.size()) {
            return (pq1.peek() + pq2.peek()) / 2.0;
        } else {
            return pq1.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
