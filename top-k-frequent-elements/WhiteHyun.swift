//  
//  347. Top K Frequent Elements
//  https://leetcode.com/problems/top-k-frequent-elements/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/01.
//  

final class Solution {
  func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
    // Python의 Counter 모듈처럼 만드는 것과 동일
    var counter: [Int: Int] = [:]
    for number in nums {
      counter[number, default: 0] += 1
    }
    
    return counter
      .sorted { lhs, rhs in
        lhs.value > rhs.value                             // 빈도 수를 기준으로 내림차순 정렬
      }
      .prefix(k)                                          // 앞에서부터 k만큼 Subarray로 가져옴
      .map(\.key)                                         // 제일 빈도가 많았던 것의 숫자를 가져옴 (Dictionary의 Key값)
  }
}
