package leetcode_study

//
/*
* 주어진 양의 정수(n)를 이진수로 변환했을 때, 1의 개수를 구하는 문제 (1 <= n <= 2^31 -1. 즉, 양의 정수)
* _> 숫자가 Decimal로 주어지더라도 bit 연산에서는 내부적으로 binary 로 변환하여 처리됩니다.
* 시간 복잡도: O(1)
* -> masking 연산은 항상 32번 고정이기 때문에 상수 시간 복잡도
* 공간 복잡도: O(1)
* -> 추가적인 메모리 사용 없이 두 개의 변수 count, mask만 사용되기 때문에 상수 공간 복잡도
* */
fun hammingWeight(n: Int): Int {
    var count = 0
    var mask = 1 shl 31
    while (mask != 0) {
        if (n and mask != 0) {
            count++
        }
        mask = mask ushr 1
    }
    return count
}
