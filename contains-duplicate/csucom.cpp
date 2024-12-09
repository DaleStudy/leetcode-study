#include <malloc.h>
#include <string.h>

bool containsDuplicate(int* nums, int numsSize) {
    char* pflag = (char*)malloc(1000000001);
    char* mflag = (char*)malloc(1000000001);
    memset(pflag, 0, 1000000001);
    memset(mflag, 0, 1000000001);
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < 0) {
            if (mflag[-nums[i]] == 1) {
                free(pflag);
                free(mflag);
                return true;
            }
            mflag[-nums[i]] = 1;
        }
        else {
            if (pflag[nums[i]] == 1) {
                free(pflag);
                free(mflag);
                return true;
            }
            pflag[nums[i]] = 1;
        }
    }
    free(pflag);
    free(mflag);
    return false;
}


