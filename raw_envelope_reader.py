def extract_envelope(Envelop_Peak_List):
    # print("Hello python word")
    env_infos = []

    if ((Envelop_Peak_List[0] & 0x000F) == 8) or ((Envelop_Peak_List[0] & 0x000F) == 7) or ((Envelop_Peak_List[0] & 0x000F) == 9):
        PyhAddr = Envelop_Peak_List[0] >> 12
        # print(PyhAddr)
        FrameCounter = (Envelop_Peak_List[0] >> 8) & 0x000F
        print(FrameCounter)

        Echo0_height = ((Envelop_Peak_List[1] << 8) & 0xFF00) + ((Envelop_Peak_List[2] >> 8) & 0x00FF);
        print("Echo0_num:" + str(Echo0_height))
        ech0 = (0, Echo0_height)
        env_infos.append(ech0)

        Echo1_height = ((Envelop_Peak_List[2] << 8) & 0xFF00) + ((Envelop_Peak_List[3] >> 8) & 0x00FF);
        print("Echo1_num:" + str(Echo1_height))
        ech1 = (1, Echo1_height)
        env_infos.append(ech1)

        Echo2_height = ((Envelop_Peak_List[3] << 8) & 0xFF00) + ((Envelop_Peak_List[4] >> 8) & 0x00FF);
        print("Echo2_num:" + str(Echo2_height))
        ech2 = (2, Echo2_height)
        env_infos.append(ech2)
        
        Echo3_height = ((Envelop_Peak_List[4] << 8) & 0xFF00) + ((Envelop_Peak_List[5] >> 8) & 0x00FF);
        print("Echo3_num:" + str(Echo3_height))
        ech3 = (3, Echo3_height)
        env_infos.append(ech3)

        Echo4_height = ((Envelop_Peak_List[5] << 8) & 0xFF00) + ((Envelop_Peak_List[6] >> 8) & 0x00FF);
        print("Echo4_num:" + str(Echo4_height))
        ech4 = (4, Echo4_height)
        env_infos.append(ech4)

        Echo5_height = ((Envelop_Peak_List[6] << 8) & 0xFF00) + ((Envelop_Peak_List[7] >> 8) & 0x00FF);
        print("Echo5_num:" + str(Echo5_height))
        ech5 = (5, Echo5_height)
        env_infos.append(ech5)

    return env_infos
