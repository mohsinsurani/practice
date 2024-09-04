from collections import defaultdict
from typing import List

def get_count_occ(given_string: str, sub_string: str):
    k = len(sub_string)

    pattern_count = defaultdict(int)
    for item in sub_string:
        pattern_count[item] += 1

    
    window_count = defaultdict(int)
    i = 0
    j = 0
    count = 0 # To store the count of anagram occurrences

    while j < len(given_string):
        # add the current char in the window count
        window_count[given_string[j]] += 1

        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            if window_count == pattern_count:
                count += 1

            window_count[given_string[i]] -= 1
            if window_count[given_string[i]] == 0:
                del window_count[given_string[i]] 
            
            # Slide the window forward
            i += 1
            j += 1

    print(count)

given_string = "forxxorfxdofr"  
sub_string = "for"
k = len(sub_string)  # Window size
get_count_occ(given_string=given_string, sub_string=sub_string)
