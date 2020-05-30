# Python program that returns true if there is
# a Pythagorean Triplet in a given array.
from math import sqrt


class PythagoreanTriplet():
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.BaseSide = -1
        self.OppositeSide = -1
        self.Hypotnuse = -1
        self.found = False

    def __init__(self, a, b, c, isTriplet):
        # Each rocket has an (x,y) position.
        self.BaseSide = a
        self.OppositeSide = b
        self.Hypotnuse = c
        self.found = isTriplet


# Returns true if there is Pythagorean
# triplet in ar[0..n-1]
def isTriplet(ar, n):
    # Square all the elemennts
    for i in range(n):
        ar[i] = ar[i] * ar[i]

    # sort array elements
    ar.sort()

    # fix one element
    # and find other two
    # i goes from n - 1 to 2
    for i in range(n - 1, 1, -1):
        # start two index variables from
        # two corners of the array and
        # move them toward each other
        j = 0
        k = i - 1
        while (j < k):
            # A triplet found
            if (ar[j] + ar[k] == ar[i]):
                pt = PythagoreanTriplet(int(sqrt(ar[j])), int(sqrt(ar[k])), int(sqrt(ar[i])), True)
                return pt
            else:
                if (ar[j] + ar[k] < ar[i]):
                    j = j + 1
                else:
                    k = k - 1
    # If we reach here, then no triplet found
    return PythagoreanTriplet()


# Driver program to test above function */
ar = [42, 12, 54, 69, 48, 45, 63, 58, 38, 60, 24, 42, 30, 79, 17, 36, 91, 43, 89, 7, 41, 43, 65, 49, 47, 6, 91, 30, 71,
      51, 7, 2, 94, 49, 30, 24, 85, 55, 57, 41, 67, 77, 32, 9, 45, 40, 27, 24, 38, 39, 19, 83, 30, 42, 34, 16, 40, 59,
      5, 31, 78]
ar_size = len(ar)
result = isTriplet(ar, ar_size)
print(result.BaseSide, result.OppositeSide, result.Hypotnuse, result.found)
if (result.found):
    print("Yes")
else:
    print("No")
