- 문제 : https://leetcode.com/problems/product-of-array-except-self/
- time complexity : O(n)
- space complexity : O(n)
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/05/08/leetcode-238

## case 나눠서 풀기

```java
public int[] productExceptSelf(int[] nums) {
    int[] products = new int[nums.length];
    int result = 1;
    int zeroCount = 0;

    int p = 0;
    while (p < nums.length) {
        if (nums[p] != 0) {
            result *= nums[p];
        } else {
            zeroCount++;
            if (zeroCount >= 2) {
                Arrays.fill(products, 0);
                return products;
            }
        }
        p++;
    }

    if (zeroCount == 1) {
        p = 0;
        while (p < nums.length) {
            if (nums[p] == 0) {
                products[p] = result;
            }
            p++;
        }
    } else {
        p = 0;
        while (p < nums.length) {
            products[p] = result / nums[p];
            p++;
        }
    }

    return products;
}
```

## 재밋는 방법으로 풀기 (prefixProd)

```java
public int[] productExceptSelf(int[] nums) {
    int[] result = new int[nums.length];

    int[] prefixProd = new int[nums.length];
    int[] suffixProd = new int[nums.length];

    prefixProd[0] = nums[0];
    for (int i = 1; i < nums.length; i++) {
        prefixProd[i] = prefixProd[i-1] * nums[i];
    }

    suffixProd[nums.length - 1] = nums[nums.length - 1];
    for (int i = nums.length - 2; i > -1; i--) {
        suffixProd[i] = suffixProd[i + 1] * nums[i];
    }

    result[0] = suffixProd[1];
    result[nums.length - 1] = prefixProd[nums.length - 2];
    for (int i = 1; i < nums.length - 1; i++) {
        result[i] = prefixProd[i - 1] * suffixProd[i + 1];
    }

    return result;
}
```
