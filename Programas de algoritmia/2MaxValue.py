import numpy as np


def test_rand():
    max1 = 0;
    max2 = 0;
    toTest = np.random.randint(200, size=10)
    for i in range(toTest.size):
        if toTest[i] > max1:
            max2 = max1
            max1 = toTest[i]
        elif toTest[i] > max2:
            max2 = toTest[i]

    print(f"Max: {max1}, Max2:{max2}")
    print(toTest)



if __name__ == '__main__':
    test_rand()
