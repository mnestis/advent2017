
import unittest

import part1

class TestPart1(unittest.TestCase):

    def test_part1_a(self):
        level = part1.determine_level(1)
        self.assertEqual(level, 0)
        hour = part1.determine_hour(1)
        self.assertEqual(hour, 0)
        self.assertTupleEqual(part1.determine_coords(level, hour), (0, 0))
        self.assertEqual(part1.manhattan_distance(1), 0)

    def test_part1_b(self):
        level = part1.determine_level(12)
        self.assertEqual(level, 2)
        hour = part1.determine_hour(12)
        self.assertEqual(hour, 2)
        self.assertTupleEqual(part1.determine_coords(level, hour), (2, 1))
        self.assertEqual(part1.manhattan_distance(12), 3)

    def test_part1_c(self):
        level = part1.determine_level(23)
        self.assertEqual(level, 2)
        hour = part1.determine_hour(23)
        self.assertEqual(hour, 13)
        self.assertTupleEqual(part1.determine_coords(level, hour), (0, -2))
        self.assertEqual(part1.manhattan_distance(23), 2)

    def test_part1_d(self):
        self.assertEqual(part1.manhattan_distance(1024), 31)

    def test_part1_custom_1(self):
        # 10
        level = part1.determine_level(10)
        self.assertEqual(level, 2)
        hour = part1.determine_hour(10)
        self.assertEqual(hour, 0)
        self.assertEqual(part1.determine_coords(level, hour), (2, -1))
        self.assertEqual(part1.manhattan_distance(10), 3)

    def test_part1_custom_2(self):
        # 49
        level = part1.determine_level(49)
        self.assertEqual(level, 3)
        hour = part1.determine_hour(49)
        self.assertEqual(hour, 23)
        self.assertTupleEqual(part1.determine_coords(level, hour), (3, -3))
        self.assertEqual(part1.manhattan_distance(49), 6)
