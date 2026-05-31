class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count - 1

        while left <= right {
            let mid = (left + right) / 2
                
            // 일단, 찾았으면 바로 반환
            if nums[mid] == target {
                return mid
            }
            
            // 이 문제의 배열은 정렬되지 않은 것이 아니고, 정렬된 배열 두 개를 붙여 놨다고 생각하면 된다.
            // 유효한 인덱스임이 보장된 left와 현재 인덱스인 mid를 비교한다.
            if nums[left] <= nums[mid] {
                // 이로써 left와 mid 사이가 이 "정렬된 부분"임을 체크한다.
                // 정렬이 되어 있다면, 찾고자 하는 값이 이 "정렬된 범위" 내에 있는지 확인한다.
                // left에서 >=를 이용한 이유는, left 자체가 정답 인덱스일 수도 있기 때문.
                if target >= nums[left] && target < nums[mid] {
                    // 만약 그렇다면 통상적인 이진 탐색의 논리대로 가면 된다.
                    right = mid - 1
                } else {
                    // 만약 그렇지 않다면 원래 갔어야 할 방향의 반대 방향으로 가면 된다.
                    left = mid + 1
                }
            } else {
                // left와 mid 사이가 정렬이 틀어져 있다면, mid와 right 사이는 정렬되어 있는 것이다.
                // 위와 동일하게 범위 확인을 하되, 방향을 반대로 가져가면 된다.
                if target <= nums[right] && target > nums[mid] {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        // early return하지 못했다면, 배열 내에 찾고자 하는 수가 없는 것이다.
        return -1
    }
}
