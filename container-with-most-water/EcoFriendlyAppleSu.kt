package leetcode_study

/*
* 주어진 높이에서 만들 수 있는 가장 큰 면적을 구하는 문제.
* Brute force로 모든 경우의 수를 따져가며 최대 면적을 구하는 방법.
* 주어진 높이(n)의 개수는 2 보다 크거가 같고 10^4 보다 작거나 같음.
* 이중 Loop으로 해결할 경우 시간 초과 발생 (10^8 이하로 해결해야 제한 시간 안으로 문제 해결 가능)
*
* 시간 복잡도: O(n^2)
* -> 두 개의 서로 다른 높이를 구하기 위해 이중 반복문 실행: O(n^2)
* 공간 복잡도: O(1)
* -> 추가 메모리 사용 없음.
* */
fun maxArea01(height: IntArray): Int {
    var maxValue = 0
    for (i in 0 until height.size) {
        for (j in i + 1 until height.size) {
            // 너비는 두 선분 사이의 거리
            val width = j - i
            // 높이는 두 선분 중 작은 값
            val containerHeight = Math.min(height[i], height[j])
            // 면적 계산
            val area = width * containerHeight
            // 최대값 갱신
            maxValue = Math.max(maxValue, area)
        }
    }
    return maxValue
}

/*
* 이중 포인터를 사용한 문제 풀이.
* 결과에 영향을 주는 조건과 요소
* -> 높이의 위치를 나타내는 왼쪽값과 오른쪽 값에서 두 값 중 작은 값이 높이가 될 수 있음.
* -> 오른쪽의 값은 왼쪽 값보다 작을 수 없음.
* -> 너비 값은 오른쪽 인덱스에서 왼쪽 인덱스를 뺀 값임.
*
* 시간 복잡도: O(n)
* -> 주어진 높이 배열에서 양쪽 끝 값을 증감/가감 해가며 반복 진행: O(n)
* 공간 복잡도: O(1)
* -> 추가 메모리 사용 없음.
* */
fun maxArea02(height: IntArray): Int {
    var maxValue = 0
    var left = 0
    var right = height.size - 1
    while (left <= right) {
        val width = right - left
        val containerHeight = Math.min(height[left], height[right])
        val area = width * containerHeight
        maxValue = Math.max(maxValue, area)
        if (height[left] < height[right]) {
            left++
        } else {
            right--
        }
    }
    return maxValue
}
