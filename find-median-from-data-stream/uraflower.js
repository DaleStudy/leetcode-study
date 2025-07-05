// 배열 + 이분 탐색 삽입 (정렬) 로 풀이함

// 다른 방식으로는 듀얼 힙을 사용하는 게 있음 (성능 면에서 더 우수함)
// 최소힙, 최대힙 두 개를 두고 나눠서 add 이 때 size 차이는 1 이하여야 함
// ex. 1 2 3 4 5 6 => 최대 힙에 1 2 3, 최소 힙에 4 5 6 => (3 + 4) / 2
// ex. 2 3 4 => 최대 힙에 2 3, 최소 힙에 4 => 3
// 참고로 leetcode에서 JS를 위한 MaxPriorityQueue와 같은 자료구조를 제공하는 듯 한데...
// 메서드를 어디서 볼 수 있는지 모르겠음

class MedianFinder {
    constructor() {
        this.nums = [];
    }

    /**
     * 시간복잡도: O(n) (이분탐색: log n, splice: n)
     * 공간복잡도: O(1)
     * @param {number} num
     * @return {void}
     */
    addNum(num) {
        const i = this.#findInsertPosition(num);
        this.nums.splice(i, 0, num);
    }

    /**
     * 이진 탐색으로 삽입 지점 찾는 함수
     * 시간복잡도: O(log n)
     * 공간복잡도: O(1)
     */
    #findInsertPosition(num) {
        let left = 0;
        let right = this.nums.length;
        
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (num < this.nums[mid]) {
                right = mid - 1;
            } else if (this.nums[mid] < num) {
                left = mid + 1;
            } else {
                return mid;
            }
        }

        return left;
    }

    /**
     * 시간복잡도: O(1)
     * 공간복잡도: O(1)
     * @return {number}
     */
    findMedian() {
        const len = this.nums.length;
        const midIndex = Math.floor(len / 2);

        if (len % 2 === 0) {
            return (this.nums[midIndex - 1] + this.nums[midIndex]) / 2;
        } else {
            return this.nums[midIndex];
        }
    }
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
