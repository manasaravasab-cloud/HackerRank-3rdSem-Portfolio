import sys

def compare_triplets(a: list[int], b: list[int]) -> list[int]:
    """
    Compares two ratings triplets element-by-element and returns individual scores.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    alice_score = sum(1 for x, y in zip(a, b) if x > y)
    bob_score = sum(1 for x, y in zip(a, b) if x < y)
    return [alice_score, bob_score]

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if len(input_data) >= 6:
        a = [int(x) for x in input_data[:3]]
        b = [int(x) for x in input_data[3:6]]
        result = compare_triplets(a, b)
        print(f"{result[0]} {result[1]}")
