class MedianFinder {
    arr: number[]
    constructor() {
        this.arr = []
    }
    /*
    Time Complexity: O(logn)
    Space Complexity: O(n)
    */
    addNum(num: number): void {
        let left = 0
        let right = this.arr.length

        while (left < right) {
            const mid = Math.floor((left + right) / 2)
            if (this.arr[mid] < num) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        this.arr.splice(left, 0, num)
    }
    /*
    Time Complexity: O(1)
    Space Complexity: O(n)
    */
    findMedian(): number {
        const n = this.arr.length
        if (n % 2 === 0) {
            return (this.arr[n / 2 - 1] + this.arr[n / 2]) / 2
        } else {
            return (this.arr[Math.floor(n / 2)])
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
