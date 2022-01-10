class Knight:
    def __init__(self, hp, level, ringsign, events):
        self.hp = hp                # 1 <= hp <= 999
        self.level = level          # 1 <= level <= 10
        self.ringsign = ringsign    # 0 <= ringsign <= 9
        self.events = events
        self.opponents_baseDamage = {
            1: 0.8,
            2: 1.2,
            3: 4.1,
            4: 7.9,
            5: 6.5,
            6: 8.7,
            9: 0.1
        }
        self.ec = [ringsign]
        self.success = True

    def traveling(self):
        self.idx = 0
        for e in self.events:
            self.idx += 1
            if e < 100:
                if e == 0:
                    self.event_s1(e)
                    break
                elif (e // 10) in [1, 2, 3, 4, 5, 6, 9]:
                    self.event_s2(e)
                elif (e // 10) == 7:
                    self.event_s3(e)
                elif e == 8:
                    self.event_s4(e)
                else:               # Handle non-existed event
                    continue
            else:
                continue
            if not self.success:
                return ''
        return self.ec

    def event_s1(self, e):
        self.success = True

    def event_s2(self, e):
        b = self.idx % 10
        levelO = ((b if b > 5 else 5) if (self.idx > 6) else b)
        ringsignO = e % 10

        if self.level > levelO:
            self.ec += [ringsignO]
            if (e // 10) == 9:
                self.event_a3(win=True, ringsignO=ringsignO)
        elif self.level < levelO:
            self.hp = int(
                self.hp - self.opponents_baseDamage[e//10]*levelO*10)
            if (self.hp <= 0):
                self.success = False

            # Special case
            if (e // 10) == 4:
                self.event_a1(ringsignO)
            elif (e // 10) == 5:
                self.event_a2()
            elif (e // 10) == 9:
                self.event_a3(win=False, ringsignO=ringsignO)

    def event_s3(self, e):
        # What if EC Code is Empty ???? (After event 5XX)
        digit = self.ec[::-1] if self.ec else [0]
        adding = [0] * len(digit)
        adding[0] = e % 10
        result = [x + y for x, y in zip(digit, adding)]
        mem = 0
        temp = []
        for i in range(len(result)):
            if i != len(result) - 1:
                temp.append((result[i] + mem) % 10)
                if (result[i] + mem) >= 10:
                    mem = 1
                else:
                    mem = 0
            else:
                if (result[i] + mem) < 10:
                    temp.append(result[i] + mem)
                else:
                    temp.append((result[i] + mem) % 10)
                    temp.append((result[i] + mem) // 10)
        self.ec = temp[::-1]

    def event_s4(self, e):
        if (self.hp < 999 and len(self.ec) > 0):
            del self.ec[-1]
            self.hp = 999

    def event_a1(self, ringsignO):
        temp = self.ec[::-1]
        try:
            temp.remove(ringsignO)
            self.ec = temp[::-1]
        except:
            pass

    def event_a2(self):
        if len(self.ec) > 3:
            self.ec = self.ec[3:]
        else:
            self.ec.clear()

    def event_a3(self, win=True, ringsignO=0):
        if win:
            self.ec = self.ec[::-1]
        else:
            try:
                self.ec = list(filter(lambda x: x != ringsignO, self.ec))
            except:
                pass


def read_file(filename):
    knight_attributes = []
    events = []
    with open(filename, 'r') as f:
        input_data = f.readlines()
        knight_attributes = input_data.pop(0).split(' ')
        knight_attributes = tuple([int(x.replace('\n', ''))
                                  for x in knight_attributes])

        for line in input_data:
            events += line.split(' ')

        events = [int(x.replace('\n', '')) for x in events]
    # Handle error input
    if knight_attributes[0] not in range(0, 1000, 1):
        raise ValueError(
            "invalid knight's HP. Knight's HP must between 0 and 999")
    if knight_attributes[1] not in range(1, 11, 1):
        raise ValueError(
            "invalid knight's level. Knight's level must between 1 and 10")
    if knight_attributes[2] not in range(0, 10, 1):
        raise ValueError(
            "invalid knight's ringsign. Knight's ringsign must between 0 and 9")
    return knight_attributes, events


def error(func):
    def handlingError(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
    return handlingError


@error
def knight_journey(filename):
    knight_attributes, events = read_file(filename)
    knight = Knight(
        knight_attributes[0], knight_attributes[1], knight_attributes[2], events)
    code = knight.traveling()
    return ''.join(map(str, code))


if __name__ == '__main__':
    code = knight_journey('input.txt')
    if code:
        print(code)
    else:
        print('empty code')
