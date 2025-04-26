// time: O(n)
class Solution {
    func hammingWeight(_ n: Int) -> Int {
        return String(n, radix: 2).filter{$0 == "1"}.count
    }
}
// time: O(1), space: O(1)
class AnotherSolution {
    func hammingWeight(_ n: Int) -> Int {
        var count = 0
        var num = n
        // 최대 32비트이기 때문에 반복을 32번 돌며 비트를 순회함
        for _ in 0..<32 {
            if num & 1 == 1 { // 가장 오른쪽 비트만 가져와 1인지 확인함
                count += 1 // 비트가 1이면 count 증가
            }
            num >>= 1 // 오른쪽으로 1비트 이동
        }
        return count
    }
}
