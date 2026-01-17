public class Geegong {

    /**
     * two pointer 를 사용, 처음에는 height 배열을 정렬해서 높은 순오르 최대 면적을 구하는건가 싶었지만 그럴 필요는 없었음
     * (어차피 모든 원소를 돌아야되기 때문에 소팅의 의미가 없음, 그리고 NLogN 시간 복잡도가 생겨서 더 좋지 않음)
     * time complexity : O(N)
     * space complexity : O(N)
     *
     * @param height
     * @return
     */
    public int maxArea(int[] height) {


        int leftIdx=0;
        int rightIdx = height.length - 1;
        int maxVolume = 0;

        while(leftIdx < rightIdx) {

            int leftHeight = height[leftIdx];
            int rightHeight = height[rightIdx];
            int gap = rightIdx - leftIdx;
            int currentVolume = gap * Math.min(leftHeight, rightHeight);
            maxVolume = Math.max(currentVolume, maxVolume);

            if (leftHeight > rightHeight) {
                rightIdx--;
            } else {
                leftIdx++;
            }

        }

        return maxVolume;








////////// 아래 부분은 예전 기수에서 풀었던 방법
//        int leftIndex = 0;
//        int rightIndex = height.length - 1;
//
//        int maxAmount = 0;
//        int currentAmount = 0;
//
//        while(leftIndex != rightIndex && leftIndex < rightIndex) {
//            // 면적을 먼저 구해본다.
//            int minHeight = Math.min(height[leftIndex], height[rightIndex]);
//            currentAmount = minHeight * (rightIndex - leftIndex);
//
//            maxAmount = Math.max(currentAmount, maxAmount);
//            // 어느 포인터를 움직일지 결정
//            /**
//             * case 1. 단순히 전체를 모두 훑어버리면 Time limit exceeded 발생
//             */
////            if (leftIndex < rightIndex - 1) {
////                rightIndex--;
////            } else if (leftIndex == rightIndex - 1) {
////                rightIndex = height.length - 1;
////                leftIndex++;
////            }
//
//            /**
//             * case 2. 포인터가 돌면서 높은 height만 고려해서 포인터가 움직일 때에는 Time limit exceeded 발생 X
//             */
//            if (height[leftIndex] < height[rightIndex]) {
//                leftIndex++;
//            } else if (height[leftIndex] > height[rightIndex]) {
//                rightIndex--;
//            } else {
//                rightIndex--;
//                leftIndex++;
//            }
//        }
//
//        return maxAmount;
    }
}

