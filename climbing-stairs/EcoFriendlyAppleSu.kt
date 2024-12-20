package leetcode_study

/**
 * 계단에 올라갈 수 있는 경우의 수 구하는 방법
 * 시간 복잡도: O(n)
 * -> 주어진 횟수 만큼 반복 진행
 * 공간 복잡도: O(k)
 * -> 주어진 계단 수 만큼 횟수를 저장할 공간 필요
 */
fun climbStairs(n: Int): Int {
    val step = IntArray(n+1)

    if (n == 1) {
        return 1
    }
    step[1] = 1
    step[2] = 2

    for (i in 3 until step.size) {
        step[i] = step[i-1] + step[i-2]
    }

    return step[n]
}
