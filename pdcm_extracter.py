import re
from impedance_measurement.impedance_raw_parser import parse_impedance_raw


def extract_pdcms(raw_pdcm_infos, match_str):
    local_pdcms = []
    local_single_pdcm = []

    for info in raw_pdcm_infos:
        # print(info)
        if info:
            m = re.match(match_str, info)
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
