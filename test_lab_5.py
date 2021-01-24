import unittest
from lab5 import naive_search

class MyTest(unittest.TestCase):
    def test_naive_search(self):
        self.assertEqual(naive_search("aabaacaadaabaaba", "aaba"), [(0,4),(9,13),(12,16)])
        self.assertEqual(naive_search("AABCCAADDEE", "FAA"), [])
        self.assertEqual(naive_search("AAAAAAA", "AAAA"), [(0,4),(1,5),(2,6),(3,7)])
        self.assertEqual(naive_search("AAAAAAAAAAAAAAAAAB", "AAAB"), [(14,18)])
        self.assertEqual(naive_search("Some books are to be tasted, others to be swallowed, and some few to be chewed and digested.", 'to'), [(15,17), (36, 38), (66,68)])

unittest.main()