
/**
 * 시간 복잡도: O(nlogn) - sort 메소드
 */
// class MedianFinder {
//     arr: number[]
//     constructor() {
//         this.arr = [];
//     }

//     addNum(num: number): void {
//         this.arr.push(num)
//         this.arr.sort((a, b) => a - b);
//     }

//     findMedian(): number {
//         const len = this.arr.length;
//         const mid = Math.floor(len / 2);
//         if(len % 2) return this.arr[mid];
//         else return (this.arr[mid - 1] + this.arr[mid]) / 2;
//     }
// }

/**
 * 시간 복잡도: O(log n) - 힙 연산의 시간 복잡도
 * 공간 복잡도: O(n) - n개의 숫자를 저장하는 데 필요한 공간
 */
class MedianFinder {
    maxHeap = new MaxPriorityQueue() // 최대값을 트리의 루트에 위치시키는 힙 
    minHeap = new MinPriorityQueue() // 최소값을 트리의 루트에 위치시키는 힙 
    size: number

    constructor() {
        this.size = 0
    }

    addNum(num: number): void {
        this.size++
        this.maxHeap.enqueue(num) // 먼저 최대 힙에 추가
        const item = this.maxHeap.dequeue() // 최대 힙의 최대값 제거
        this.minHeap.enqueue(item) // 최소 힙에 추가 

        // 최소 힙이 크면 최대 힙으로 이동
        if (this.minHeap.size() > this.maxHeap.size()+1) {
            const item = this.minHeap.dequeue() 
            this.maxHeap.enqueue(item)
        }
    }

    findMedian(): number {
        if (this.size % 2 !== 0) {
            // 최소 힙의 최소값 
            return this.minHeap.front()
        } else {
            // 최대 힙의 최대값(root)과 최소 힙의 최소값(root)의 평균
            return (this.maxHeap.front() + this.minHeap.front()) / 2 
        }
    }
}
/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
