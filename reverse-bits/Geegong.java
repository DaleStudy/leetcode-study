public class Geegong {

    /**
     * time complexity : O(1)
     * space complexity : O(1)
     * @param n
     * @return
     */
    public int reverseBits(int n) {

        // 32bit 만큼 움직인다.
//        for (int index=32; index > 0; index--) {
//            // 맨 오른쪽 1bit만 꺼낸다
//            int lastOneBit = n & 1;
//            // 그런데!! 시프트연산이 하위 5비트까지 밖에 안되서ㅠㅠ << 32 가 아니가 << 0 으로 되어버림
//            int temp = lastOneBit << index;
//            result = result | temp;
//            n = n >>> 1;
//        }

        int result = 0;
        // 시프트 연산을 1비트씩 움직이는걸로 변경해야 한다
        for (int index=1; index <= 32; index++) {
            // 마지막 1비트를 추출하고 그걸 result 에서 왼쪽으로 1비트 시프트한걸 합쳐야 한다.
            // 0001 -> 0010 -> 0100 -> .... 요렇게
            result = (n & 1) | (result << 1);
            n = n >>> 1;
        }

        return result;
    }

}



