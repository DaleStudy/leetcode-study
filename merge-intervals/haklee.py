"""TC: O(l * i + n), SC: O(n)

※ 쉬운 길을 돌아가는 풀이라는 것을 감안하고 읽어야 한다!!!
※ 구간의 끝 값이 10^4라고 되어있는 것을 보고 효율 안 따지고 냅다 아래의 방법으로 접근해보았다.

n은 전체 구간의 끝 값. 문제에서는 10^4으로 주어져 있다. (구체적으로는, 구간의 시작과 끝이 [0, 10^4] 구간에 존재)
i는 전체 인터벌의 개수. 문제에서는 10^4으로 주어져 있다.
l은 각 인터벌의 크기. 문제에서는 10^4으로 주어져 있다.

아이디어:
- n칸 짜리 일직선으로 되어있는 벽이 있다고 하자. 이 벽에는 아무런 칠이 되어있지 않다.
    - [0, 0, ..., 0] 리스트라고 생각하자.
- 모든 인터벌을 순회하면서 인터벌의 시작, 끝 값을 활용하여 이 벽의 일정 구간에 페인트를 칠한다고 하자.
    - 특정 구간의 값을 1로 바꾼다.
    - [0, ..., 0, 1, ..., 1, 0, ..., 0]
                  ^       ^
                  s     e - 1
- 페인트 칠이 끝났으면 벽의 시작부터 끝까지 훑으면서 칠해진 구간을 찾아내어 결과로 리턴한다.

SC:
- 벽을 길이 n짜리 리스트로 관리. O(n).
- 페인트 칠이 완료된 벽에서 구간을 찾을때 구간의 시작, 끝 인덱스를 관리하는 값에서 O(1).
- 종합하면 O(n).

TC:
- 각 인터벌을 순회할 때마다 벽 리스트에서 최대 l개의 아이템에 접근해서 값을 1로 바꾼다. O(l).
- 위의 작업을 인터벌 개수 만큼 진행. 여기까지 O(l * i).
- 페인트 칠이 끝난 벽을 순회하며 인터벌 추출. O(n).
- 종합하면 O(l * i + n).
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_v = int(1e4 + 2)
        flags = [False] * max_v

        for i in intervals:
            for v in range(i[0], i[1] + 1):
                flags[v] = True

        res = []

        make_interval = False
        int_s, int_e = -1, -1

        for i in range(max_v):
            if flags[i]:
                # 인터벌에 포함되어야 하는 값
                if not make_interval:
                    # 인터벌의 시작 값이다. 인터벌 시작을 i로 세팅.
                    make_interval = True
                    int_s = i
                else:
                    # 인터벌에 포함된 값이다. 인터벌 끝을 i로 세팅.
                    int_e = i
            else:
                # 인터벌에 포함 안되는 값
                if make_interval:
                    # 직전 값까지는 인터벌에 포함되었으므로, i에서
                    # 인터벌이 끝났다. 인터벌을 더해줌.
                    res.append([int_s, int_e])
                    make_interval = False

        return res


"""
그런데 위의 코드를 제출하면 오답이라고 나온다. 왜냐하면, 문제 조건상 인터벌의 s와 e값이 같을 수 있고,
따라서 길이 0짜리 구간이 존재할 수 있기 때문!!!!! (길이 0짜리 인터벌이라니... 분노를 금할 수 없다.)
그래서 위에서 벽에 페인트를 칠하는 비유로는 설명이 불가능한 이상한 인터벌도 결과에 포함시켜서 리턴해야 한다.
이를 위해서 별도의 처리를 한 것이 아래의 코드다. 추가된 코드를 보기 편하게 하기 위해 한글 변수명을 활용했다.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_v = int(1e4 + 2)
        flags = [False] * max_v
        억까 = []

        for i in intervals:
            for v in range(i[0], i[1]):
                flags[v] = True
            if i[0] == i[1]:
                억까.append(i[0])

        억까 = list(set(억까))
        억까.sort()

        res = []

        make_interval = False
        int_s, int_e = -2, -2
        억까_ind = 0

        for i in range(max_v):
            if flags[i]:
                # 인터벌에 포함되어야 하는 값
                if not make_interval:
                    # 길이가 있는 인터벌 앞에 오는 길이 0짜리 인터벌들을 추가해주자.
                    while 억까_ind < len(억까) and (v := 억까[억까_ind]) <= i:
                        if int_e + 1 < v:
                            # 직전에 결과에 추가한 인터벌의 끝 값보다는 커야 한다.
                            if v < i:
                                res.append([v, v])
                        억까_ind += 1

                    # 인터벌의 시작 값이다. 인터벌의 시작과 끝을 i로 세팅.
                    make_interval = True
                    int_s = int_e = i

                else:
                    # 인터벌에 포함된 값이다. 인터벌 끝을 i로 세팅.
                    int_e = i
            else:
                # 인터벌에 포함 안되는 값
                if make_interval:
                    # 직전 값까지는 인터벌에 포함되었으므로, i에서
                    # 인터벌이 끝났다. 인터벌을 더해줌.
                    res.append([int_s, int_e + 1])
                    make_interval = False

        while 억까_ind < len(억까):
            # 끝에 오는 길이 0짜리 인터벌들을 마저 추가해주자.
            if int_e + 1 < (v := 억까[억까_ind]):
                res.append([v, v])
            억까_ind += 1

        return res
