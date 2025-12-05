class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var curOneNode = list1
        var curTwoNode = list2
        
        val resultStartNode = ListNode(999) 
        var resultCurNode = resultStartNode

        while (curOneNode != null && curTwoNode != null) {

            if (curOneNode.`val` <= curTwoNode.`val`) {
                resultCurNode.next = curOneNode
                curOneNode = curOneNode.next 
            } else {
                resultCurNode.next = curTwoNode
                curTwoNode = curTwoNode.next
            }
            
            resultCurNode = resultCurNode.next!!
        }

        if (curOneNode != null) {
            resultCurNode.next = curOneNode
        }
        if (curTwoNode != null) {
            resultCurNode.next = curTwoNode
        }

        return resultStartNode.next
    }
}