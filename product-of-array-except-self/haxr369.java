import java.util.HashMap;
import java.util.Map;

class Solution {
  /**
   * 풀이요약: 범위를 반씩 나누며 곱을 캐싱하고, 제외할 인덱스만 골라 탐색하는 분할 정복 기반 배타 곱 계산
   * 
   * 
   * 풀이결과:
   * 
   * Runtime: 872 ms (Beats 3.62%)
   * Memory: 137.29 MB (Beats 5.61%)
   * Space Complexity: O(NlogN)
   * - 길이 N인 배열을 절반씩 자른 범위 안에 수들을 곱한 값을 저장 O(NlogN)
   * - 길이 N인 출력 배열 생성 O(N)
   * > O(N) + O(NlogN) > O(NlogN)
   * 
   * Time Complexity: O(NlogN)
   * - 길이 N인 배열을 절반씩 잘라가면서 안에 수들을 곱하기 O(NlogN)
   * - 0~N 범위를 절반씩 잘라가면서 i가 포함되지 않은 범위 수를 곱하기 O(logN)
   * - N개의 숫자에 대해서 찾기 => O(NlogN)
   * > O(NlogN) + O(NlogN) > O(NlogN)
   */
  public int[] productExceptSelf1(int[] nums) {
    Map<String, Integer> mp = new HashMap<>();
    fndRngMul(mp, nums, 0, nums.length);
    int[] ans = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
      int val = binaryFnd(mp, i, 0, nums.length);
      ans[i] = val;
    }

    return ans;
  }

  /***
   * 특정 idx를 제외한 구간 곱을 재귀적으로 찾는다.
   * 
   * - 범위가 단일 원소면 곱에 포함될 값이 없으므로 1 반환
   * - 범위를 반으로 자르고, idx가 속하지 않은 부분의 곱을 즉시 사용
   * - idx가 속한 쪽은 계속 재귀 탐색
   */
  private int binaryFnd(Map<String, Integer> mp, int idx, int str, int end) {
    int val = 1;

    if (end - str == 1) {
      return val;
    }

    int mid = (str + end) / 2;
    String leftKey = str + "_" + mid;
    String rightKey = mid + "_" + end;
    // System.out.println("----idx->"+idx+" mid->"+mid);
    // idx는 좌측에 위치하기 때문에 우측 값을 곱함.
    if (idx < mid) {
      // 하지만 다은 idx가 포함된 범위를 탐색
      int leftVal = binaryFnd(mp, idx, str, mid);
      // System.out.println(". ----leftVal->"+leftVal+" base->"+mp.get(rightKey)+"
      // val-> "+val);
      val = mp.get(rightKey) * leftVal;
    } else { // idx는 우측에 위치하기 때문에 좌측 값을 곱함.
      int rightVal = binaryFnd(mp, idx, mid, end);
      // System.out.println(". ----rightVal->"+rightVal+" base->"+mp.get(leftKey)+"
      // val-> "+val);
      val = mp.get(leftKey) * rightVal;
    }
    return val;
  }

  /**
   * 배열의 범위 [str, end) 내 값들의 곱을 구해 캐싱한다.
   * 
   * - 원소가 하나만 있는 구간이면 nums[str] 저장
   * - 구간을 반으로 나누어 왼쪽/오른쪽 곱을 재귀적으로 계산
   * - 전체 구간이 아니라면 left * right 를 캐싱
   * - 전체 구간(0~N)은 제외 곱 계산 시 무시해야 하므로 '1' 저장
   */
  private int fndRngMul(Map<String, Integer> mp, int[] nums, int str, int end) {
    String k = str + "_" + end;

    if (end - str == 1) {
      // System.out.println("put k->"+k+" v->"+v);
      mp.put(k, nums[str]);
      return nums[str];
    }
    int mid = (str + end) / 2;
    int leftRngMul = fndRngMul(mp, nums, str, mid);
    int rightRngMul = fndRngMul(mp, nums, mid, end);

    int v = 1;
    // 전체 곱은 구하지 않음.
    if (str == 0 && end == nums.length) {
      v = 1;
    } else {
      v = leftRngMul * rightRngMul;
    }
    mp.put(k, v);
    // System.out.println("put2 k->"+k+" v->"+v);
    return v;
  }
}