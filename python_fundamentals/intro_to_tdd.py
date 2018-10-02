import unittest

# 1
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
def isPalindrome(str):
    newstr = ""
    for i in range(0,len(str)):
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

