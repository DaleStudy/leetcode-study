//
//  20. Valid Parentheses.swift
//  https://leetcode.com/problems/valid-parentheses/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/05/04.
//

import Foundation

final class LeetCode20 {
  func isValid(_ s: String) -> Bool {
    var stack: [Character] = []

    for character in s {
      if "([{".contains(character) {
        stack.append(character)
        continue
      }

      // `([{`가 아닌 닫힌 괄호가 들어왔는데 stack이 비어있으면 안 됨.
      if stack.isEmpty { return false }

      // 아스키 값의 차를 활용하여 1~2사이의 차이가 난다면 알맞은 쌍.
      // 하지만, 각 괄호의 아스키 값이 3 이상 나는 경우는 서로 맞지 않음.
      // Swift에서는 asciiValue 프로퍼티의 타입이 `UInt8` 이기 때문에 음수가 없어서 가능한 비교!
      // `&-` 는 오버플로우 연산으로, 만약 오버플로우가 난다면 무시함.
      if character.asciiValue! &- stack.last!.asciiValue! > 2 {
        return false
      }

      stack.removeLast()
    }

    return stack.isEmpty
  }
}
