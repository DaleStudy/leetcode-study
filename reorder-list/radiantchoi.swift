// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    // [최초 풀이]
    // - 시간 복잡도: O(N)
    // - 공간 복잡도: O(N) (별도의 리스트 생성)
    // - 전략: 뒤집어진 리스트를 새로 만들고(Deep Copy), 하나씩 꺼내서 기존 리스트의 사이사이에 끼워 넣는다.
    func reorderList(_ head: ListNode?) {
        var rev: ListNode? = nil
        var tracker = head
        var threshold = 0

        // 뒤집어진 리스트 만들기 (메모리 추가 사용)
        while let point = tracker {
            let temp = rev
            rev = ListNode(point.val)
            rev?.next = temp
            threshold += 1

            tracker = tracker?.next
        }

        var head = head
        threshold -= 1

        // 뒤집어진 리스트의 노드 값을 이용해 새로운 노드를 만들어, 사이사이에 삽입
        while head != nil && threshold > 0 {
            let temp = head?.next
            let newNode = ListNode(rev!.val)
            head?.next = newNode
            head = head?.next
            threshold -= 1

            guard threshold > 0 else {
                head?.next = nil
                break
            }

            head?.next = temp
            head = head?.next
            rev = rev?.next
            threshold -= 1

            guard threshold > 0 else {
                head?.next = nil
                break
            }
        }
    }
    
    // [개선된 풀이]
    // - 시간 복잡도: O(N)
    // - 공간 복잡도: O(1) (In-place 조작)
    // - 전략: Slow & Fast Pointer로 중간을 찾고, 뒷부분만 뒤집은 뒤 병합한다.
    func reorderList2(_ head: ListNode?) {
        // 예외 처리: 노드가 0개, 1개, 2개일 때는 재배열 불필요
        guard head != nil, head?.next != nil else { return }

        var slow = head
        var fast = head

        // 1. 중간 지점 찾기 (Slow & Fast Runner)
        // fast는 2칸씩 가므로, fast가 끝에 닿으면 slow는 정확히 중간에 위치함.
        // (홀수 개일 땐 정중앙, 짝수 개일 땐 n/2번째 노드)
        while fast?.next != nil && fast?.next?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }

        // 2. 리스트 분리 및 뒷부분 뒤집기 (Reverse Linked List)
        var current = slow?.next
        slow?.next = nil // 앞부분 리스트의 끝을 nil로 막아줌 (완전 분리)
        var rev: ListNode? = nil

        while current != nil {
            let temp = current?.next // Save: 다음 이동할 곳 기억
            current?.next = rev      // Cut & Attach: 방향을 뒤로 돌림 (기존 연결 끊김)
            rev = current            // Move: rev(헤드)를 현재로 당겨옴
            current = temp           // Move: 다음 노드로 전진
        }

        // 3. 두 리스트 병합하기 (Merge)
        var first = head
        var second = rev

        // 리스트 다루기의 대원칙 (Merge 과정)
        // 1. [Save] 노드 뭉치의 next(다음 갈 곳)를 임시 변수에 저장
        // 2. [Cut & Attach] 노드의 next를 새로운 대상에 연결
        //    (Tip: 굳이 nil로 끊었다가 다시 붙일 필요 없이, 덮어쓰면 기존 연결은 자동으로 끊어짐)
        // 3. [Move] 기준 포인터를 저장해둔 next 위치로 이동
        while second != nil {
            let firstTemp = first?.next   // 1. Save
            let secondTemp = second?.next // 1. Save

            first?.next = second          // 2. Cut & Attach (first가 second를 가리킴)
            second?.next = firstTemp      // 2. Cut & Attach (second가 원래 first의 다음을 가리킴)

            first = firstTemp             // 3. Move
            second = secondTemp           // 3. Move
        }
    }
}
