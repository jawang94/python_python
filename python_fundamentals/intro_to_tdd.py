# 1
import unittest
def reverseList(arr):
    for i in range(0, len(arr)):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr


class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])

    def test2(self):
        return self.assertEqual(reverseList([2, 4, -3]), [-3, 4, 2])

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == "__main__":
    unittest.main()


# 2
import unittest
def isPalindrome(str):
    newstr = ""
    for i in range(0, len(str)):
        newstr += str[len(str)-1-i]
    return newstr == str


class isPalindromeTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(isPalindrome("racecar"), True)

    def test2(self):
        return self.assertEqual(isPalindrome("rabbit"), False)

    def test3(self):
        return self.assertTrue(isPalindrome("anna"))

    def test4(self):
        return self.assertTrue(isPalindrome("poop"))

    def setUp(self):
        print("Running setup")
        print("*"*50)

    def tearDown(self):
        print("Running teardown")
        print("*"*50)


if __name__ == "__main__":
    unittest.main()


# 3
import unittest
def countChange(num):
    # pass
    change = [0, 0, 0, 0]
    change[0] = int((num-num%25)/25)
    num = num%25
    change[1] = int((num-num%10)/10)
    num = num%10
    change[2] = int((num-num%5)/5)
    num = num%5
    change[3] = num
    return change


class countChangeTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(countChange(87), [3,1,0,2])

    def test2(self):
        return self.assertEqual(countChange(100), [4,0,0,0])

    def test3(self):
        return self.assertEqual(countChange(55), [2,0,1,0])

    def test4(self):
        return self.assertEqual(countChange(63), [2,1,0,3])

    def test5(self):
        return self.assertEqual(countChange(105), [4,0,1,0])
        
    def setUp(self):
        print("Running setup")
        print("*"*50)

    def tearDown(self):
        print("Running teardown")
        print("*"*50)


if __name__ == "__main__":
    unittest.main()

