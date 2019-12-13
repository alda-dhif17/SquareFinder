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
        self.y_from = y_from
        self.length = length

    def __str__(self):
        return "{0},{1} : {2}".format(self.x_from, self.y_from, self.length)


class Interval:
    def __init__(self, num, x_from, x_to, y, length):
        self.num = num
        self.x_from = x_from
        self.x_to = x_to
        self.y = y
        self.length = length

    def __str__(self):
        return self.num + ": " + str(self.x_from) + "-" + str(self.x_to) + " x " + str(self.length)

    def fits_in_list(self, curr_list):
        last_item = curr_list[-1]
        return ((self.x_from >= last_item.x_from and self.x_from <= last_item.x_to) or (self.x_to >= last_item.x_from and self.x_to <= last_item.x_to))


class RegionHandler:
    def __init__(self):
        self.regions = {}

    def add_square(self, current_num, x, y, length):
        if not current_num in self.regions:
            self.regions[current_num] = [Square(x, y, length)]
            return
        else:
            if length > self.regions[current_num][0].length:
                self.regions[current_num] = [Square(x, y, length)]
                return
            elif length == self.regions[current_num][0].length:
                self.regions[current_num].append(Square(x, y, length))


def main():
    lines = get_sections()
    # for intervals in lines:
    #     print('  |  '.join([str(x) for x in intervals]))

    char_map = find_consecutive(lines)

    find_squares(char_map)


def find_consecutive(lines):
    char_map = {}

    for line in lines:
        for interval in line:
            # character not present --> create new entry
            if interval.num not in char_map:
                char_map[interval.num] = [[interval]]
                continue

            list_of_curr_char = char_map[interval.num]

            isInList = False

            for curr_list in list_of_curr_char:
                if interval.fits_in_list(curr_list):
                    curr_list.append(interval)
                    isInList = True
                    continue

            if not isInList:
                list_of_curr_char.append([interval])

    return char_map


def get_sections() -> [[Interval]]:
    lines = []
    with open('../input.txt', 'r') as f:
        temp = f.readlines()
        for y in range(0, len(temp)):
            intervals = []
            l = temp[y]
            l = l.replace("\n", "")
            split = re.split(" ", l)

            current = split[0]
            x_from = 0
            x_to = 0
            for i in range(1, len(split)):
                if current == split[i]:
                    continue

                intervals.append(
                    Interval(current, x_from, i, y, i+1-x_from))
                current = split[i]
                x_from = i

            intervals.append(
                Interval(current, x_from, len(split)-1, y, x_to+1-x_from)
            )

            lines.append(intervals)

    return lines


def find_square_in_consecutive_interval(region_handler: RegionHandler, intervals: [Interval]):
    for (index, interval) in enumerate(intervals):
        # y = index
        min_x = interval.x_from
        max_x = interval.x_to

        for (j, lower) in enumerate(intervals[index+1:]):
            min_x = max(min_x, lower.x_from)
            max_x = min(max_x, lower.x_to)
            diff = max_x - min_x
            if j-index == diff:
                region_handler.add_square(interval.num, min_x, index, j-index)
            elif j-index < diff:
                for ni in range(0, diff):
                    region_handler.add_square(
                        interval.num, min_x+ni, index, j-index)


def find_squares(char_map):
    region_handler = RegionHandler()

    find_square_in_consecutive_interval(region_handler, char_map["1"][0])

    for region in region_handler.regions["1"]:
        print(str(region))


if __name__ == '__main__':
    main()
