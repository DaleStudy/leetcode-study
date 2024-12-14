/*
Runtime: 10 ms(Beats: 95.83 %)
Time Complexity: O(nlogn)
- map에 item 추가 : O(n)
- items 배열 정렬 : O(nlogn)
- result 배열에 원소 추가 : O(n)

Memory: 49.50 MB(Beats: 6.84 %)
Space Complexity: O(n)
- map : O(n)
- items : O(n)
- result : O(n)
*/

class Solution {
    class Item {
        int val;
        int cnt;

        public Item(int val, int cnt) {
            this.val = val;
            this.cnt = cnt;
        }

        public void plusOne() {
            this.cnt += 1;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Item> map = new HashMap<>();
        for (int num : nums) {
            Item item = map.get(num);
            if (item == null) {
                item = new Item(num, 1);
                map.put(num, item);
            } else {
                item.plusOne();
            }
        }

        ArrayList<Item> items = new ArrayList<>(map.values());
        Collections.sort(items, (item1, item2) -> Integer.compare(item2.cnt, item1.cnt));

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = items.get(i).val;
        }

        return result;
    }
}
