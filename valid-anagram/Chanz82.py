class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()

        # 공간복잡도 : hashmap을 사용하므로 공간복잡도는 O(N)입니다.
        # 시간복잡도 : 문자열 s의 길이만큼 한번 순회하고, 다시 문자열 t의 길이만큼 순회하므로 O(s+t) => O(N)입니다.
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        
        for ch in t:
            if ch in hashmap:
                hashmap[ch] -= 1
                if hashmap[ch] == 0:
                    del hashmap[ch]
            else:
                return False
        
        return not hashmap
      
