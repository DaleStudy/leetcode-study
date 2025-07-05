/**
 * <a href="https://leetcode.com/problems/find-median-from-data-stream/">week13-4. find-median-from-data-stream</a>
 * <li>Description: Implement the MedianFinder class</li>
 * <li>Topics: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream</li>
 * <li>Time Complexity: O(logN), Runtime 99ms   </li>
 * <li>Space Complexity: O(N), Memory 63.68MB   </li>
 */

class MedianFinder {
    PriorityQueue<Integer> head;
    PriorityQueue<Integer> tail;

    public MedianFinder() {
        head = new PriorityQueue<>(Comparator.reverseOrder());
        tail = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if(head.isEmpty() || num <= head.peek()) {
            head.add(num);
        } else {
            tail.add(num);
        }

        if (head.size() > tail.size() + 1) {
            tail.add(head.poll());
        } else if (head.size() < tail.size()) {
            head.add(tail.poll());
        }
    }

    public double findMedian() {
        if(head.size() == tail.size()){
            return ((double)head.peek() + tail.peek()) / 2;
        }
        return head.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
