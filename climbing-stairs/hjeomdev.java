class Solution {
    List<Integer> list = new ArrayList<>();
    public int climbStairs(int n) {
        list.add(0);
        list.add(1);
        list.add(2);
        return step(n);
    }

    public int step(int n) {
        if (list.size() > n && list.get(n) != null) {
            return list.get(n);
        }
        int result = step(n - 1) + step(n - 2);
        list.add(result);
        return result;
    }
}
