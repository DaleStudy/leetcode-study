class MedianFinder {
    PriorityQueue<Integer> left;
    PriorityQueue<Integer> right;

    public MedianFinder() {
        /**
        리스트를 중간으로 나눠서 절반은 왼쪽, 오른쪽에 저장
        왼쪽 리스트는 항상 큰 수가 가장 왼쪽(앞)에 오도록
        오른쪽 리스트는 항상 작은 수가 가장 왼쪽(앞)에 오도록 저장한다.

         */
        left = new PriorityQueue<>(Collections.reverseOrder()); //max heap
        right = new PriorityQueue<>(); //min heap
        
    }
    
    public void addNum(int num) {
        left.add(num);
        right.add(left.poll());

        //총 원소 수가 홀수개이면 left size 더 크도록 유지 
        if(right.size() > left.size()) {
            left.add(right.poll());
        }
    }
    
    public double findMedian() {
        if(left.size() > right.size()) {
            return left.peek();
        }
        return (left.peek() + right.peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
