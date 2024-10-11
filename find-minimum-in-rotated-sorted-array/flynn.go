/*
풀이 1
- 주어진 배열을 두 부분으로 나눌 수 있기 때문에 이진탐색을 이용하여 풀이할 수 있습니다
  주어진 배열이 A = [4,5,6,7,0,1,2] 라고 할 때, 이 배열은 두 부분으로 나눌 수 있습니다
    A[0:3] : rotate되어 앞으로 배열의 앞으로 옮겨진 부분
	A[4:6] : rotate되어 배열의 뒤로 밀려난 부분
  이걸 조금 다르게 표현하면 이렇게도 바라볼 수 있습니다
  f(A) = [T, T, T, T, F, F, F] (T/F: rotate되어 배열의 앞으로 옮겨진 부분인가?)

  이 때, 우리가 찾는 값 (the Minimum in the rotated sorted array)는 두 구간의 경계에 위치하고 있습니다
  즉, 첫번째 F의 위치를 찾는 문제로 바꿔 생각할 수 있단 뜻입니다

Big O
- N: 주어진 배열 nums의 길이

- Time complexity: O(logN)
- Space complexity: O(1)
*/

func findMin(nums []int) int {
	lo, hi := 0, len(nums)-1
	// rotate가 0번 실행된 경우, 이진탐색을 실행할 필요가 없고 이진탐색의 초기값 설정이 까다로워지기 때문에 처음에 따로 처리해줍니다
	// 앞서 hi의 초기값을 설정할 때, len(nums)가 아닌 len(nums) - 1로 설정할 수 있었던 이유이기도 합니다
	if nums[lo] < nums[hi] {
		return nums[lo]
	}

	// Go는 while문에 대응하는 표현을 for로 이렇게 표현합니다
	for lo < hi {
		mid := lo + (hi-lo)/2

		// 만일 mid가 앞으로 밀려난 부분에 속한다면...
		if nums[lo] <= nums[mid] && nums[mid] > nums[hi] {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return nums[lo]
}

/*
풀이 2
- 풀이 1에서 덜어낼 수 있는 로직을 덜어낸 좀 더 깔끔한 이진탐색 풀이입니다

Big O
- 풀이 1과 동일
*/

func findMin(nums []int) int {
    lo, hi := 0, len(nums)

    for lo < hi {
        mid := lo+(hi-lo)/2

        if nums[mid] > nums[len(nums)-1] {
            lo = mid + 1
        } else {
            hi = mid
        }
    }

    return nums[lo]
}
