class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

"""
================================================================================
풀이 과정 - 09:43 시작 ~ 풀이 과정 떠올리지 못함
================================================================================

1. 정수 배열 nums가 주어짐
2. 배열 answer를 반환해야 하는데
3. answer[i]는 nums의 모든 요소의 곱과 같다 (nums[i]를 제외한)
4. O(n) 시간에 실행되는 알고리즘을 작성해야하고, 나누기 연산을 사용해서는 안된다
5. 나누기 연산을 어떻게 이용 안하고 풀지?

────────────────────────────────────────────────────────────────────────────────
6. Claude 도움 → answer[i] = (i 왼쪽의 곱) * (i 오른쪽의 곱)


[1차 시도] 왼쪽/오른쪽 곱 배열 사용
────────────────────────────────────────────────────────────────────────────────
7. 각 위치의 왼쪽 누적곱과 오른쪽 누적곱을 미리 계산
8. left[i] = nums[0] * ... * nums[i-1]
9. right[i] = nums[i+1] * ... * nums[n-1]
10. answer[i] = left[i] * right[i]

        n = len(nums)
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        right = [1] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        return [left[i] * right[i] for i in range(n)]

11. 정상적으로 통과되는 것 확인 완료


[2차 개선] 공간 복잡도 최적화
────────────────────────────────────────────────────────────────────────────────
12. left, right 배열을 따로 만들면 O(n) 공간 복잡도 추가 사용
13. answer 배열을 재활용하면 추가 공간 없이 해결 가능
14. 첫 번째 순회: answer에 왼쪽 누적곱 저장
15. 두 번째 순회: answer에 오른쪽 누적곱을 곱하면서 최종 결과 완성

        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

16. 추가 공간 복잡도 O(n) → O(1)로 개선 완료 (answer 배열 제외)
17. 최종 통과 확인 완료


[문제 복기] 패턴 발견 과정
────────────────────────────────────────────────────────────────────────────────
- 문제를 다시 복기해보면
- 각 위치에서 자기 자신을 제외한 모든 원소의 곱을 구해야함
- 제약을 무시하면 이중 반복문 Brute Force로 풀 수 있음
- 제약을 무시하면 나눗셈을 이용해서도 풀 수 있음
- 나눗셈도 금지되고 O(n) 시간에 풀어야한다면?
- "제외한다"를 어떻게 표현해주면 좋을까? (이 부분이 핵심)

작은 예시로 패턴 찾기:
    nums = [2, 3, 4]

    answer[0] = 3 * 4 = 12
    answer[1] = 2 * 4 = 8
    answer[2] = 2 * 3 = 6

    answer[0] = (없음) * (3 * 4) = 12
    answer[1] = (2) * (4) = 8
    answer[2] = (2 * 3) * (없음) = 6

- 패턴 발견 → 왼쪽 부분 * 오른쪽 부분
- 해법 도출 → 왼쪽 부분의 모든 곱 * 오른쪽 부분의 모든 곱

패턴을 일반화하는 과정이 필요:
    answer[i] = nums[0] * ... * nums[i-1] * nums[i+1] * ... * nums[n-1]
    left[i] = nums[0] * ... * nums[i-1]
    right[i] = nums[i+1] * ... * nums[n-1]
    answer[i] = left[i] * right[i]

점화식 찾는데, DP적 사고 필요:
    왼쪽 누적곱:
        left[1] = nums[0]
        left[2] = nums[0] * nums[1] = left[1] * nums[1]
        left[3] = nums[0] * nums[1] * nums[2] = left[2] * nums[2]
        → left[i] = left[i-1] * nums[i-1]

    오른쪽 누적곱:
        right[2] = nums[3]
        right[1] = nums[3] * nums[2] = right[2] * nums[2]
        right[0] = nums[3] * nums[2] * nums[1] = right[1] * nums[1]
        → right[i] = right[i+1] * nums[i+1]

관련해서 코드로 구현하는 과정이 필요함
"""
