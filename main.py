def H_index(citations):
    citations.sort()

    for i, cited in enumerate(citations):

        result = len(citations) - i

        if result <= cited:
            return result

    return 0


if __name__ == '__main__':
    citations = [50, 40, 33, 23, 12, 11, 8, 5, 1, 0]
    print(H_index(citations))
