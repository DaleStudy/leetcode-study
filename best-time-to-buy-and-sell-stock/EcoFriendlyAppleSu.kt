package leetcode_study

/*
* 두 거래일 사이 최고의 수익을 구하는 문제
* 시간 복잡도: O(n^2)
* -> 모든 경우의 수를 순회하며 거래일 사이 최고 가격을 구하는 로직: O(n^2)
* 공간 복잡도: O(1)
* 아래 로직은 시간 초과 발생 O(n^2)의 복잡도를 줄여야함.
* */
fun maxProfit(prices: IntArray): Int {
    var result = Int.MIN_VALUE

    for (i in prices.indices) {
        for (j in i + 1 until prices.size) {
            if (prices[i] < prices[j]) {
                if (result < prices[j] - prices[i]) {
                    result = prices[j] - prices[i]
                }
            }
        }
    }
    if (result == Int.MIN_VALUE) return 0
    return result
}

/*
* 가장 작은 값을 저장하는 변수와 가장 큰 수익을 갖는 변수를 두고 문제 해결
* 시간 복잡도: O(n)
* 공간 복잡도: O(1)
* */
fun maxProfit2(prices: IntArray): Int {
    var minValue = Int.MAX_VALUE
    var maxValue = 0

    for (price in prices) {
        if (price < minValue) {
            minValue = price
        } else if (price - minValue > maxValue) {
            maxValue = price - minValue
        }
    }
    return maxValue
}
