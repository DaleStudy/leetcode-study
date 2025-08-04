///양의 정수 n이 주어졌을 때,
///이진 표현으로 setbit의 수를 반환하는 함수(해밍 가중치라고도 함)를 작성합니다.
///setbit이란 이진수 중에서 1의 값을 가지는 비트의 갯수

class Solution {
    func hammingWeight(_ n: Int) -> Int {
        let count = String(n, radix: 2).filter { $0 == "1" }.count
        return count
    }
}
