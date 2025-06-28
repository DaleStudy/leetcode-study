/**
 * [Problem]: [295] Find Median from Data Stream
 * (https://leetcode.com/problems/find-median-from-data-stream/description/)
 */
class Heap {
    private numbers: number[];
    private compare: (a: number, b: number) => boolean;

    constructor(compare: (a: number, b: number) => boolean) {
        this.numbers = [];
        this.compare = compare;
    }

    private getParentIdx(index: number) {
        return Math.floor((index - 1) / 2);
    }

    private getLeftChildIdx(index: number) {
        return 2 * index + 1;
    }

    private getRightChildIdx(index: number) {
        return 2 * index + 2;
    }

    private swap(index1: number, index2: number): void {
        [this.numbers[index1], this.numbers[index2]] = [this.numbers[index2], this.numbers[index1]];
    }

    private heapifyUp(index: number) {
        const parentIndex = this.getParentIdx(index);
        if (0 <= parentIndex && this.compare(this.numbers[index], this.numbers[parentIndex])) {
            this.swap(index, parentIndex);
            this.heapifyUp(parentIndex);
        }
    }

    private heapifyDown(index: number): void {
        const leftChildIndex = this.getLeftChildIdx(index);
        const rightChildIndex = this.getRightChildIdx(index);
        let largestIndex = index;

        if (
            leftChildIndex < this.numbers.length &&
            this.compare(this.numbers[leftChildIndex], this.numbers[largestIndex])
        ) {
            largestIndex = leftChildIndex;
        }

        if (
            rightChildIndex < this.numbers.length &&
            this.compare(this.numbers[rightChildIndex], this.numbers[largestIndex])
        ) {
            largestIndex = rightChildIndex;
        }

        if (largestIndex !== index) {
            this.swap(index, largestIndex);
            this.heapifyDown(largestIndex);
        }
    }

    insert(number: number) {
        this.numbers.push(number);
        this.heapifyUp(this.numbers.length - 1);
    }

    pop() {
        if (this.numbers.length === 0) {
            return null;
        }

        if (this.numbers.length === 1) {
            return this.numbers.pop()!;
        }

        const root = this.numbers[0];
        this.numbers[0] = this.numbers.pop()!;
        this.heapifyDown(0);

        return root;
    }

    peek() {
        return this.numbers.length > 0 ? this.numbers[0] : null;
    }

    size(): number {
        return this.numbers.length;
    }
}

class MedianFinder {
    private smallHeap: Heap;
    private largeHeap: Heap;

    constructor() {
        this.smallHeap = new Heap((a, b) => a > b);
        this.largeHeap = new Heap((a, b) => a < b);
    }

    //시간복잡도 O(log n)
    addNum(num: number): void {
        this.smallHeap.insert(num);
        this.largeHeap.insert(this.smallHeap.pop()!);

        if (this.smallHeap.size() < this.largeHeap.size()) {
            this.smallHeap.insert(this.largeHeap.pop()!);
        }
    }

    //시간복잡도 O(1)
    findMedian(): number {
        if (this.smallHeap.size() > this.largeHeap.size()) {
            return this.smallHeap.peek()!;
        } else {
            return (this.smallHeap.peek()! + this.largeHeap.peek()!) / 2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
