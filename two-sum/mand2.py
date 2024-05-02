# 문제: https://leetcode.com/problems/two-sum/description/

# targetNum - list[i] 값이 list에 있는지 확인만 하면 끝. -> 이 아니고 i. j 리턴
def solutions(nums, target_num):
    table = {num: idx for idx, num in enumerate(nums)}

    for i, value in enumerate(nums):
        look = target_num - value
        print('look:', look)
        # value -> idx로 바로 치환하기가 어렵..
        if look in table and i != table[look]:
            look_idx = table[look]
            return [i, look_idx]


# 시간복잡도: O(n)
# 공간복잡도: O(n)

answer_1 = solutions([2, 7, 11, 15], 9)
answer_2 = solutions([3, 3], 6)  # 중복된수가나오면..?!?!?!?!
answer_3 = solutions([3, 2, 4], 6)

print(answer_1 == [0, 1])
print(answer_2 == [0, 1])
print(answer_3 == [1, 2])
