import java.util.PriorityQueue
class MedianFinder() {
    // 1 2 3 4 5
    // 중간값을 기준으로 
    //   3
    //  2 4
    // 1   5
    // 1 2 : maxHeap
    // 4 5 : minHeap
    private val maxHeap = PriorityQueue<Int> { a, b -> b - a }
    private val minHeap = PriorityQueue<Int>()

    // TC: O(log n)
    // SC: O(n)
    fun addNum(num: Int) {
       if(maxHeap.isEmpty() || maxHeap.peek() >= num) {
        maxHeap.add(num)
       } else {
        minHeap.add(num)
       }

       if(maxHeap.size > minHeap.size + 1) {
        minHeap.add(maxHeap.poll())
       } else if(minHeap.size > maxHeap.size) {
        maxHeap.add(minHeap.poll())
       }
    }

    fun findMedian(): Double {
       if(maxHeap.size == minHeap.size) {
        return (maxHeap.peek() + minHeap.peek()) / 2.0
       } else {
        return maxHeap.peek().toDouble()
       }
    }

}
