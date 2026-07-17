class Solution {
    public int hammingWeight(int n) {
        // 이진수로 바꾸고, 1 이 몇개 있는 지 파악한다.
        return Integer.bitCount(n);

        // 추가 풀이.
        // String ans = Integer.toBinaryString(n).replace("0","");
        // return ans.length();
    }
}

