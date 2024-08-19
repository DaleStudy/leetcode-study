import Foundation

final class MaxHeap<T: Comparable> {
    private var heap: [T] = []
    
    func insert(_ value: T) {
        heap.append(value)
        heapifyUp(from: heap.count - 1)
    }
    
    func pop() -> T? {
        guard !heap.isEmpty else {
            return nil
        }
        
        if heap.count == 1 {
            return heap.removeLast()
        }
        
        let removedValue = heap[0]
        heap[0] = heap.removeLast()
        heapifyDown(from: 0)
        
        return removedValue
    }
}

private extension MaxHeap {
    private func parentIndex(of index: Int) -> Int {
        return (index - 1) / 2
    }
    
    private func leftChildIndex(of index: Int) -> Int {
        return 2 * index + 1
    }
    
    private func rightChildIndex(of index: Int) -> Int {
        return 2 * index + 2
    }
    
    private func heapifyUp(from index: Int) {
        var currentIndex = index
        while currentIndex > 0 {
            let parentIdx = parentIndex(of: currentIndex)
            if heap[currentIndex] > heap[parentIdx] {
                heap.swapAt(currentIndex, parentIdx)
                currentIndex = parentIdx
            } else {
                break
            }
        }
    }
    
    private func heapifyDown(from index: Int) {
        var oldIndex = index
        let count = heap.count
        
        while true {
            let leftIndex = leftChildIndex(of: oldIndex)
            let rightIndex = rightChildIndex(of: oldIndex)
            var newIndex = oldIndex
            
            if leftIndex < count && heap[leftIndex] > heap[newIndex] {
                newIndex = leftIndex
            }
            
            if rightIndex < count && heap[rightIndex] > heap[newIndex] {
                newIndex = rightIndex
            }
            
            if newIndex == oldIndex {
                break
            }
            
            heap.swapAt(oldIndex, newIndex)
            oldIndex = newIndex
        }
    }
}

struct Item: Comparable {
    let num: Int
    let count: Int

    static func < (lhs: Item, rhs: Item) -> Bool {
        return lhs.count < rhs.count
    }
}

class Solution {

    /*
        Runtime: 30 ms (Beats 65.79%)
        Analyze Complexity: O(n log n), n개의 숫자에 대해 heappush, k개의 item에 대해 heappop
        Memory: 17.63 MB (Beats 64.66%)
    */
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var countDict: [Int: Int] = [:]
        for num in nums {
            countDict[num] = (countDict[num] ?? 0) + 1
        }

        var maxHeap = MaxHeap<Item>()
        for (num, count) in countDict {
            maxHeap.insert(Item(num: num, count: count))
        }

        var result: [Int] = []
        for _ in 0..<k {
            if let maxItem = maxHeap.pop() {
                result.append(maxItem.num)
            }
        }

        return result
    }
}
