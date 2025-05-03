// time: O(n+m) space: O(1)
class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        // 전처리
        guard list1 != nil, list2 != nil else { return list1 ?? list2 }
        // 변수 정의
        var answer: ListNode? = ListNode(0)
        var top: ListNode? = answer
        var list1 = list1
        var list2 = list2
        // 2개의 ListNode를 순회하면서 값을 보고 작은 순으로 저장 (ListNode에)
        while list1 != nil && list2 != nil {
            if let value1 = list1?.val, let value2 = list2?.val {
                if value1 < value2 {
                    answer?.next = ListNode(value1)
                    list1 = list1?.next
                }
                else {
                    answer?.next = ListNode(value2)
                    list2 = list2?.next
                }
                answer = answer?.next
            }
        }
        // 남은 노드들 연결하기
        answer?.next = list1 ?? list2
        return top?.next
    }
}
