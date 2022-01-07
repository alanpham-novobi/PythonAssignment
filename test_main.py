import unittest
from testUtils import TestOutput


class Testing(unittest.TestCase):
    # def testcase_x(self):
    #     inputData = """"""
    #     output = """"""
    #     number = 0
    #     self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    # Assignment's testcase
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

    # Self testcase
    def testcase_10(self):
        inputData = """500 1 0\n2 3 4 5 6 7 9"""
        output = """0"""
        number = 10
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_11(self):
        inputData = """100 1 5\n11 65 0"""
        output = """"""
        number = 11
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_12(self):
        inputData = """360 2 2\n11 21 31 14 15 22 24 25 26 31 32 61 61 0"""
        output = """"""
        number = 12
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_13(self):
        inputData = """999 5 2\n11 21 31 51 61 61 15 26 0"""
        output = """21111"""
        number = 13
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_14(self):
        inputData = """999 9 5\n12 13 14 21 22 23 33 38 61 62 63 66 65 68 67\n35 39 33 38 61 62 63 21 22 23 24 31 32 33 33 34 0"""
        output = """52341233823658759312312341234"""
        number = 14
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_15(self):
        inputData = """999 9 5\n12 13 14 21 22 23 24 31 32 33 33 34 35 39 33 38 61 62 63 66 65 68 67\n35 39 33 38 61 62 63 66 65 68 67 12 13 14 21 22 23 24 31 32 33 33 34 0"""
        output = """5234123413345938126587593813658723413412334"""
        number = 15
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_16(self):
        inputData = """100 10 0\n19 72"""
        output = """11"""
        number = 16
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_17(self):
        inputData = """633 9 0\n19 17 73"""
        output = """100"""
        number = 17
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_18(self):
        inputData = """500 8 9\n19 19 29 39 19 19 78 78 77 76 79 75 0"""
        output = """10000042"""
        number = 18
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_19(self):
        inputData = """747 9 5\n18 28 74 16 26 28 77 65 66 71 72 73 0"""
        output = """5926761"""
        number = 19
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_20(self):
        inputData = """956 7 2\n11 12 21 25 28 34 35 39 71 75 78 65 69 66 72 71 75 33 39 74 79 0"""
        output = """"""
        number = 20
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_21(self):
        inputData = """500 5 5\n11 21 31 33 71 72 12 13 8 0"""
        output = """5111"""
        number = 21
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_22(self):
        inputData = """498 9 0\n21 8 8 0"""
        output = """0"""
        number = 22
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_23(self):
        inputData = """700 5 1\n31 8 72 72 72 65 8 0"""
        output = """"""
        number = 23
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_24(self):
        inputData = """640 6 4\n12 13 14 21 26 30 17 72 8 8 22 28 26 39 35 75 77 8 0"""
        output = """4234128707"""
        number = 24
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_25(self):
        inputData = """350 4 9\n11 12 21 25 28 34 8 35 39 71 75 8 78 65 69 66 72\n71 75 33 39 74 79 8 11 12 32 25 26 8 8 8 8 8 0"""
        output = """"""
        number = 25
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_26(self):
        inputData = """800 5 5\n11 12 21 25 28 35 48 0"""
        output = """51215"""
        number = 26
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_27(self):
        inputData = """495 7 1\n21 22 34 12 13 19 8 45"""
        output = """112423"""
        number = 27
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_28(self):
        inputData = """875 8 2\n21 25 34 34 36 13 14 18 44"""
        output = """2154463"""
        number = 28
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_29(self):
        inputData = """875 8 2\n12 15 19 25 26 24 34 38 64 8 71 72 75 32 39 34 17 15 49"""
        output = """2259572247"""
        number = 29
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_30(self):
        inputData = """996 7 3\n13 13 13 23 29 26 24 8 71 72 73 75 73 73 74 75\n34 38 64 8 71 72 75 32 33 43 33 34 17 15 49 0"""
        output = """"""
        number = 30
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_31(self):
        inputData = """412 5 3\n13 21 25 21 72 59"""
        output = """53"""
        number = 31
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_32(self):
        inputData = """865 2 5\n13 72 59 79 72 73 11 21 8 0"""
        output = """1"""
        number = 32
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_33(self):
        inputData = """745 4 8\n11 21 31 52 53 72 76 53 4 5 6 11 12 15 21 26 33 42 50 74 8 0"""
        output = """"""
        number = 33
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_34(self):
        inputData = """580 9 9\n28 33 45 20 10 5 6 3 12 13 15 7 8 72 73\n28 48 42 25 12 12 36 38 8 75 76 8 8 0"""
        output = """98350088822279"""
        number = 34
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))

    def testcase_35(self):
        inputData = """945 10 9\n12 13 23 36 40 45 20 10 5 6 3 12 13 15 7 8 72 73\n28 48 42 30 35 25 12 17 36 38 8 75 76 8 8 0"""
        output = """923360500288820552779"""
        number = 35
        self.assertTrue(TestOutput.checkOutput(inputData, output, number))


if __name__ == '__main__':
    unittest.main()
