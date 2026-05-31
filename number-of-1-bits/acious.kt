class Solution {
    fun hammingWeight(n: Int): Int {
        // 2^31 = 1,073,741,823
        // 몫 : dividend
        // 한텀당 n을 2로 나눠서 몫과 나머지를 구해냄. 나머지가 1이면 result에 +=1, 나머지가 0이면 result에 변화없음.
        // 몫이 0으로 떨어지면 연산이 끝나고 result 반환
        // 시간 복잡도 : n이 최대 2^31이고 n이 커짐에 따라 최대 31번 반복문이 도므로 O(1)
        // 공간복잡도 : O(1)
        var dividend = n
        var result = 0
        while (dividend != 0) {
            if (dividend % 2 == 1) {
                result+=1
            }
            dividend = dividend/2
        }
        return result
    }
}
