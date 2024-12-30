package leetcode_study

/*
* 오름차순으로 정렬된 두 노드 리스트를 크기 순서대로 병합하는 문제
* 기준 노드와 다음 노드를 가리키는 포인터 노드를 상용해 문제 해결
* 시간 복잡도: O(n)
* -> 주어진 두 노드 숫자만큼 순회
* 공간 복잡도: O(1)
* */
fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
    val resultNode = ListNode(0)
    var currentNode = resultNode

    var firstCurrentNode = list1
    var secondCurrentNode = list2

    while (firstCurrentNode != null && secondCurrentNode != null) {
        if (firstCurrentNode.value <= secondCurrentNode.value) {
            currentNode.next = ListNode(firstCurrentNode.value)
            firstCurrentNode = firstCurrentNode.next
        } else {
            currentNode.next = ListNode(secondCurrentNode.value)
            secondCurrentNode = secondCurrentNode.next
        }
        currentNode = currentNode.next!!
    }

    if (firstCurrentNode != null) {
        currentNode.next = firstCurrentNode
    } else if(secondCurrentNode != null) {
        currentNode.next = secondCurrentNode
    }
    return resultNode.next
}


class ListNode(
    var value: Int,
) {
    var next: ListNode? = null
}
