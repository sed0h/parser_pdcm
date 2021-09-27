def extract_peaks(xs, ys, Peak_List, prev):
    # prev = [[prev_echo_num, prev_echo_height], [delta_echo_num_step, delta_echo_height_step]]

    pdcm_frame_counter = (Peak_List[0] >> 8) & 0xF
    subtype = Peak_List[0] & 0x000F
    if(1 == subtype) or (2 == subtype):
        envelp_frame_counter = Peak_List[1] >> 8
        print("EnvCnt" + str(envelp_frame_counter))

        # init prevs
        prev_echo_num = prev[0][0]
        prev_echo_height = prev[0][1]
        delta_echo_num_step = prev[1][0]
        if prev[1][1] >= 0:
            delta_echo_height_step_p = prev[1][1]
            delta_echo_height_step_n = 0
        else:
            delta_echo_height_step_n = prev[1][1] * -1
            delta_echo_height_step_p = 0

        # one PDCM, 12bytes echo info
        delta_echos = []
        LF_flag = Peak_List[1] >> 15
        for i in range(2, 8):
            delta_echos.append(Peak_List[i-1] & 0x00FF)
            delta_echos.append(Peak_List[i] >> 8)

        # parse each echo info
        delta_height = 0
        echo_height = 0
        echo_num = 0
        for delta_echo in delta_echos:
            if (delta_echo >> 6) == 0:  # +DeltaEchoHeight
                delta_height = (delta_echo_height_step_p << 6) | (delta_echo & 0x003F)
                delta_echo_height_step_p = 0
                delta_echo_height_step_n = 0
                # echo_height = delta_height*32+prev_echo_height
                echo_height = (delta_height + prev_echo_height)
                echo_num = prev_echo_num+1
                print("EchoNum: " + str(echo_num) + ',EchoHeight: ' + str(32*echo_height))
                prev_echo_height = echo_height
                prev_echo_num = echo_num

                xs.append(echo_num)
                ys.append(echo_height)
            elif (delta_echo >> 6) == 1:  # -DeltaEchoHeight
                delta_height = (delta_echo_height_step_n << 6) | (delta_echo & 0x003F)
                delta_echo_height_step_n = 0
                delta_echo_height_step_p = 0
                # echo_height = prev_echo_height-delta_height*32
                echo_height = prev_echo_height - delta_height
                echo_num = prev_echo_num+1
                print("EchoNum: " + str(echo_num) + ',EchoHeight: ' + str(32*echo_height))
                prev_echo_height = echo_height
                prev_echo_num = echo_num

                xs.append(echo_num)
                ys.append(echo_height)
            elif (delta_echo >> 5) == 4:  # +DeltaEchoHeightStep
                delta_echo_height_step_p = delta_echo & 0x1F
            elif (delta_echo >> 5) == 5:  # -DeltaEchoHeightStep
                delta_echo_height_step_n = delta_echo & 0x1F
            elif (delta_echo >> 5) == 6:  # DeltaEchoNum
                delta_echo_num = (delta_echo_num_step << 5) | (delta_echo & 0x1F)
                delta_echo_num_step = 0
                prev_echo_num = prev_echo_num + delta_echo_num
            elif (delta_echo >> 4) == 14:  # DeltaEchoNumStep
                delta_echo_num_step = delta_echo & 0x0F
            elif (delta_echo >> 4) == 15:  # last frame
                delta_echo_RSV = delta_echo & 0x0F

        # set current echo info to prev
        prev[0][0] = prev_echo_num
        prev[0][1] = prev_echo_height
        prev[1][0] = delta_echo_num_step
        if delta_echo_height_step_p == 0:
            prev[1][1] = delta_echo_height_step_n * -1
        else:
            prev[1][1] = delta_echo_height_step_p

        print("Current PDCM Last One: " + str(prev[0][0]), str(prev[0][1]), str(prev[1][0]), str(prev[1][1]))
    return prev
