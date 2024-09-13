import RPi.GPIO as GPIO   #导入库
import time

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

# 可以通过更改括号内的数值改变电机转动的速度，数值范围0~100
def forward(time_sleep):   #正转几秒
    p1.start(0)
    p2.start(50)
    p3.start(0)
    p4.start(50)
    time.sleep(time_sleep)
    
def stop():  #停止
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)    

spin_count = 0
spin_count2 = 0
E1A = 20     #设置引脚
E1B = 21
E2A=26
E2B=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(E1B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(E1A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(E2B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(E2A, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def my_callback(channel): #回调函数
    global spin_count
    if GPIO.input(E1A):
        if not GPIO.input(E1B):
            spin_count += 1
        elif GPIO.input(E1B):
            spin_count -= 1
    print(spin_count)
    
def my_callback2(channel):
    global spin_count2
    if GPIO.input(E2A):
        if not GPIO.input(E2B):
            spin_count2 += 1
        elif GPIO.input(E2B):
            spin_count2 -= 1
    print(spin_count2)


GPIO.add_event_detect(E1A, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(E2A, GPIO.RISING, callback=my_callback2)

forward(5)   #正转5s
stop()     #停止