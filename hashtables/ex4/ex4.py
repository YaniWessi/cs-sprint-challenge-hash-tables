def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dubplicates = {}

    for number in a:
        if number not in dubplicates and number < 0:
            dubplicates[number] = number
    for number in dubplicates:
        if (dubplicates[number] * -1) in a:
            result.append(dubplicates[number] * -1)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# dictonary to key value
# they would by the number is
