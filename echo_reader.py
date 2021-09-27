import re


def read(infos):
    echos = []
    for info in infos:
        if info:
            m = re.match(r'^num: (\d{1,3}), height: (\d{1,5})', info)
            if m:
                echo_num = int(m.group(1), 10)
                echo_height = int(m.group(2), 10)
                echo = (echo_num, echo_height)
                echos.append(echo)

    return echos
