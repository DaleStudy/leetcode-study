// time: O(n)
// approach - 2자리 3자리 ... 로 2진법 변환시 맨 앞 1은 고정이다.
// 그 이후 나머지는 0~N자리일때 총 1의 갯수 를 더해줬다.
class Solution {
    func countBits(_ n: Int) -> [Int] {
        var answer: [Int] = [0, 1]

        while answer.count < n + 1 {
            answer += answer.map{$0 + 1}
        }

        return [Int](answer.prefix(n + 1))
    }
}
