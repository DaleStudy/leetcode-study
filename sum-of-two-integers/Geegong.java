public class Geegong {
    /**
     * XOR, AND 연산을 이용하여 계산
     * XOR : carry 확인하여 1비트씩 왼쪽으로 이동 (<<)
     * AND : carry 없이 더하기 결과값만 확인
     * time complexity : O(N)
     * space complexity : O(N)
     * @param a
     * @param b
     * @return
     */
    public int getSum(int a, int b) {
        int a_ = a;
        int b_ = b;

        while (a_ != 0) {
            int temp = a_;
            a_ = (a_ & b_) << 1;
            b_ = (temp ^ b_);
        }

        return b_;
    }

}
