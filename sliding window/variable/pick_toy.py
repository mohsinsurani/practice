# Longest Substring With K Unique Characters | Variable Size Sliding Window

from collections import defaultdict

# get the maximum window size from the subarray with target sum k
def get_max_toys(given_string: str, k: int):
    i = 0
    j = 0
    count_map = defaultdict(int)
    toy_count = 0

    while (j < len(given_string)):
        count_map[given_string[j]] += 1

        if len(count_map) < k:
            pass
        elif len(count_map) == k:
            toy_count = max(toy_count, j - i + 1)
        else:
            while (len(count_map) > k):
                count_map[given_string[i]] -= 1
                if count_map[given_string[i]] == 0:
                    del count_map[given_string[i]]
                i += 1
        j += 1
    print(toy_count)


given_string = "abaccab"
# a - one type of toy, b - one type, again a is repeated, o/p = acca - 2 type 2 quty
k = 2 # target toys to pick
get_max_toys(given_string=given_string, k=k)