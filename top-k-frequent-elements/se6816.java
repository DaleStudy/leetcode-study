/**
Problem 347 : Top K Frequent Elements
Summary : 
- Map을 통해 숫자의 중복 횟수를 구한다.
- 배열을 통해, 중복 횟수를 인덱스로 해당 숫자를 연결 리스트를 통해 값을 저장한다.
- 중복 횟수를 저장한 배열에서 마지막 인덱스부터 for문을 돌리면서 k개까지 리턴 배열에 숫자를 저장한다.
- 제약 조건에서 응답이 유일하다는 것을 보장하고 있으므로, 개수가 부족하거나, 중복에 대해서는 고려하지 않아도 된다.
- 정렬을 이용하면 최소한 시간복잡도가 O(NlogN)이지만 해당 방법은 O(N)이 가능하다.

*/

class Solution {
    class Node {
        int num;
        Node next;
        public Node(int n){
            num = n;
        }
    }
    class NodeList {
        Node head;
        Node tail;

        public NodeList() {
        }

        public void add(Node node){
            if(head == null){
                head = node;
                tail = node;
                return;
            }

            tail.next = node;
            tail = tail.next;
        }

        public boolean empty() {
            return head == null;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        NodeList[] list = new NodeList[nums.length+1];
        int[] result = new int[k];
        Map<Integer, Integer> map= new HashMap<>();

        for(int i=0; i < list.length; i++) {
            list[i] = new NodeList();
        }

        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            list[entry.getValue()].add(new Node(entry.getKey()));
        }

        int idx = 0;
        for(int i=list.length-1; (i >= 0) && (idx < k); i--) {
            if(!list[i].empty()) {
                Node head = list[i].head;
                while(head != null) {
                    result[idx] = head.num;
                    head = head.next;
                    idx++;
                }
            }
        }
        return result;
    }
}
