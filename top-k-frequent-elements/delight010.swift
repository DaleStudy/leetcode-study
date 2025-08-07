class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dictionary: [Int: Int] = [:]
        for num in nums { // for loop를 돌면서 O(n)의 시간복잡도
            dictionary[num, default: 0] += 1
            // Swift에서 dictionary 검색의 시간복잡도는 O(1)
        }
        
        return dictionary
            .sorted(by: { $0.value > $1.value })
        // dictionary sorted()의 시간복잡도 O(n log n)
            .prefix(k)
        // k의 개수만큼 탐색합니다. 고로 시간복잡도는 O(n)
            .map(\.key)
        // prefix에서 k만큼 탐색하였습니다.
        // .map의 시간복잡도는 O(n)입니다.
    }
}
 
