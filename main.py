# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sys import argv
import peak_info_reader
import raw_envelope_reader
import pdcm_extracter
import peak_drawer
import echo_reader

import numpy as np
from peak_raw_datas.raw_uart_info0_from_file import raw_uart_info0
from peak_raw_datas.raw_uart_info1_from_file import raw_uart_info1
from raw_uart_info2_from_file import raw_uart_info2

from sensor_echos import echos_extracter
from sensor_echos.echos_info import echos_prints
from sensor_echos.echos_info import echos_seem_abnormal

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# pdcm = "DSI 1, Sensor 1, PDCM 05: 0x13b4 0x4613 0xf3b3 0x3c23 0x03b5 0x3920 0x3f05 0xd92a"
# single_pdcm_decimal = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    '''
    sensor1_pdcms = []
    sensor2_pdcms = []
    sensor3_pdcms = []

    raw_uart_infos = raw_uart_info2.strip('\n').split('\n')

    sensor1_to_match = r'^(DSI \d{1,2}, Sensor 1, PDCM (\d{1,5}):)(( 0(x|X)[0-9(a-z|A-Z)]{4}){8})'
    sensor1_pdcms = pdcm_extracter.extract_pdcms(raw_uart_infos, sensor1_to_match)
    sensor2_to_match = r'^(DSI \d{1,2}, Sensor 2, PDCM (\d{1,5}):)(( 0(x|X)[0-9(a-z|A-Z)]{4}){8})'
    sensor2_pdcms = pdcm_extracter.extract_pdcms(raw_uart_infos, sensor2_to_match)
    sensor3_to_match = r'^(DSI \d{1,2}, Sensor 3, PDCM (\d{1,5}):)(( 0(x|X)[0-9(a-z|A-Z)]{4}){8})'
    sensor3_pdcms = pdcm_extracter.extract_pdcms(raw_uart_infos, sensor3_to_match)

    # peak_drawer.draw_peaks(pdcms)
    # peak_drawer.draw_envlopes(pdcms)

    # peak_drawer.draw(pdcms)
    # peak_drawer.draw_baseon_latest(pdcms)

    # peak_drawer.draw_originals_and_sendouts()

    peak_drawer.draw_baseon_delta_height(sensor1_pdcms, sensor2_pdcms, sensor3_pdcms)
    # echos = echo_reader.read(raw_uart_infos)
    # peak_drawer.draw_ehcos_after_pars(echos)
    '''

    # raw_echos_strs = echos_prints.strip('\n').split('\n')
    raw_echos_strs = echos_seem_abnormal.strip('\n').split('\n')
    str_to_match = r'^.+\[(\d{1,3})\]echonum=(\d{1,3}) echoheight=(\d{1,5})'
    echo_nums = []
    echo_heights = []
    echo_nums, echo_heights = echos_extracter.read_and_draw_echos(raw_echos_strs, str_to_match)

    # print(len(echo_nums))
    # print(len(echo_heights))


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
