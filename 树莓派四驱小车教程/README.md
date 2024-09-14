# 四驱车教程

## 1.学前知识
1. **树莓派**：树莓派树莓派是一款高级的微型计算机，可以烧录像windows一样的图像界面系统，也可以像单片机一样直接控制IO口。
2. **直流有刷电机**：是最常见的电机，转速高低由电压控制。具有两个端口，改变电压输入方向，即可完成电机换向。
3. **霍尔编码器**：霍尔元件制作，专门用于记录轮子转的圈数之类的信息，用以计算速度。
4. **双路电机驱动板**：树莓派的IO口不能流过太大的电流，因此驱动电机的电流还需要驱动板提供。这块驱动板能驱动两个电机

<sub>树莓派与驱动板接线</sub>

![树莓派与驱动板接线](树莓派与驱动板接线图.png)


<sub>驱动板引脚功能图</sub>

![驱动板引脚功能图](驱动板引脚功能图.png)


## 2.代码解释

---
>设置使用的引脚编码
```
GPIO.setmode(GPIO.BCM)    #设置引脚编码
```
树莓派引脚有不同编码方式（BCM，wiringPi，BOARD），这里选择BCM编码

![引脚编码](https://github.com/user-attachments/assets/ab783865-609b-42b0-87c3-e98111dbfa81)

>定义A，B电机的输入引脚（决定树莓派的哪几个引脚来控制电机）
```
AIN1 = 17
AIN2 = 18
BIN1 = 22
BIN2 = 23
```

---
>配置引脚
```
GPIO.setwarnings(False)     #消除警告信息输出，让输出内容更干净

GPIO.setup(AIN1, GPIO.OUT)   #引脚设置为输出，电流信号从树莓派流出
p1 = GPIO.PWM(AIN1, 50)  # 这里的50是频率为50Hz
p1.start(0)  #使该引脚以0的占空比输出
```
`PWM（Pulse Width Modulation，脉宽调制）`是一种控制信号的方法，通过调节一个周期信号（一般是方波信号），实现等效电压的调节。占空比即一个周期内，高电平时间与周期时间的比值，0%~100%。
![PWM图解](https://github.com/user-attachments/assets/99a8c37e-6190-474c-93eb-91c5bd181318)

---
>驱动电机
```
# 可以通过更改括号内的数值改变电机转动的速度，数值范围0~100
def forward(time_sleep):   #正转几秒
    p1.start(0)
    p2.start(50)
    p3.start(0)
    p4.start(50)
    time.sleep(time_sleep) #time.sleep是延时函数，变量time_sleep单位为秒。
    
def stop():  #停止
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
```

---
>配置编码器读取引脚和使用
```
E1A=20     #设置引脚
E1B=21
E2A=26
E2B=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(E1B, GPIO.IN, pull_up_down=GPIO.PUD_UP) #这里由于要接受霍尔编码器发送来的数据，因此引脚配置为输入模式
GPIO.setup(E1A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(E2B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(E2A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
```
`pull_up_down=GPIO.PUD_UP`是可选参数，这个参数用于指定是否对引脚启用上拉或下拉电阻，可以理解为，引脚在没有输入信号时，默认保持低电平还是高电平。如果不写这个参数，引脚在未连接设备时处于“悬空”状态，由于电路内部本身的干扰，从而造成不稳定的信号。

---
>配置事件检测机制（中断函数）
```
spin_count = 0
def my_callback(channel): #回调函数
    global spin_count
    if GPIO.input(E1A):
        if not GPIO.input(E1B):
            spin_count += 1
        elif GPIO.input(E1B):
            spin_count -= 1
    print(spin_count)  #print函数可以把变量打印到控制台，方便调试和查看

GPIO.add_event_detect(E1A, GPIO.RISING, callback=my_callback)
```
`spin_count`用来记录霍尔编码器发送过来的脉冲的数量，若继续修改即可得到电机速度函数。

`GPIO.add_event_detect(E1A, GPIO.RISING, callback=my_callback)`中断函数配置。
- `E1A`：这是你希望检测的引脚编号。
- `GPIO.RISING`：表示你希望检测信号的上升沿，即从低电平（0V）变为高电平（3.3V）。还有其他选项，比如 GPIO.FALLING（下降沿）或 GPIO.BOTH（同时检测上升沿和下降沿）。
- `callback=my_callback`：当检测到事件时，执行 my_callback 函数，这里 my_callback 是用户定义的函数。
