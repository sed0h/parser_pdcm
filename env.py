print("Hello python word")

Peak_List = [0x16f2,0x0002,0xf700,0x9600,0xb201,0x7002,0x7904,0x6fa9]
PyhAddr = Peak_List[0]>>12
print(PyhAddr)
FrameCounter = (Peak_List[0]>>8)&0x000F
print(FrameCounter)

Echo0_num = ((Peak_List[1]<<8)&0xFF00) + ((Peak_List[2]>>8)&0x00FF);
print("Echo0_num:" + str(Echo0_num))

Echo1_num = ((Peak_List[2]<<8)&0xFF00) + ((Peak_List[3]>>8)&0x00FF);
print("Echo1_num:" + str(Echo1_num))

Echo2_num = ((Peak_List[3]<<8)&0xFF00) + ((Peak_List[4]>>8)&0x00FF);
print("Echo2_num:" + str(Echo2_num))

Echo3_num = ((Peak_List[4]<<8)&0xFF00) + ((Peak_List[5]>>8)&0x00FF);
print("Echo3_num:" + str(Echo3_num))

Echo4_num = ((Peak_List[5]<<8)&0xFF00) + ((Peak_List[6]>>8)&0x00FF);
print("Echo4_num:" + str(Echo4_num))

Echo5_num = ((Peak_List[6]<<8)&0xFF00) + ((Peak_List[7]>>8)&0x00FF);
print("Echo5_num:" + str(Echo5_num))
