// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        // 뒤에서 n번째 노드를 찾기 위한 Two Pointer
        var slow = head
        var fast = head
        var threshold = n

        // fast 포인터를 n만큼 이동시킴
        // 전체 갯수를 c개라고 했을 때, 뒤에서 n번째 노드는 앞에서 c - n + 1번째 노드
        while threshold > 0 {
            fast = fast?.next
            threshold -= 1
        }

        // padding 노드 생성
        var prev: ListNode? = ListNode()
        // slow 포인터에 위치한 노드를 제거하는 전략 - prev 포인터를 slow 포인터의 이전 노드로 이동시킴
        prev?.next = slow
        
        // 반환을 위한 result 노드 포인터 생성
        let result = prev

        while fast != nil {
            prev = prev?.next
            slow = slow?.next
            fast = fast?.next
        }

        // fast 노드는 리스트의 범위를 벗어나 nil이 되었고,
        // slow 노드는 뒤에서 n번째 자리에 위치해 있음
        // 그보다 한 칸 앞에 있는 prev 노드의 next를, next?.next로 바꿔 주면, slow 부분의 노드 제거
        prev?.next = prev?.next?.next

        // 반환시 맨 앞의 padding 노드를 제거
        return result?.next
    }
}
