from unittest import TestCase


from cycle_detector import CycleDetected
from flatter import flatten


class Test(TestCase):
    def test_flattens(self):
        self.assertEquals(
            list(flatten([1, [2, 3]])), 
            [1, 2, 3])

    def test_flattens_strings(self):
        self.assertEquals(
            list(flatten(
                [['one', 'two'], 'three', ['four', ['five', 'six']]])),
            ['one', 'two', 'three', 'four', 'five', 'six'])

    def test_can_flatten_strings_if_asked(self):
        self.assertEquals(
            list(flatten('abc', excluded_types=())),
            ['a', 'b', 'c'])

    def test_sets(self):
        self.assertEquals(
            list(flatten(set(['a', 'bc']))),
            ['a', 'bc'])

    def test_multiple_types(self):
        self.assertEquals(
            list(flatten(['a', ('b', 'c')])),
            ['a', 'b', 'c'])
        
                         
            



