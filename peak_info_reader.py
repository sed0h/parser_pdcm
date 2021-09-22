def extract_peak_info(Peak_List):
    echo_infos = []

    if ((Peak_List[0]&0x000F) == 1) or ((Peak_List[0]&0x000F) == 2) or ((Peak_List[0]&0x000F) == 3):
        PyhAddr = Peak_List[0]>>12
        # print(PyhAddr)
        FrameCounter = (Peak_List[0]>>8)&0x000F
        print(FrameCounter)

        Echo0_type = (Peak_List[1]>>2)&0x0001
        # print("Echo0_type:" + str(Echo0_type))
        Echo0_num = Peak_List[1]>>7;
        # print("Echo0_num:" + str(Echo0_num))
        Echo0_height = (((Peak_List[1]&0x0003)<<8) + (Peak_List[2] >> 8)) * 16;
        tmp=(Peak_List[1] & 0x0003) << 8;
        # print("Echo0_height:" + str(Echo0_height))
        print('{' + str(Echo0_type)+',' + str(Echo0_num)+','+ str(Echo0_height)+'},')
        ech0 = (Echo0_num, Echo0_type, Echo0_height)
        if Echo0_num > 0:
            echo_infos.append(ech0)

        Echo1_type = (Peak_List[2]>>2)&0x0001
        # print("Echo1_type:" + str(Echo1_type))
        Echo1_num = (((Peak_List[2]>>3)&0x001F) + Echo0_num)
        # print("Echo1_num:" + str(Echo1_num))
        Echo1_height = (((Peak_List[2]&0x0003)<<8) + (Peak_List[3]>>8))*16;
        # print("Echo1_height:" + str(Echo1_height))
        print('{' + str(Echo1_type)+',' + str(Echo1_num)+','+ str(Echo1_height)+'},')
        ech1 = (Echo1_num, Echo1_type, Echo1_height)
        if (Echo1_num-Echo0_num) > 0:
            echo_infos.append(ech1)

        Echo2_type = (Peak_List[3]>>2)&0x0001
        # print("Echo2_type:" + str(Echo2_type))
        Echo2_num = (((Peak_List[3]>>3)&0x001F) + Echo0_num)
        # print("Echo2_num:" + str(Echo2_num))
        Echo2_height = (((Peak_List[3]&0x0003)<<8) + (Peak_List[4]>>8))*16;
        # print("Echo2_height:" + str(Echo2_height))
        print('{' + str(Echo2_type)+',' + str(Echo2_num)+','+ str(Echo2_height)+'},')
        ech2 = (Echo2_num, Echo2_type, Echo2_height)
        if (Echo2_num-Echo0_num) > 0:
            echo_infos.append(ech2)

        Echo3_type = (Peak_List[4]>>2)&0x0001
        # print("Echo3_type:" + str(Echo3_type))
        Echo3_num = (((Peak_List[4]>>3)&0x001F) + Echo0_num)
        # print("Echo3_num:" + str(Echo3_num))
        Echo3_height = (((Peak_List[4]&0x0003)<<8) + (Peak_List[5]>>8))*16;
        # print("Echo3_height:" + str(Echo3_height))
        print('{' + str(Echo3_type)+',' + str(Echo3_num)+','+ str(Echo3_height)+'},')
        ech3 = (Echo3_num, Echo3_type, Echo3_height)
        if (Echo3_num-Echo0_num) > 0:
            echo_infos.append(ech3)

        Echo4_type = (Peak_List[5]>>2)&0x0001
        # print("Echo4_type:" + str(Echo4_type))
        Echo4_num = (((Peak_List[5]>>3)&0x001F) + Echo0_num)
        # print("Echo4_num:" + str(Echo4_num))
        Echo4_height = (((Peak_List[5]&0x0003)<<8) + (Peak_List[6]>>8))*16;
        # print("Echo4_height:" + str(Echo4_height))
        print('{' + str(Echo4_type)+',' + str(Echo4_num)+','+ str(Echo4_height)+'},')
        ech4 = (Echo4_num, Echo4_type, Echo4_height)
        if (Echo4_num-Echo0_num) > 0:
            echo_infos.append(ech4)

        Echo5_type = (Peak_List[6]>>2)&0x0001
        # print("Echo5_type:" + str(Echo5_type))
        Echo5_num = (((Peak_List[6]>>3)&0x001F) + Echo0_num)
        # print("Echo5_num:" + str(Echo5_num))
        Echo5_height = (((Peak_List[6]&0x0003)<<8) + (Peak_List[7]>>8))*32/2;
        # print("Echo5_height:" + str(Echo5_height))
        print('{' + str(Echo5_type)+',' + str(Echo5_num)+','+ str(Echo5_height)+'},')
        ech5 = (Echo5_num, Echo5_type, Echo5_height)
        if (Echo5_num-Echo0_num) > 0:
            echo_infos.append(ech5)

    return echo_infos