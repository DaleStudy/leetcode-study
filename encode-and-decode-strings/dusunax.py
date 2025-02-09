'''
# 271. Encode and Decode Strings

## Time and Space Complexity

Use ":" as a separator and also store the length of each string to decode the string correctly.


### encode

```
TC: O(n * k)
SC: O(m)
```

#### TC is O(n * k):

- iterating through the list of strings and appending each string to the result. = O(n * k)
  - f-string is O(k)

#### SC is O(m):
- storing the result in a string.

### decode

```
TC: O(m)
SC: O(m)
```

#### TC is O(m):
- iterating over the string until the string length is 0. = O(m)
- do list slicings for extract parts and removing the processed section = each operation takes O(k)

#### SC is O(m):
- storing the result in a list(total length of strings is m) = O(m)

'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ''
        for str in strs: # TC: O(n)
            result += f"{len(str)}:{str}" # TC: O(k)
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
      result = []

      while len(str) > 0: # TC: O(m)
          length = int(str[:1]) # TC: O(k)
          string = str[2:length+2] # TC: O(k)
          str = str[length+2:] # TC: O(k)

          result.append(string) # SC: O(m)
        
      return result
