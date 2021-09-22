from uart_envlp.rawdata import raw_uart_envlp


if __name__ == '__main__':
    uart_envlps = raw_uart_envlp.strip('\n').split('00 0D 0A')

    echos_hight = []
    for uart_envlp in uart_envlps:
        print(uart_envlp)
        envlp = uart_envlp.strip().split(' ')
        # if ((len(envlp)) >= 16) and '38' == envlp[15] and '00' == envlp[14]:
        #     # echos_hight.append(0)
        #     print(envlp)

