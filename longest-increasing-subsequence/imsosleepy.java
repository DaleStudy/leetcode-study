// 이진 트리로 값을 변경해가면서 해결하면된다.
// 기존에 있던 노드에 위치한 값보다 작은 값이 등장하면 값이 치환된다는 개념만 이해하면 쉽다.
// 자바에서는 콜렉션에서 바이너리 서치를 제공해서 편하게 구현가능
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> sub = new ArrayList<>();

        for (int num : nums) {
            int pos = Collections.binarySearch(sub, num);
            if (pos < 0) {
                pos = -(pos + 1);
            }
            if (pos < sub.size()) {
                sub.set(pos, num);
            } else {
                sub.add(num);
            }
        }
        return sub.size();
    }
}
