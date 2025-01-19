package leetcode_study

/**
 * 시간복잡도 : O(n)
 * - 두개의 포인터를 이용하여 n의 길이를 가진 배열을 한 번 확인하므로 O(n) 입니다.
 *
 * 공간복잡도 : O(1)
 * 변수로만 값을 저장하으므로 O(1) 입니다.
 * */
fun maxArea(height: IntArray): Int {
    var maxWater = 0

    var firstPoint = 0
    var secondPoint = height.size - 1

    while (firstPoint != secondPoint) {
        val width = secondPoint - firstPoint
        val lessHeight = minOf(height[firstPoint], height[secondPoint])
        maxWater = maxOf(maxWater, width * lessHeight)

        if (height[firstPoint] < height[secondPoint]) firstPoint += 1
        else secondPoint -= 1
    }

    return maxWater
}
