public class Geegong {

    /**
     * leftIdx, rightIdx 를 둬서 왼족 인덱스를 기준으로 오른쪽 인덱스를 움직여가며 palindromic string 을 찾아간다
     * time complexity : O(N^2)
     * space complexity : O(1)
     * @param s
     * @return
     */
    public int countSubstrings(String s) {
        int count = 0;
        char[] sArray = s.toCharArray();


        for (int leftIdx = 0; leftIdx < sArray.length; leftIdx++) {
            int rightIdx = leftIdx + 1;

            // 한글자씩 따졌을 때 palindrome
            count++;
            while(leftIdx <= rightIdx && rightIdx < sArray.length) {
                int offset = rightIdx - leftIdx;
                boolean isEqual = sArray[leftIdx] == sArray[rightIdx];

                if (!isEqual) {
                    rightIdx++;
                    continue;
                }

                if (offset == 1 && isEqual) {
                    count++;
                    rightIdx++;

                } else { // isEqual 이고 offset > 1인 케이스
                    // 서로 조여가면서 palindrome 인지 체크
                    count += isPalindromic(sArray, leftIdx + 1, rightIdx - 1);
                    rightIdx++;
                }
            }
        }

        return count;

    }

    public int isPalindromic(char[] origin, int leftIdx, int rightIdx) {
        // 서로 조여가면서 palindrome 인지 체크
        while (leftIdx < rightIdx) {
            if (origin[leftIdx] == origin[rightIdx]) {
                leftIdx++;
                rightIdx--;
                continue;
            }

            return 0;
        }

        return 1;
    }

}


