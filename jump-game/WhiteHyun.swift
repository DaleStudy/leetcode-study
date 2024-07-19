//  
//  55. Jump Game
//  https://leetcode.com/problems/jump-game/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/20.
//  

class Solution {
  func canJump(_ numbers: [Int]) -> Bool {
    var goal = numbers.endIndex - 1

    for index in numbers.indices.dropLast().reversed() where index + numbers[index] >= goal {
      goal = index
    }

    return goal == 0
  }
}
