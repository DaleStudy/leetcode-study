/**
 * [풀이 개요]
 * - 시간복잡도 : O(log n)
 * - 공간복잡도 : O(1)
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - 정렬된 배열이 시프트 된 형태로 주어짐. 그러니까 원래는 오름차순 정렬임
     * - 이때 최소 값을 찾아야 함
     * - 반씩 나누어 탐색하는 이분 탐색 형태로 시간복잡도는 O(log n)
     * - 별도로 유의미한 공간 할당을 하지 않으므로 공간복잡도는 O(1)
     */
    public int findMin(int[] nums) {
        int len = nums.length - 1;
        // 중간 지점은 전체 갯 수를 2로 나눈 수로 함. 배열의 크기는 1 이상 5000 이하 이므로 int 커버 됨.
        
        int left = 0;
        int right = len;
        
        while(left < right) {
            int mid = (left + right) / 2;
            if(nums[mid] < nums[right]) { // mid 우측은 살펴볼 필요가 없음
                right = mid; // mid가 최소값일 가능성 있음
            } else {
                // nums[mid] > nums[right] // mid 좌측은 살펴볼 필요가 없음
                left = mid + 1 ; // mid가 최소 값일 가능성 없음
            }
        }
        return nums[left];
    }
}