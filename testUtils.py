from main import knight_journey


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = f"testcase/" + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return filename


class TestOutput:
    @staticmethod
    def checkOutput(input, expect, num):
        inp = TestUtil.makeSource(input, num)
        dest = open("output/" + str(num) + ".txt", "w")
        solution = knight_journey(inp)
        if solution == expect:
            dest.write("Correct solution. Expected: {e}. Output: {s}".format(
                e=expect, s=solution))
            dest.close()
            return True
        else:
            dest.write("Incorrect solution. Expected: {e}. Output: {s}".format(
                e=expect, s=solution))
            dest.close()
            return False
