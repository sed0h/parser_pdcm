# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import codecs
from sys import argv

import chardet
from future.moves import sys


print_on = 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    if print_on:
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_dbc_header(line):
    nodes = line.strip('\n').split()
    if print_on:
        print("node:", nodes[0])


def parse_msgid(line):
    node = line.split()
    id = node[1]
    if print_on:
        print("msg_id:", id)
    return id


def parse_signame(line, message_id):
    node = line.split()
    nm = node[1]
    st = node[3].split('|')
    start = st[0]
    ln = st[1].split('@')
    len = ln[0]
    if print_on:
        print(" sig_name:", nm, 'start:', start, 'len:', len, 'Intel' if('1' == ln[1][0]) else 'Motorola', 'Signed' if('1' == ln[1][1]) else 'Unsigned')
    # print("cfd_signal_template_t sig_", nm, '_', message_id, " = {\n", message_id, ',\n"', nm, '",\n', start, ',\n', len, ',\n', 'true' if('1' == ln[1][0]) else 'false', ',\n', 'false' if('1' == ln[1][1]) else 'true', ',\n};\n', sep='', file=__file__)
    signal = {
        'msg_id': message_id,
        'sig_nm': nm,
        'start_bit': start,
        'sig_len': len,
        'intel_seq': (True if ('1' == ln[1][0]) else False),
        'unsign': (False if ('1' == ln[1][1]) else True)
    }
    signals.append(signal)


def print_object(sig):
    print("{", sig['msg_id'], ',"', sig['sig_nm'], '",', sig['start_bit'], ',',
          sig['sig_len'], ',', sig['intel_seq'], ',', sig['unsign'],
          '},', sep='', file=__file__)


def convert_file_encoding(filenme_in, filenme_out, encode_in, encode_out):
    try:
        fi = codecs.open(filename=filenme_in, mode='r', encoding=encode_in)
    except:
        print('open file_in failed')
        fi.close()
    else:
        print('file_in open ok!')
        data = fi.read()
    try:
        fo = codecs.open(filename=filenme_out, mode='w', encoding=encode_out)
    except:
        print('open file_out failed')
        fo.close()
    else:
        fo.write(data)
        print('file converted ok!!')
        fo.close()

# Press the green button in the gutter to run the script.


# !!!usage!!!: 
# 1.cd D:\1work\saic_zhijia\candbc_parse
# 2.canconvert arxmls/FVCM_20210607.arxml dbcs/m.dbc
# 3.python parse_dbc.py D:\1work\saic_zhijia\candbc_parse\dbcs\PHY_TEST_DBC.dbc
# output file is in current path !!!
# for example:
# (candbc_parse) C:\Users\YiXing>python D:\1work\saic_zhijia\candbc_parse\parse_dbc.py D:\1work\saic_zhijia\candbc_parse\dbcs\PHY_TEST_DBC.dbc
# output is in C:\Users\YiXing

if __name__ == '__main__':
    print_hi('PyCharm')
    if len(argv) >= 3:
        print("do not support >= 2 file")
        sys.exit(-1)
    else:
        dbcfile = argv[1]  # 'dbcs/m_CANCluster.dbc'  # PHY_TEST_DBC.dbc
    converted = 'encoding_converted.dbc'

    with open(dbcfile, 'rb') as f:
        data = f.read()
        encoding_type = chardet.detect(data)
        ecd_tp = encoding_type['encoding']
    if ecd_tp != 'utf-8':
        convert_file_encoding(dbcfile, converted, ecd_tp, 'utf-8')
    f = open(converted, 'r', encoding='utf-8')

    __file__ = open(r'canfd_signals.c', 'w')
    signals = []

    while 1:
        line = f.readline()
        if not line:
            break
        elif line.startswith('VERSION '):
            print_dbc_header(line)
        elif line.startswith('NS_ :'):
            print_dbc_header(line)
        elif line.startswith('BU_:'):
            print_dbc_header(line)
        elif line.startswith('BO_ '):
            mg_id = parse_msgid(line)
            while 1:
                line_sig = f.readline()
                if not line_sig:
                    break
                if not line_sig.startswith(' SG_ '):
                    break
                parse_signame(line_sig, mg_id)

    sorted_signals = sorted(signals, key=lambda x: x['msg_id'])
    for sig in sorted_signals:
        # print(sig, ',', sep='', file=__file__)
        print_object(sig)
    __file__.close()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
