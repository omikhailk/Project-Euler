def sum_of_multiples(limit):
    """
    This function will find the sum of all of the
    multiples of 3 or 5 which are below the limit.
    """
    multiples = [i for i in range(1, limit) if not i % 3 or not i % 5]
    return sum(multiples)


print(sum_of_multiples(1000))
