//
//  Merge_Two_Sorted_Lists.swift
//  Algorithm
//
//  Created by 안세훈 on 4/22/25.
//

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        //list1, list2가 nil일 경우를 대비해 전처리
        guard list1 != nil else { return list2 }
        guard list2 != nil else { return list1 }

        //초기화 Node
        var head : ListNode? = ListNode(0)

        //연산을 위한 Node
        var current = head
        var l1 = list1
        var l2 = list2

        while l1 != nil && l2 != nil{                     //두 리스트 모두 nil이 아닐 경우에만 연산.
            if let val1 = l1?.val, let val2 = l2?.val{    //비교할 node를 각각 list1?.val, list2?.val로 안전히 바인딩
                if val1 < val2{                           //두 수 비교
                    current?.next = ListNode(val1)        //reusltNode의 다음을 작은수로 설정
                    l1 = l1?.next                         //연산 후 다음 노드로 넘김
                }else{
                    current?.next = ListNode(val2)        //reusltNode의 다음을 작은수로 설정
                    l2 = l2?.next                         //연산 후 다음 노드로 넘김
                }
                current = current?.next                   //연산 후 결과 노드도 다음으로 넘김
            }
        }
        current?.next = l1 ?? l2                          //while이 끝난 후 남은 노드는 뒤에 붙힘

        return head?.next
    }
}
