package leetcode_study

/*
* Node를 역순으로 만드는 문제
* 추가 저장 공간을 사용해 노드를 채워 둔 뒤 역행하면서 포인터 값을 변경하는 방법으로 해결
* 시간 복잡도: O(n)
* -> 새로운 공간에 값을 추가하는 반복문: O(n)
* -> 각 노드에 접근하여 포인터 값을 변경하는 반복문: O(n)
* 공간 복잡도: O(n)
* -> 주어진 노드를 저장할 수 있을만큼 저장 공간 필요: O(n)
* */
fun reverseList(head: ListNode?): ListNode? {
    val stack = mutableListOf<ListNode>()
    var currentNode = head
    if (head == null) return null

    while (currentNode != null) {
        stack.add(currentNode)
        currentNode = currentNode.next
    }


    for (i in stack.size - 1 downTo 1) {
        stack[i].next = stack[i-1]
    }
    stack[0].next = null
    return stack[stack.size -1]
}
