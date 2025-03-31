package leetcode_study

/*
* 끝에서 n 번째 노드를 제거하는 문제
* 예외 상황이 발생하는 Case를 나눠 문제 해결
* 시간 복잡도 : O(n)
* -> node list를 순회하며 배열에 담는 과정
* 공간 복잡도 : O(n)
* -> 각 node를 담을 list 공간
* */
fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
    val tempNodeList = mutableListOf<ListNode>()
    var currentHead = head
    while (currentHead != null) {
        tempNodeList.add(currentHead)
        currentHead = currentHead.next
    }

    val preIndex = tempNodeList.size - n - 1
    val postIndex = tempNodeList.size - n + 1

    if (preIndex < 0) {
        if (tempNodeList.size == 1) {
            return null
        }
        return tempNodeList[postIndex]
    } else if (postIndex == tempNodeList.size) {
        tempNodeList[preIndex].next = null
        return head
    } else {
        tempNodeList[preIndex].next = tempNodeList[postIndex]
    }
    return head
}
