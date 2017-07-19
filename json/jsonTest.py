import unittest
import jsonNew


class TestStringMethods(unittest.TestCase):
    def testCat(self):
        self.assertEqual(jsonNew.cat('"a":"aaaa',"key"), 0)
        self.assertEqual(jsonNew.cat('"a":aaaa',"key"), 0)
        self.assertEqual(jsonNew.cat('"a:"aaaa"',"key"), 0)
        self.assertEqual(jsonNew.cat('"key""aaaa"',"key"), 0)
        self.assertEqual(jsonNew.cat('"key":"55a55',"key"), 0)
        self.assertEqual(jsonNew.cat('"key":""',"key"), "")
        self.assertEqual(jsonNew.cat('"key":"as","key":65',"key"), ',"key":65')
        self.assertEqual(jsonNew.cat(':"as","key":65',"key"), 0)
    def testCheck(self):
        self.assertEqual(jsonNew.check('"a":""',"key"), 1)
        self.assertEqual(jsonNew.check('"a":"as"',"key"), 1)

if __name__ == '__main__':
    unittest.main()
