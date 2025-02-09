/**
 * 배열의 두개의 높이를 가지고 최대 용량을 구하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(1)
 * @param height
 */
function maxArea(height: number[]): number {
    // end - start * min(height[start], height[end])가 큰 것

    // 8 - 0 * min(1, 7) = 8
    // 8 - 1 * min(8, 7) = 49
    // 7 - 1 * min(8, 3) = 18
    // 6 - 1 * min(8, 8) = 40
    // ...

    let s = 0
    let e = height.length - 1
    let curr = 0
    let max = 0

    while(s < e) {
        curr = (e - s) * Math.min(height[s], height[e])
        max = Math.max(curr, max)
        if(height[s] < height[e]){
            s += 1
        } else {
            e -= 1
        }
    }

    return max
}
