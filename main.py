# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sys import argv
import re
import peak_info_reader
import matplotlib.pyplot as plt
import numpy as np
from raw_uart_info0_from_file import raw_uart_info0
from raw_uart_info1_from_file import raw_uart_info1
from raw_uart_info2_from_file import raw_uart_info2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def extract_pdcms(raw_pdcm_infos):
    local_pdcms = []
    local_single_pdcm = []

    for info in raw_pdcm_infos:
        # print(info)
        if info:
            m = re.match(r'^(DSI \d{1,2}, Sensor \d{1,2}, PDCM (\d{1,5}):)(( 0(x|X)[0-9(a-z|A-Z)]{4}){8})', info)
            if m:
                if m.group(3):
                    frame_str = m.group(3).strip(' ').split(' ')
                    # print(frame_str)
                    for f in frame_str:
                        frame_dec = int(f, 16)
                        # frame_bin = bin(frame_dec)
                        local_single_pdcm.append(frame_dec)
                    # print(single_pdcm_decimal)
                    local_pdcms.append(local_single_pdcm)
                    local_single_pdcm = []
    # print(pdcms)
    return local_pdcms


# pdcm = "DSI 1, Sensor 1, PDCM 05: 0x13b4 0x4613 0xf3b3 0x3c23 0x03b5 0x3920 0x3f05 0xd92a"
single_pdcm_decimal = []

raw_uart_info_from_file = \
('''

DSI 1, Sensor 1, PDCM 08: 0x15b1 0x1880 0xb60d 0x6a11 0x0911 0x091d 0x8648 0x4ae3

DSI 1, Sensor 1, PDCM 09: 0x16f1 0x1d00 0x4a14 0xaf18 0x8618 0x8624 0x8c58 0x2139

DSI 1, sensor 1, HwErr

DSI 1, Sensor 1, PDCM 10: 0x16f1 0x0000 0x0000 0x3330 0x0868 0x0384 0x3e88 0x0aee

DSI 1, Sensor 1, PDCM 11: 0x17f1 0x2280 0x2114 0x3330 0x0868 0x0384 0x3e88 0x0a55

DSI 1, Sensor 1, PDCM 12: 0x18f1 0x2d80 0x2c0c 0x2d40 0x0820 0x092c 0x2940 0x083b

DSI 1, Sensor 1, PDCM 13: 0x18f1 0x2d80 0x2c00 0x0000 0x0000 0x036c 0x0f70 0x0181

DSI 1, Sensor 1, PDCM 14: 0x19f1 0x3780 0x090c 0x1318 0x0650 0x036c 0x0f70 0x01bd

DSI 1, Sensor 1, PDCM 15: 0x1af1 0x4000 0x081c 0x2d20 0x2c20 0x2c2c 0x3630 0x25c5

DSI 1, Sensor 1, PDCM 16: 0x1af1 0x4000 0x081c 0x2d20 0x2c20 0x2c2c 0x3600 0x004a

DSI 1, Sensor 1, PDCM 17: 0x1bf1 0x4300 0x2534 0xa358 0x7b58 0x7b94 0xf3d0 0x3dbb

DSI 1, Sensor 1, PDCM 18: 0x1cf1 0x5000 0x3d14 0x4c30 0x0780 0x20a4 0x4eb0 0x4b6c

DSI 1, Sensor 1, PDCM 19: 0x1df1 0x5b00 0x4b3c 0xa060 0x3c68 0x0384 0x08a0 0x02c6

DSI 1, Sensor 1, PDCM 20: 0x1ef1 0x6500 0x0224 0x0a38 0x0178 0x038c 0x0898 0x02ab

DSI 1, Sensor 1, PDCM 21: 0x1ef1 0x6500 0x0224 0x0a38 0x0178 0x038c 0x0898 0x02ab

DSI 1, Sensor 1, PDCM 22: 0x1ef1 0x6500 0x0224 0x0a38 0x0178 0x038c 0x0898 0x02ab

PDCM time:41502, Total time:43613

Peak Env, Chirp: Dot Cnt Total:80, Env1 Cnt: 2, Env2 Cnt: 0, AM: Dot Cnt Total:0, Env Cnt: 0

start_pulses_send 2, mode: 2

''')
('''
DSI 1, Sensor 1, PDCM 09: 0x16f1 0x1981 0x392c 0x2f68 0xf068 0xf074 0xf590 0x3f5f
DSI 1, Sensor 1, PDCM 11: 0x17f1 0x2280 0x3f0c 0x6b20 0x3820 0x382c 0x4f48 0x2c0b
DSI 1, Sensor 1, PDCM 12: 0x18f1 0x2700 0x2c1c 0x9548 0x1448 0x1464 0x5688 0x15eb
DSI 1, Sensor 1, PDCM 13: 0x19f1 0x2f80 0x151c 0x3d38 0x0f58 0x0774 0x4f80 0x1dd6
DSI 1, Sensor 1, PDCM 14: 0x1af1 0x3780 0x1d24 0x9828 0x6400 0x0000 0x0000 0x0079
DSI 1, Sensor 1, PDCM 15: 0x1bf1 0x4a00 0x2914 0x4238 0x0c38 0x0c5c 0x1970 0x04cb
DSI 1, Sensor 1, PDCM 16: 0x1cf1 0x6080 0x0124 0x2048 0x0848 0x085c 0x0f78 0x08b0
''')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pdcms = []

    raw_uart_infos = raw_uart_info2.strip('\n').split('\n')
    # print(raw_uart_infos)

    pdcms = extract_pdcms(raw_uart_infos)

    infos = []
    xs = []
    ys = []
    for pdcm in pdcms:
        info = peak_info_reader.extract_peak_info(pdcm)
        for i in info:
            # if i[2] > 0:
            xs.append(i[0])
            ys.append(i[2])
    print(xs, ys)
    plt.plot(xs, ys)
    for a,b in zip(xs, ys):
        plt.text(a, b, (a,b),ha='center', va='bottom', fontsize=8)
    plt.show()


    # if len(argv) >= 3:
    #     print("do not support >= 2 file")
    #     sys.exit(-1)


    # saved_files_from_uart = 'saved_peak_info\ReceivedTofile-COM9-2021_7_30_11-42-05.DAT'
    # pdcms_lst = []
    # with open(saved_files_from_uart, 'rb') as f:
    #     while 1:
    #         line = f.readline()
    #         if not line:
    #             break
    #         line_str = line.strip(b'\r').strip(b'\n').decode()
    #         # print(type(line_str))
    #         m = re.match(r'^(DSI \d{1,2}, Sensor \d{1,2}, PDCM (\d{1,5}):)(( 0(x|X)[0-9(a-z|A-Z)]{4}){8})', line_str)
    #         if m:
    #             # print(m.group(2))  # print(m.group(0)) # print(m.group(1))
    #             idx = int(m.group(2))
    #             ele = m.group(3)
    #             pdcms_lst.insert(idx, ele)


    # line_lft_right = line.split(b':')
    # if len(line_lft_right) >= 2:
    #     ele_lst = line_lft_right[1].split(b' ')
    #     # print(type(line_elements[1]))  # <class 'bytes'>
    #     for ele in ele_lst:
    #         print(ele)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
