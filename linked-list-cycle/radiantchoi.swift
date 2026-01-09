/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

// 1차 버전: 문제의 constraint에 따라 1만 번의 traverse를 수행하는 답안 (통과는 됩니다)
class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        guard let head else { return false }

        return traverse(head, 0)
    }

    func traverse(_ node: ListNode?, _ currentIndex: Int) -> Bool {
        guard let node else { return false }
        guard currentIndex < 10000 else { return true }

        return traverse(node.next, currentIndex + 1)
    }
}

// LLM 첨삭 버전: Floyd's Cycle Detection Algorithm 사용
class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        guard let head else { return false }

        var slow: ListNode? = head
        var fast: ListNode? = head

        while true {
            // fast는 한 번에 두 칸씩 이동
            fast = fast?.next?.next
            
            // slow는 한 번에 한 칸씩 이동
            slow = slow?.next

            // fast나 slow가 nil이면 cycle이 없다
            if fast == nil || slow == nil { return false }
            
            // fast와 slow가 같은 노드를 가리키면 cycle이 있다
            // break로 마무리한 이유는, 그래서 그 만나는 노드가 어디인가? 라는 문제에 응용하기 위함
            if fast === slow { break }
        }
        
        // 사이클 시작 지점을 찾는 문제일 경우 여기에 entry 포인터 삽입 후 탐색

        return true
    }
}

/* 
사이클 시작 지점을 찾으시오, 라는 문제일 경우?
entry라는 별도의 포인터를 하나 더 둔 다음 slow와 함께 한 칸씩 이동시킨다.
두 포인터가 만나는 지점이 사이클 시작 지점!
이것이 가능한 이유는, 아래의 이동 거리 공식 때문에 그렇다.
        
L: 사이클 입구까지의 길이
C: 사이클 길이
d: 사이클 내에서, 사이클 종료(==시작)까지 남은 거리
        
fast의 이동 거리: L + n * C + d
slow의 이동 거리: L + d
        
fast의 이동 거리는 slow의 이동 거리의 2배이므로
2 * (L + d) = L + n * C + d
        
따라서, L = n * C - d 이다.
그리고 L은 entry 포인터가 이동해야 하는 거리이다.
n * C - d는 사이클 안에서는 C - d와 같다. fast 노드가 n번 돌았을 뿐, 사이클 안이었기 때문.
따라서 entry 포인터와 slow 포인터를 다시 한 칸씩 이동시키다 보면, 반드시 만나게 된다.
이 만나는 지점이 사이클 시작 지점.
*/