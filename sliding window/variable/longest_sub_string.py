# Longest Substring With K Unique Characters | Variable Size Sliding Window

from collections import defaultdict

# get the maximum window size from the subarray with target sum k
def get_longest_substring(given_string: str, k: int):
    i = 0
    j = 0
    count_map = defaultdict(int)
    long_sub_string_count = 0

    while (j < len(given_string)):
        count_map[given_string[j]] += 1

        if len(count_map) < k:
            pass
        elif len(count_map) == k:
            long_sub_string_count = max(long_sub_string_count, j - i + 1)
        else:
            while (len(count_map) > k):
                count_map[given_string[i]] -= 1
                if count_map[given_string[i]] == 0:
                    del count_map[given_string[i]]
                i += 1
        j += 1
    print(long_sub_string_count)


given_string = "aabacbebebe"
k = 3 # target sum
get_longest_substring(given_string=given_string, k=k)