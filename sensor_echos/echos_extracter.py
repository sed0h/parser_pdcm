import re
from sensor_echos.echo_drawer import draw_echos


def read_and_draw_echos(echos_strs, str_to_match):
    nums = []
    heights = []
    prev_indx = 0

    for echos_str in echos_strs:
        matched = re.match(str_to_match, echos_str)
        if matched:
            if matched.group(1):
                echo_indx = (int(matched.group(1), 10))
                if echo_indx <= prev_indx:
                    print(nums)
                    print(heights)
                    draw_echos(nums, heights)
                    nums = []
                    heights = []
                prev_indx = echo_indx

            if matched.group(2):
                nums.append(int(matched.group(2), 10))
            if matched.group(3):
                heights.append(int(matched.group(3), 10))

    return nums, heights

