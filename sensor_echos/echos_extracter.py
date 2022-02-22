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
                print(echo_indx)
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


import matplotlib.pyplot as plt


def read_draw_heights_about_sample(heights_raw_before, heights_raw_after, str_match):
    nums = []
    heights = []
    prev_num = 0

    for height_raw in heights_raw_before:
        matched = re.match(str_match, height_raw)
        if matched:
            num = matched.group(1)
            number = int(num, 10)
            height_value = int(matched.group(2), 10)
            if number < prev_num:
                plt.plot(nums, heights, color='blue')
                for a, b in zip(nums, heights):
                    if b > 4000:
                        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=3)
                print(nums, heights)
                nums = []
                heights = []
            nums.append(number)
            heights.append(height_value)
            prev_num = number
            print(prev_num)

    nums = []
    heights = []
    prev_num = 0
    for height_raw in heights_raw_after:
        matched = re.match(str_match, height_raw)
        if matched:
            num = matched.group(1)
            number = int(num, 10)
            height_value = int(matched.group(2), 10)
            if number < prev_num:
                plt.plot(nums, heights, color='red')
                for a, b in zip(nums, heights):
                    if b > 4000:
                        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=3)
                print(nums, heights)
                nums = []
                heights = []
            nums.append(number)
            heights.append(height_value)
            prev_num = number
            print(prev_num)

    plt.show()


def read_draw_line_numbers(lines, str_match):
    numbers = []
    for line in lines:
        matched = re.match(str_match, line)
        if matched:
            line_number = int(matched.group(1), 10)
            print(line_number)
            numbers.append(line_number)

    x_s = []
    for i in range(len(numbers)):
        x_s.append(i)
    plt.plot(numbers)
    for a, b in zip(x_s, numbers):
        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=3)
    plt.show()
