def extract_envelope_peaks(Envelop_Peak_List):
    envlps_peaks_info = []

    if ((Envelop_Peak_List[0] & 0x000F) == 8) or ((Envelop_Peak_List[0] & 0x000F) == 7) or ((Envelop_Peak_List[0] & 0x000F) == 9):
        PyhAddr = Envelop_Peak_List[0] >> 12
        # print(PyhAddr)
        FrameCounter = (Envelop_Peak_List[0] >> 8) & 0x000F
        # print(FrameCounter)

        EchoNum1 = (Envelop_Peak_List[1] >> 8)
        EchoTypes = (Envelop_Peak_List[1] & 0x00FC) >> 2
        EchoHight1 = (((Envelop_Peak_List[1] & 0x0003) << 8) | (((Envelop_Peak_List[2] & 0xFF00) >> 8)))*32
        if EchoHight1 > 0:
            echo1 = (EchoNum1, EchoHight1)
            envlps_peaks_info.append(echo1)
            print("Echo1: (" + str(EchoNum1) + ',' + str(EchoHight1) + ')')

        EchoNum2 = ((Envelop_Peak_List[2] & 0x00FC) >> 2) + EchoNum1
        EchoHight2 = (((Envelop_Peak_List[2] & 0x0003) << 8) | (((Envelop_Peak_List[3] & 0xFF00) >> 8)))*32
        if EchoHight2 > 0:
            echo2 = (EchoNum2, EchoHight2)
            envlps_peaks_info.append(echo2)
            print("Echo2: (" + str(EchoNum2) + ',' + str(EchoHight2) + ')')

        EchoNum3 = ((Envelop_Peak_List[3] & 0x00FC) >> 2) + EchoNum1
        EchoHight3 = (((Envelop_Peak_List[3] & 0x0003) << 8) | (((Envelop_Peak_List[4] & 0xFF00) >> 8)))*32
        if EchoHight3 > 0:
            echo3 = (EchoNum3, EchoHight3)
            envlps_peaks_info.append(echo3)
            print("Echo3: (" + str(EchoNum3) + ',' + str(EchoHight3) + ')')

        EchoNum4 = ((Envelop_Peak_List[4] & 0x00FC) >> 2) + EchoNum1
        EchoHight4 = (((Envelop_Peak_List[4] & 0x0003) << 8) | (((Envelop_Peak_List[5] & 0xFF00) >> 8)))*32
        if EchoHight4 > 0:
            echo4 = (EchoNum4, EchoHight4)
            envlps_peaks_info.append(echo4)
            print("Echo4: (" + str(EchoNum4) + ',' + str(EchoHight4) + ')')

        EchoNum5 = ((Envelop_Peak_List[5] & 0x00FC) >> 2) + EchoNum1
        EchoHight5 = (((Envelop_Peak_List[5] & 0x0003) << 8) | (((Envelop_Peak_List[6] & 0xFF00) >> 8)))*32
        if EchoHight5 > 0:
            echo5 = (EchoNum5, EchoHight5)
            envlps_peaks_info.append(echo5)
            print("Echo5: (" + str(EchoNum5) + ',' + str(EchoHight5) + ')')

        EchoNum6 = ((Envelop_Peak_List[6] & 0x00FC) >> 2) + EchoNum1
        EchoHight6 = ((Envelop_Peak_List[6] & 0x0003) << 8)*32 + ((Envelop_Peak_List[7] & 0xFF00) >> 8)*32
        if EchoHight6 > 0:
            echo6 = (EchoNum6, EchoHight6)
            envlps_peaks_info.append(echo6)
            print("Echo6: (" + str(EchoNum6) + ',' + str(EchoHight6) + ')')

    return envlps_peaks_info

