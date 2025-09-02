import java.util.ArrayList;
import java.util.List;

/**
 * 가장 먼저 들었던 의문은 왜 dp가 2차원 배열이 아닐까? 였지만,
 * dp를 2차원 자료구조로 선언하는 경우는 경로 저장이나 상태 전이가 2개 이상의 조건에 따라 나눠질 때인데
 * 이 문제는 1차원으로 해결이 가능한 문제입니다. 가장 중요한 건 “마지막 원소 위치 i”라는 하나의 상태입니다.
 *
 * LIS = "주어진 수열에서 순서를 지키면서 고를 수 있는 원소 중, 값이 점점 커지도록 선택했을 때 만들 수 있는 가장 긴 부분 수열."
 * brute force로 이중 for문을 사용하는 것은 비효율적입니다. 그래서 for문 + BS를 곁들였습니다.
 *
 * Arrays.binarySearch()는 정렬된 배열에서만 동작하므로 이 문제의 테스트 케이스에 맞지 않습니다.
 *
 * 신규 메서드: Collections.binarySearch()
 * List 안의 요소들에 대해서 이분 탐색을 해서 해당 index를 반환합니다. (없을 경우 -1)
 * 단, list 안의 요소들은 정렬되어 있어야 합니다 (이분 탐색의 기본 조건처럼)
 * 신규 메서드 혹은 직접적으로 binarySearch() 메서드를 구현해도 됩니다. 다만 원본 nums를 이분 탐색하는 것이 아니며
 * 직관적으로 개념을 이해하기 위해서 간편한 메서드 방식인 Collections.binarySearch()를 사용했습니다.
 *
 *
 * [테스트 케이스 과정 출력]
 * 0
 * [10]
 * 0
 * [9]
 * 0
 * [2]
 * 1
 * [2, 5]
 * 1
 * [2, 3]
 * 2
 * [2, 3, 7]
 * 3
 * [2, 3, 7, 101]
 * 3
 * [2, 3, 7, 18]
 */
import java.util.*;

class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> tails = new ArrayList<>(); // 길이 k인 증가 수열의 "꼬리 최솟값"들

        for (int x : nums) {
            int idx = Collections.binarySearch(tails, x);
            // 해당 x 숫자를 찾지 못하면 -1을 반환하면 이는 list에서 범위에 벗어나기 때문에
            // 음수면 삽입 위치로 변환해서 범위 예외를 처리해야 합니다.
            if (idx < 0) idx = -(idx + 1);

            // 중요 연산은 더하기와 교체입니다.
            // 가장 크다는 것: 주어진 인덱스와 꼬리 리스트의 길이가 같다. -> 새 subsequence가 생깁니다.
            // 그렇지 않다는 것은 최댓값보다 더 작은 값이 있다는 것, 그 자리를 주어진 x로 교체한다.
            // 결론: 가장 크면 add, 그 외에는 인덱스 자리를 x로 교체
            if (idx == tails.size()) {
                tails.add(x);                // 가장 크면 뒤에 추가 → 길이 +1
            } else {
                tails.set(idx, x);           // 아니면 그 자리의 꼬리를 더 작은 x로 교체
            }
        }
        return tails.size(); // 꼬리 리스트 길이 = LIS 길이
    }
}
