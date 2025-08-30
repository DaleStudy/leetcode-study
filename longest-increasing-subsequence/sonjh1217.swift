class Solution {
    // O(nlogn) time / O(n) space
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var piles: [Int] = []
        // Patience(1인 카드놀이) sort 이용
        for num in nums {
            let leftInsertion = binarySearch(piles: piles, target: num)

            // piles[k] >= x인 pile이 없을 때만 append(길이 증가)
            if leftInsertion == piles.count {
                piles.append(num)
            } else {
                //가장 왼쪽의 piles[k] >= x 위치에 교체
                piles[leftInsertion] = num
            }

        }
        
        // piles[k] = 길이 (k+1) 증가수열이 가질 수 있는 '끝값의 최소치'
        // sort 로직상 piles.count가 최대한 길게 만들었기 때문에 piles.count는 가장 긴 길이가 됨
        return piles.count
    }

    func binarySearch(piles: [Int], target: Int) -> Int {
        var left = 0
        
        //target의 삽입 위치고 맨 끝에 덧붙일수도 있어서 nums.count - 1 이 아님
        var right = piles.count

        while left < right {
            let mid = left + (right - left) / 2
            if target > piles[mid] {
                left = mid + 1
            } else {
                //맨 왼쪽 거를 찾아야 함으로 다시 쪼개가면서 맨 왼쪽 거를 찾는다. 맨 왼쪽 거에 넣어야 길이(k) 증가수열의 끝값이 가장 작게 된다. 이래야 최대한 뒤에 계속 더 이어붙여서 최대한 길게 piles를 만들 수 있음.
                right = mid
            }
        }
        return left
    }
}
