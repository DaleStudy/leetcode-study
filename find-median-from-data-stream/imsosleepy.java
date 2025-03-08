// 메모리초과로 알 수 있었던 것은 저장 공간이 여러개 필요하다는 거 였다.
// 그리고 주어진 데이터가 정렬되지 않아서 무조건 nlog(n) 이상의 시간복잡도가 나오기 때문에
// 자동 정렬할 수 있는 우선순위 큐를 사용하면 좋겠따고 생각
// 그러나 데이터를 나누는 알고리즘이 필요한지 모르고 헤메다가 GPT 답을 보게됨
// 시간복잡도 우선순위 큐 : O(logN)
class MedianFinder {
    private PriorityQueue<Integer> maxHeap;
    private PriorityQueue<Integer> minHeap;

    public MedianFinder() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        maxHeap.offer(num);

        if (!minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
            minHeap.offer(maxHeap.poll());
        }

        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    public double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.peek();
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }
}

// 메모리초과
class MedianFinder {
    private List<Integer> arr;

    public MedianFinder() {
        arr = new ArrayList<>();
    }

    public void addNum(int num) {
        arr.add(num);
    }

    public double findMedian() {
        Collections.sort(arr);

        int size = arr.size();
        if (size % 2 == 1) {
            return arr.get(size / 2);
        } else {
            return (arr.get(size / 2 - 1) + arr.get(size / 2)) / 2.0;
        }
    }
}
