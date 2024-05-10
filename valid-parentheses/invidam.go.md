# Intuition
스택을 이용하여 이전에 등장한 여는 괄호를 판단한다.

# Approach
<!-- Describe your approach to solving the problem. -->
1. 기존에 이미 알고있던 문제라서 스택을 이용한 풀이가 떠올랐다.
2. 스택을 구현하기에 귀찮음이 있어 등장한 괄호의 빈도를 저장하면 어떨까 싶었다. (관련 문제가 생각났다.)
3. 2번의 경우 여러 종류를 대응할 수 없어 (등장 빈도는 같지만 순서가다른 `([{]})` 같은 경우) 스택을 이용해 해결했다.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(n은 문자열의 길이)
# Code
```


type Stack[T any] struct {
	Data  []T
	Index int
}

func CreateStack[T any](capacity int) Stack[T] {
	return Stack[T]{Data: make([]T, 0, capacity), Index: 0}
}

// Push adds an element to the queue, expanding it if necessary.
func (q *Stack[T]) Push(value T) {
	if q.Index >= len(q.Data) {
		q.Data = append(q.Data, value)
	} else {
		q.Data[q.Index] = value
	}
	q.Index++
}

func (q *Stack[T]) Pop() T {
	if q.Index-1 < 0 {
		panic("Stack is empty")
	}
	element := q.Data[q.Index-1]
	q.Index--
	return element
}

func (q *Stack[T]) Peek() T {
	if q.Index-1 < 0 {
		panic("Stack is empty")
	}
	return q.Data[q.Index-1]
}

func (q *Stack[T]) Size() int {
	return q.Index
}

func getOpenBracket(close rune) uint8 {
	opens := "([{"
	closes := ")]}"

	for i, ch := range closes {
		if ch == close {
			return opens[i]
		}
	}

	return ' '
}
func isValid(s string) bool {
	opens := "([{"

	savedStack := CreateStack[uint8](len(s))

	for _, ch := range s {
		if strings.ContainsRune(opens, ch) {
			savedStack.Push(uint8(ch))
			continue
		}

		if savedStack.Size() == 0 {
			return false
		}

		open := getOpenBracket(ch)
		if savedStack.Peek() != open {
			return false
		}
		savedStack.Pop()
	}

	return savedStack.Size() == 0
}

```

# Learned
- append, copy 등의 내장 함수: append는 배열 용량 초과시 resize까지 진행하며, resize의 크기는 os에 따라 다르다.
- mapping을 간단히 하는 방법.: 기존에는 배열을 이용하여 매핑했으나, hash map을 이용하는 게 직관적이라 느꼈다.
- 제너릭 활용: Go의 `type parameter`는 다른 언어(e.g. `Java`)의 제너릭과 인터페이스(다형성 활용)의 교집합 느낌이다.
- Go에서 문자를 처리하는 방법: 어디서는 `rune`이고 어디선 `uint8`이다.