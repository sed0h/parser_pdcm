import matplotlib.pyplot as plt
import re


def extract_raw_data(pdcm_infos, match_str):
    bytes_in_1pdcm = []
    envlp_datum = []
    envlp_datum_s = []

    for info in pdcm_infos:
        # print(info)
        if info:
            m = re.match(match_str, info)
            if m:
                print(m.group(2))
                if m.group(3):
                    bytes_in_1pdcm = m.group(3).strip(' ').split(' ')
                    print(bytes_in_1pdcm)
                    for datum in parse_impedance_raw(bytes_in_1pdcm):
                        envlp_datum.append(datum)
                if 24 == int(m.group(2), 10):
                    envlp_datum_s.append(envlp_datum)
                    envlp_datum = []

    draw_impedance_envlp(envlp_datum_s)


def parse_impedance_raw(pdcm_bytes):
    datum = []
    frame_counter = (int(pdcm_bytes[0], 16) >> 8) & 0x000F
    for i in range(1, 7):
        data = ((int(pdcm_bytes[i], 16) & 0x00FF) << 8) + (int(pdcm_bytes[i+1], 16) >> 8)
        # print(data)
        datum.append(data)

    return datum


def draw_impedance_envlp(envlp_raw):
    xs = []
    ys = []
    i = 0

    for envlp in envlp_raw:
        xs = []
        ys = []
        i = 0
        for e_r in envlp:
            ys.append(e_r)
            i = i+1
            xs.append(1000000/50502*i)

        plt.plot(xs, ys)
        plt.grid()
        plt.xlabel('usec')
        plt.ylabel('ENVP_RAW_DATA')
        # for a, b in zip(xs, ys):
        #     plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=3)
    plt.show()
