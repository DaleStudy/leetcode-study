public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public void reorderList(ListNode head) {
        List<Integer> nArr = new ArrayList<>();
        Map<Integer, List<ListNode>> lMap = new HashMap<>();

        ListNode cur = head.next;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = null;
            nArr.add(cur.val);

            if (lMap.containsKey(cur.val)) {
                lMap.get(cur.val).add(cur);
            } else {
                List<ListNode> temp = new ArrayList<>();
                temp.add(cur);
                lMap.put(cur.val, temp);
            }

            cur = next;
        }

        int[] arr = nArr.stream().mapToInt(i -> i).toArray();
        int start = 0;
        int end = arr.length - 1;

        while (start < end) {
            head.next = lMap.get(arr[end]).remove(0);
            head = head.next;
            head.next = lMap.get(arr[start]).remove(0);
            head = head.next;

            start++;
            end--;
        }

        if (arr.length % 2 != 0) {
            for (int anInt : new ArrayList<>(lMap.keySet())) {
                List<ListNode> anArr = lMap.get(anInt);

                if (anArr.size() > 0) {
                    head.next = anArr.remove(0);
                }
            }
        }
    }
}

// NOTE: 동일한 val의 ListNode를 고려하지 못하여 틀린 경우
class WrongSolution {
    public void reorderList(ListNode head) {
        List<Integer> nArr = new ArrayList<>();
        Map<Integer, ListNode> lMap = new HashMap<>();

        ListNode cur = head.next;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = null;
            nArr.add(cur.val);
            lMap.put(cur.val, cur);
            cur = next;
        }

        int[] arr = nArr.stream().mapToInt(i -> i).toArray();
        int start = 0;
        int end = arr.length - 1;

        while (start < end) {
            head.next = lMap.remove(arr[end]);
            head = head.next;
            head.next = lMap.remove(arr[start]);
            head = head.next;

            start++;
            end--;
        }

        if (arr.length % 2 != 0) {
            for (int anInt : new ArrayList<>(lMap.keySet())) {
                head.next = lMap.remove(anInt);
            }
        }
    }
}
