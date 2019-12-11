import re


class PointFrom:
    def __init__(self, num, x, y, length):
        self.num = num
        self.x = x
        self.y = y
        self.length = length


class Square:
    def __init__(self, x_from, y_from, length):
        self.x_from = x_from
        self.x_to = y_from
        self.length = length


class Interval:
    def __init__(self, num, x_from, x_to, y, length):
        self.num = num
        self.x_from = x_from
        self.x_to = x_to
        self.y = y
        self.length = length

    def __str__(self):
        return self.num + ": " + str(self.x_from) + "-" + str(self.x_to) + " x " + str(self.length)


class RegionHandler:
    def __init__(self):
        self.regions = {}

    def add_square(self, current_num, x, y, length):
        if not current_num in self.regions:
            self.regions[current_num] = list(Square(x, y, length))
            return
        else:
            if length > self.regions[current_num][0].length:
                self.regions[current_num] = list(Square(x, y, length))
                return
            elif length == self.regions[current_num][0].length:
                self.regions[current_num].append(Square(x, y, length))


def main():
    lines = getSections()
    # for intervals in lines:
    #     print('  |  '.join([str(x) for x in intervals]))

    find_squares(lines)


def test(val: int):
    print(str(val))


def getSections() -> [[Interval]]:
    lines = []
    with open('../input.txt', 'r') as f:
        temp = f.readlines()
        for y in range(0, len(temp)):
            intervals = []
            l = temp[y]
            l = l.replace("\n", "")
            split = re.split("( )+", l)

            current = split[0]
            x_from = 0
            x_to = 0
            for i in range(1, len(split)):
                if current == split[i]:
                    continue

                intervals.append(
                    Interval(current, x_from, i, y, i+1-x_from))
                # print(current)
                current = split[i]
                x_from = i

            intervals.append(
                Interval(current, x_from, len(split)-1, y, x_to+1-x_from)
            )

            lines.append(intervals)
            # for i in intervals:
            #     print(str(i)+"  ===  "+str(y))
            # print(intervals)

    return lines


def find_squares(lines: list[list[Interval]]):
    region_handler = RegionHandler()

    points = []
    for intervals in lines:
        for interval in intervals:
            point = None
            for point in points:
                if point.num == interval.num:
                                        pass


if __name__ == '__main__':
    main()
