from collections import defaultdict

# get the get_min_window_count from the subarray with win string
def get_min_window_count(given_string: str, win_string: str):
    i = 0
    j = 0
    min_window_length = float('inf')
    min_window_start = 0
    win_map_count = defaultdict(int)

    for item in win_string:
        win_map_count[item] += 1  

    required = len(win_map_count)  # Number of unique characters in win_string
    formed = 0  # To track how many characters have met their required frequency in the current window
    window_count = defaultdict(int)

    while (j < len(given_string)):
        char = given_string[j]
        window_count[char] += 1

        # Check if current character's frequency in window matches the frequency in win_string
        if char in win_map_count and window_count[char] == win_map_count[char]:
            formed += 1
        
        # Step 4: Try to contract the window from the left if all characters are matched
        while i <= j and formed == required:
            char = given_string[i]

            # Update the minimum window length and start index
            if j - i + 1 < min_window_length:
                min_window_length = j - i + 1
                min_window_start = i

            # Move left pointer `i` to make window smaller
            window_count[char] -= 1
            if char in win_map_count and window_count[char] < win_map_count[char]:
                formed -= 1

            i += 1

        # Move the right pointer `j` to expand the window
        j += 1

        # Step 5: Return the minimum window substring
    if min_window_length == float('inf'):
        return ""
    else:
        return given_string[min_window_start:min_window_start + min_window_length]




given_string = "TOTMTAPTAT"
win_string = "TTA"

get_min_window_count(given_string=given_string, win_string=win_string)