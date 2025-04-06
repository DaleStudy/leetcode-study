

class Solution {
    // 복잡도 O(n^2)
    // func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    //     for (i, num) in nums.enumerated() {
    //         guard let tempIndex = nums.firstIndex(of: target - num) else {continue}
    //         if tempIndex == i { continue }
    //         return [i, tempIndex]
    //     }
    //     return [0]
    // }

    // 시간, 공간 복잡도 O(n)
    // 해쉬맵 사용하기!
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var list: [Int:Int] = [:]
        for (i, num) in nums.enumerated() {
            if let exist = list[target-num] {
                return [exist, i]
            } else {
                list[num] = i
            }
        }
        return [0]


    }
}
