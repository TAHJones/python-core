def test_not_in(collection, item):
    assert item not in collection, "{0} does not contain {1}".format(collection, item)
    print("test_not_in() passed!")

# test_not_in([0,1,2,3,4], 4)
test_not_in([0,1,2,3,4], 5)


def test_between(collection, myNumber):
    myMax = max(collection)
    myMin = min(collection)
    assert myNumber > myMin and myNumber < myMax, "{0} is between {1} and {2}".format(myNumber, myMin, myMax)
    print("test_between() passed!")

test_between([1,2,3,4,5,6], 4)
# test_between([1,2,3,4,5,6], 0)
# test_between([1,2,3,4,5,6], 7)