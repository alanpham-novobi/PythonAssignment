import unittest
from testUtils import TestOutput


class Testing(unittest.TestCase):
    # def testcase_x(self):
    #     inputData = """"""
    #     output = """"""
    #     number = 0
    #     self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_1(self):
        inputData = """172 4 5\n0 15"""
        output = """5"""
        number = 1
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_2(self):
        inputData = """172 4 0\n23 42"""
        output = """032"""
        number = 2
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_3(self):
        inputData = """145 1 1\n6 11"""
        output = """1"""
        number = 3
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_4(self):
        inputData = """172 4 0\n32 31"""
        output = """021"""
        number = 4
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_5(self):
        inputData = """812 10 0\n11 12 13 14 15 16 17 18 19 72"""
        output = """0123456791"""
        number = 5
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_6(self):
        inputData = """200 2 0\n28 20 29 8"""
        output = """0"""
        number = 6
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_7(self):
        inputData = """400 3 3\n17 13 10 47"""
        output = """33"""
        number = 7
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_8(self):
        inputData = """812 4 0\n13 14 19 18 55"""
        output = """9"""
        number = 8
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_9(self):
        inputData = """200 8 0\n27 24 93"""
        output = """3470"""
        number = 9
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))


if __name__ == '__main__':
    unittest.main()
