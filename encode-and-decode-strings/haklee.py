"""
encode: TC: O(n), SC: O(l)
decode: TC: O(n), SC: O(l)

input으로 들어온 string들의 길이를 전부 더한 값을 l이라고 하자.
input에 들어있는 아이템 개수를 n이라고 하자.

아이디어: 
- 인풋을 처리한 값 앞쪽에 인풋을 해석하기 위한 정보를 두자.
    - 즉, 인풋을 처리한 값을 일종의 body로 보고 앞에 header를 붙이는 접근.
    - header는 body의 값이 어떻게 들어와도 영향을 받지 않는다!
- 다음과 같이 encode를 한다.
    - encode한 string은 f'{header}:{body}'형식으로 되어있다.
    - body에는 input에 있는 값을 바로 concat한 값을 쓴다.
    - header에는 input에 있는 string의 길이를 ','로 구분한 값을 쓴다.
    - e.g.)
        body: ['a', 'bc', 'd'] -> 'abcd'
        header: ['a', 'bc', 'd'] -> '1,2,1'
        encoded string: '1,2,1:abcd'
- 다음과 같이 decode를 한다.
    - 첫 번째로 등장하는 ':'을 찾아서 split한다.
        - 앞 부분이 header, 뒷 부분이 body다.
    - header를 다음과 같이 처리한다.
        - ','로 split해서 `x: List[int]`를 얻는다.
    - body를 다음과 같이 처리한다.
        - body를 앞서 구한 x에 들어있는 길이로 쭉 쪼개면 된다.
        - x의 누적합을 구하면서 이를 시작 인덱스로 활용한다.

SC:
- encode
    - body의 길이는 l이다. 즉, O(l).
    - header의 길이는 최악의 경우 O(l)이다.
        - input의 모든 글자가 길이 1일때, 최악의 경우 O(l).
        - input의 모든 글자가 한 단어일때, 최고의 경우 O(log l).
    - 종합하면 O(l) + O(l)이라 O(l)이다.
- decode
    - 전체 메시지의 body에 들어있는 값을 쪼개서 리스트로 만드는 것이므로 O(l).
    - 길이 값을 split해서 리스트로 만든다. O(n)
    - 종합하면 O(l + n)인데, 이때 n은 무조건 l 이하이므로 O(l).

TC:
- encode
    - n개의 아이템을 순회하면서 길이를 얻는다. O(n).
- decode
    - 길이 값을 split해서 리스트로 만든다. O(n).
    - 누적합을 활용하여 길이 값 리스트를 한 번 순회. O(n).
    - 종합하면 O(n).
"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        body = "".join(strs)
        header = ",".join([str(len(i)) for i in strs])
        return header + ":" + body

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        header, body = str.split(":", 1)
        len_list = [int(i) for i in header.split(",")]
        start_ind = 0
        result = []
        for i in len_list:
            result.append(body[start_ind : start_ind + i])
            start_ind += i
        return result
