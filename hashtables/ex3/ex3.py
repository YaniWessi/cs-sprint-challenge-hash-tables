def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # I need to hash the the
    # i need to loop through the
    #
    # Your code here
    count = {}
    result = []

    for inner in arrays:
        for number in inner:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1
    for (key, value) in count.items():
        if value > 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
