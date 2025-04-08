def is_anagram(s: str, t: str) -> bool:
    # return sorted(s) == sorted(t)
    '''
    Counter : 원소의 빈도수를 세는 자료구조, 한 번씩만 세면 됨 
    = O(n)
    Sorted : O(nlogn)
    '''
    return Counter(s) == Counter(t)
