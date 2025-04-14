//
//  Untitled.swift
//  Algorithm
//
//  Created by 안세훈 on 4/14/25.
//

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        var validS = s.lowercased().filter{$0.isNumber == true || $0.isLetter == true}
        //s를 모두 소문자로 변환 후 숫자 or 문자가 true인 문자만 validS에 배열로 추출.
        
        if validS == String(validS.reversed()){ //validS와 뒤집은 것과 같다면 true 아니면 false
            return true
        }else{
            return false
        }
    }
}
