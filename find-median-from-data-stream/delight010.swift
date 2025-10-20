class MedianFinder {
    
    struct Heap {
        private var element: [Int] = []
        private let isMinHeap: Bool
        var count: Int {
            return element.count
        }
        
        init(isMinHeap: Bool) {
            self.isMinHeap = isMinHeap
        }
        
        func peek() -> Int? {
            return element.first
        }
        
        mutating func insert(_ value: Int) {
            element.append(value)
            
            var currentIndex = element.count - 1
            
            while currentIndex > 0 {
                let parentIndex = (currentIndex - 1) / 2
                
                if isMinHeap {
                    if element[currentIndex] < element[parentIndex] {
                        let temp = element[currentIndex]
                        element[currentIndex] = element[parentIndex]
                        element[parentIndex] = temp
                        
                        currentIndex = parentIndex
                    } else {
                        break
                    }
                } else {
                    if element[currentIndex] > element[parentIndex] {
                        let temp = element[currentIndex]
                        element[currentIndex] = element[parentIndex]
                        element[parentIndex] = temp
                        
                        currentIndex = parentIndex
                    } else {
                        break
                    }
                }
            }
        }
        
        mutating func remove() -> Int? {
            guard !element.isEmpty else { return nil }
            
            if element.count == 1 {
                return element.removeLast()
            }
            
            let value = element[0]
            
            element[0] = element.removeLast()
            siftDown(index: 0)
            
            return value
        }
        
        mutating private func siftDown(index: Int) {
            var parentIndex = index
            var count = element.count
            
            while parentIndex < count {
                let leftChildIndex = parentIndex * 2 + 1
                let rightChildIndex = parentIndex * 2 + 2
                var tempIndex = parentIndex
                
                if isMinHeap {
                    if leftChildIndex < count && element[leftChildIndex] < element[parentIndex] {
                        tempIndex = leftChildIndex
                    }
                    
                    if rightChildIndex < count && element[rightChildIndex] < element[tempIndex] {
                        tempIndex = rightChildIndex
                    }
                    
                } else {
                    if leftChildIndex < count && element[leftChildIndex] > element[parentIndex] {
                        tempIndex = leftChildIndex
                    }
                    
                    if rightChildIndex < count && element[rightChildIndex] > element[tempIndex] {
                        tempIndex = rightChildIndex
                    }
                }
                
                if parentIndex == tempIndex {
                    break
                }
                
                element.swapAt(parentIndex, tempIndex)
                parentIndex = tempIndex
            }
        }
    }
    
    private var maxHeap = Heap(isMinHeap: false)
    private var minHeap = Heap(isMinHeap: true)

    init() {
        
    }
    
    func addNum(_ num: Int) {
        if maxHeap.count == 0 {
            maxHeap.insert(num)
            return
        }
        
        if num <= maxHeap.peek()! {
            maxHeap.insert(num)
        } else {
            minHeap.insert(num)
        }
        
        if minHeap.count > maxHeap.count {
            maxHeap.insert(minHeap.remove()!)
        }
        
        if maxHeap.count > minHeap.count + 1 {
            minHeap.insert(maxHeap.remove()!)
        }
    }
    
    func findMedian() -> Double {
        if maxHeap.count == minHeap.count {
            return Double((maxHeap.peek()! + minHeap.peek()!)) / 2
        }
        
        return Double(maxHeap.peek()!)
    }
}
 
