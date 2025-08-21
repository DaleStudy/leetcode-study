class Solution {
    func mergeTwoListsIterative(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        var iterList1 = list1
        var iterList2 = list2
        
        var dummy = ListNode()
        var merged = dummy
        
        while iterList1 != nil && iterList2 != nil,
              let list1 = iterList1,
              let list2 = iterList2 {
            if list1.val < list2.val {
                merged.next = list1
                iterList1 = list1.next
            } else {
                merged.next = list2
                iterList2 = list2.next
            }
            
            guard let next = merged.next else {
                break
            }
            
            merged = next
        }
        
        merged.next = iterList1 ?? iterList2

        return dummy.next
        
        //시간복잡도 O(m+n)
        //공간복잡도 O(1)
    }
    
    func mergeTwoListsRecursion(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        guard var list1 = list1 else {
            return list2
        }
        
        guard var list2 = list2 else {
            return list1
        }

        if list1.val < list2.val {
            list1.next = mergeTwoListsRecursion(list1.next, list2)
            return list1
        } else {
            list2.next = mergeTwoListsRecursion(list1, list2.next)
            return list2
        }
        
        //시간 복잡도 O(m+n)
        //공간 복잡도 O(m+n)
    }
}

