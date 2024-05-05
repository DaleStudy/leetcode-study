# 문제: https://leetcode.com/problems/valid-palindrome/description/

def solution(sentence):
    # removing all non-alphanumeric characters (숫자는 ㅇㅋ)
    selected = ''
    for s in sentence:
        if s.isalnum():
            selected += s.lower()
    return selected == selected[::-1]


# 시간복잡도: O(n)
# 공간복잡도: O(n)


answer_1 = solution("A man, a plan, a canal: Panama")
answer_2 = solution("0P")
answer_3 = solution("race a car")
answer_4 = solution(" ")
answer_5 = solution("a")

print(answer_1 is True)
print(answer_2 is False)
print(answer_3 is False)
print(answer_4 is True)
print(answer_5 is True)
