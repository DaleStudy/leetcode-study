// Integer.bitCount(i)는 O(log n) 이걸림 그래서 n번 반복하면 O(nlogn)
public static int[] countBits(int n) {
    int[] ans = new int[n + 1];
    
    for (int i = 0; i <= n; i++) {
        ans[i] = Integer.bitCount(i); 
    }
    
    return ans;
}
