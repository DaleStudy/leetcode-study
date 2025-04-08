class Solution {
    /*
    1차 시도
    복잡도 - O(n log n)
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var list: [Int:Int] = [:]
        var result: [Int] = []
        if nums.count == 1 { return nums }

        for i in nums {
            list[i, default: 0] += 1
        }

        var sortedList = list.sorted { $0.value > $1.value }
        print(sortedList)

        for i in 0..<k {
            let target = sortedList[i].key
            result.append(target)
            // sortedList[target] = 0
        }
        return result
    } */
    
    // 2차 시도 : 복잡도 - O(n)
    class Solution {
        func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
            var freqMap = [Int: Int]()

            for num in nums {
                freqMap[num, default: 0] += 1
            }
            
            // 버켓에 빈도수를 인덱스로 값을 저장
            var buckets = Array(repeating: [Int](), count: nums.count + 1)
            for (num, freq) in freqMap {
                buckets[freq].append(num)
            }
            
            var result = [Int]()
            for i in (0 ..< buckets.count).reversed() {
                result += buckets[i]
                if result.count == k {
                    break
                }
            }
        
            return result
        }
    }
}
