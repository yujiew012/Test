"""Simple bubble sort demonstration."""


def bubble_sort(numbers):
    """Sort a list of numbers in place using bubble sort and return it."""
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("before sort:", sample)
    sorted_list = bubble_sort(sample)
    print("after sort:", sorted_list)
