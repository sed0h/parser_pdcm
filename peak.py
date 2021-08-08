print("Hello python word")

Peak_List = [0x16f1, 0x1d00, 0x4a14, 0xaf18, 0x8618, 0x8624, 0x8c58, 0x2139]
PyhAddr = Peak_List[0]>>12
print(PyhAddr)
FrameCounter = (Peak_List[0]>>8)&0x000F
print(FrameCounter)

Echo0_num = Peak_List[1]>>7;
print("Echo0_num:" + str(Echo0_num))
Echo0_type = (Peak_List[1]>>2)&0x0001
print("Echo0_type:" + str(Echo0_type))
Echo0_height = (((Peak_List[1]&0x0003)<<8) + Peak_List[2]>>8)*32;
print("Echo0_height:" + str(Echo0_height))

Echo1_num = (((Peak_List[2]>>3)&0x001F) + Echo0_num)
print("Echo1_num:" + str(Echo1_num))
Echo1_type = (Peak_List[2]>>2)&0x0001
print("Echo1_type:" + str(Echo1_type))
Echo1_height = (((Peak_List[2]&0x0003)<<8) + Peak_List[3]>>8)*32;
print("Echo1_height:" + str(Echo1_height))

Echo2_num = (((Peak_List[3]>>3)&0x001F) + Echo0_num)
print("Echo2_num:" + str(Echo2_num))
Echo2_type = (Peak_List[3]>>2)&0x0001
print("Echo2_type:" + str(Echo2_type))
Echo2_height = (((Peak_List[3]&0x0003)<<8) + Peak_List[4]>>8)*32;
print("Echo2_height:" + str(Echo2_height))

Echo3_num = (((Peak_List[4]>>3)&0x001F) + Echo0_num)
print("Echo3_num:" + str(Echo3_num))
Echo3_type = (Peak_List[4]>>2)&0x0001
print("Echo3_type:" + str(Echo3_type))
Echo3_height = (((Peak_List[4]&0x0003)<<8) + Peak_List[5]>>8)*32;
print("Echo3_height:" + str(Echo3_height))

Echo4_num = (((Peak_List[5]>>3)&0x001F) + Echo0_num)
print("Echo4_num:" + str(Echo4_num))
Echo4_type = (Peak_List[5]>>2)&0x0001
print("Echo4_type:" + str(Echo4_type))
Echo4_height = (((Peak_List[5]&0x0003)<<8) + Peak_List[6]>>8)*32;
print("Echo4_height:" + str(Echo4_height))

Echo5_num = (((Peak_List[6]>>3)&0x001F) + Echo0_num)
print("Echo5_num:" + str(Echo5_num))
Echo5_type = (Peak_List[6]>>2)&0x0001
print("Echo5_type:" + str(Echo5_type))
Echo5_height = (((Peak_List[6]&0x0003)<<8) + Peak_List[7]>>8)*32;
print("Echo5_height:" + str(Echo5_height))
