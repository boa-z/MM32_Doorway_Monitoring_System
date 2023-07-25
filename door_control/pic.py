import time
import wiringpi; 
from wiringpi import GPIO; 
import cv2
wiringpi.wiringPiSetup() ; 

# 设置要监测的 GPIO 引脚号
gpio_pin_in = 11
wiringpi.pinMode(gpio_pin_in, GPIO.IN)

# 设置另一个 GPIO 引脚为输出模式
gpio_pin_output = 13
wiringpi.pinMode(gpio_pin_output, GPIO.OUT)

# 连接 USB 摄像头
camera = cv2.VideoCapture(0)

# 用于条件3的标志位和开始时间
flag_condition_3 = False
condition_3_start_time = 0

def trigger_condition_1():
    print("条件1被触发！")
    # 拍摄照片并保存为 "door.jpg"
    return_value, image = camera.read()
    if return_value:
        cv2.imwrite("door.jpg", image)
        print("照片已拍摄并保存为 door.jpg")
    else:
        print("无法拍摄照片")

def trigger_condition_2():
    print("条件2被触发！")
    # 设置另一个 GPIO 引脚为高电平
    wiringpi.digitalWrite(gpio_pin_output, GPIO.HIGH)

def trigger_condition_3():
    print("条件3被触发！")

def main():
    high_start_time = None
    global flag_condition_3, condition_3_start_time

    while True:
        # 监测 GPIO 的状态
        input_state = GPIO.input(gpio_pin)

        # GPIO 为高电平时
        if input_state == GPIO.HIGH:
            # 记录高电平的开始时间
            if high_start_time is None:
                high_start_time = time.time()
                
            # 检查条件3触发状态
            if flag_condition_3:
                flag_condition_3 = False  # 重置条件3触发状态
                trigger_condition_3()

        else:
            # 重置高电平开始时间，并将另一个 GPIO 引脚设为低电平
            high_start_time = None
            wiringpi.digitalWrite(gpio_pin_output, GPIO.LOW)

            # 检测条件3是否满足
            if time.time() - condition_3_start_time >= 10:
                flag_condition_3 = True

        # 触发条件 1
        if high_start_time is not None and time.time() - high_start_time >= 10:
            trigger_condition_1()

        # 触发条件 2
        if high_start_time is not None and time.time() - high_start_time >= 15:
            trigger_condition_2()

        # 适当添加延迟，以降低 CPU 占用
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("程序已终止")
    finally:
        # 释放摄像头资源并将另一个 GPIO 引脚设为低电平
        camera.release()
        GPIO.output(gpio_pin_output, GPIO.LOW)
        GPIO.cleanup()
