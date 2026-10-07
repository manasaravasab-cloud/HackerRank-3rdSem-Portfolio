import sys

def dynamic_array(n: int, queries: list[list[int]]) -> list[int]:
    """
    Processes dynamic array queries using bitwise XOR indexing.
    Time Complexity: O(Q)
    Space Complexity: O(N + Q)
    """
    arr = [[] for _ in range(n)]
    results = []
    last_answer = 0

    for q_type, x, y in queries:
        idx = (x ^ last_answer) % n
        if q_type == 1:
            arr[idx].append(y)
        elif q_type == 2:
            last_answer = arr[idx][y % len(arr[idx])]
            results.append(last_answer)

    return results

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        q = int(input_data[1])
        queries = []
        idx = 2
        for _ in range(q):
            queries.append([int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])])
            idx += 3
        
        for ans in dynamic_array(n, queries):
            print(ans)
