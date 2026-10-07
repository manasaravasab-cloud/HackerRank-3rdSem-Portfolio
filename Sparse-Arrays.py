import sys
from collections import Counter

def matching_strings(string_list: list[str], queries: list[str]) -> list[int]:
    """
    Counts occurrences of query strings in string_list using a frequency map.
    Time Complexity: O(N + Q)
    Space Complexity: O(N)
    """
    counts = Counter(string_list)
    return [counts[q] for q in queries]

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        string_list = input_data[1:n + 1]
        q = int(input_data[n + 1])
        queries = input_data[n + 2:n + 2 + q]

        for ans in matching_strings(string_list, queries):
            print(ans)
