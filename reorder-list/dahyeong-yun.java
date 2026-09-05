/**
 * TC : O(n)
 *   - 배열을 한 번 순회하면서 합을 구하기 때문에 O(n)
 * SC : O(n)
 *   - ArrayList가 노드 전체의 길이 n만큼 할당되기 때문에 O(n)
 */
class Solution {
    public void reorderList(ListNode head) {
        List<ListNode> nodes = new ArrayList<>();
        for (ListNode cur = head; cur != null; cur = cur.next)
            nodes.add(cur);

        int i = 0;
        int j = nodes.size() - 1;

        while (i < j) {
            nodes.get(i).next = nodes.get(j);
            i++;
            if (i == j) break; 
            nodes.get(j).next = nodes.get(i);
            j--;
        }

        nodes.get(j).next = null;
    }
}
