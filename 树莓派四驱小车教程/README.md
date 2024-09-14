# 四驱车教程

## 学前知识
1. **树莓派**：树莓派树莓派是一款高级的微型计算机，可以烧录像windows一样的图像界面系统，也可以像单片机一样直接控制IO口。
2. **直流有刷电机**：是最常见的电机，通过换向器换向，转速高低由电压控制。
3. **霍尔编码器**：霍尔元件制作，专门用于记录轮子转的圈数之类的信息，用以计算速度。
4. **电机驱动板**：树莓派的IO口不能流过太大的电流，因此驱动电机的电流还需要驱动板提供。

树莓派与驱动板接线
![树莓派与驱动板接线](树莓派与驱动板接线图.png)

驱动板引脚功能图
![驱动板引脚功能图](驱动板引脚功能图.png)

代码解释
''' 
GPIO.setmode(GPIO.BCM)    #设置引脚
AIN1 = 17
AIN2 = 18
BIN1 = 22
BIN2 = 23

GPIO.setwarnings(False)     #消除警告
GPIO.setup(AIN1, GPIO.OUT)   #引脚设置为输出
p1 = GPIO.PWM(AIN1, 50)  # 这里的50是频率为50Hz
p1.start(0)

GPIO.setup(AIN2, GPIO.OUT)
p2 = GPIO.PWM(AIN2, 50)
p2.start(0)

GPIO.setup(BIN1, GPIO.OUT)
p3 = GPIO.PWM(BIN1, 50)
p3.start(0)

GPIO.setup(BIN2, GPIO.OUT)
p4 = GPIO.PWM(BIN2, 50)
p4.start(0)
'''


