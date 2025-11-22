# TC: O(n)
# SC: O(1)
def isAnagram(s: str, t: str) -> bool:
  # TC: O(nlogn)
  # SC: O(n)
  # if sorted(list(s)) == sorted(list(t)):
  #   return True
  # else:
  #   return False

  chars = dict()

  if len(s) != len(t):
    return False

  for c in s:
    chars[c] = chars.get(c, 0) + 1

  for c in t:
    if c not in chars:
      return False
    chars[c] -= 1
    if chars[c] == 0:
      chars.pop(c)
  
  return True

if __name__ == '__main__':
  print(isAnagram('ab', 'a'))
