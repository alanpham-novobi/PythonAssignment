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
            self.success = True
            if e == 0:
                self.event_s1(e)
                break
            elif (e // 10) in [1, 2, 3, 4, 5, 6, 9]:
                self.event_s2(e)
            elif (e // 10) == 7:
                self.event_s3(e)
            elif e == 8:
                self.event_s4(e)
        if self.success:
            return self.ec
        else:
            return ''

    def event_s1(self, e):
        self.success = True

    def event_s2(self, e):
        b = self.idx % 10
        levelO = ((b if b > 5 else 5) if (self.idx > 6) else b)
        ringsignO = e % 10

        if self.level > levelO:
            self.ringsign = (
                self.ringsign + ringsignO) if (self.ringsign + ringsignO) <= 9 else 9
            self.ec += [ringsignO]
            if e // 10 == 9:
                self.event_a3()
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
                self.event_a3(option=False, ringsign=ringsignO)

    def event_s3(self, e):
        self.ringsign = 0
        digit = self.ec[::-1]
        adding = [0] * len(digit)
        adding[0] = e % 10
        result = [x + y for x, y in zip(digit, adding)]
        mem = 0
        temp = []
        for i in result:
            if i != result[-1]:
                temp.append((i + mem) % 10)
                if i >= 10:
                    mem = 1
                else:
                    mem = 0
            else:
                temp.append(i + mem)
        self.ec = temp[::-1]

    def event_s4(self, s):
        if (self.hp < 999):
            self.ec, exchange_ringsign = self.ec[:-1], self.ec[-1]
            self.ringsign = (self.ringsign - int(exchange_ringsign)
                             ) if (self.ringsign - int(exchange_ringsign)) > 0 else 0
            self.hp = 999

    def event_a1(self, ringsignO):
        temp = self.ec[::-1]
        remove_idx = temp.index(ringsignO)
        del temp[remove_idx]
        self.ec = temp[::-1]

    def event_a2(self):
        if len(self.ec) > 3:
            self.ec = self.ec[3:]
            print(self.ec)
        else:
            self.ec.clear()

    def event_a3(self, option=True, ringsignO=0):
        if option:
            self.ec = self.ec[::-1]
        else:
            self.ringsign = (
                self.ringsign - ringsignO) if (self.ringsign - ringsignO) > 0 else 0


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
    return knight_attributes, events


def knight_journey(filename):
    knight_attributes, events = read_file(filename)
    knight = Knight(
        knight_attributes[0], knight_attributes[1], knight_attributes[2], events)
    code = knight.traveling()
    return ''.join(map(str, code))
