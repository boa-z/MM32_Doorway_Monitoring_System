# 2023全国大学生物联网设计竞赛

## 题目

[2023年全国大学生物联网设计竞赛（华为杯）命题](http://iot.sjtu.edu.cn/show.aspx?info_lb=36&info_id=3921&flag=2)

命题2（安谋科技命题）

使用国产灵动微电子 MM32F5270 微控制器作为主要平台，完成作品的设计与开发。MM32F5270 系列微控制器是上海灵动微电子设计生产的搭载了安谋科技（Arm China）“星辰” STAR-MC1 处理器的 MCU 产品，其工作频率可达 120MHz，内置256KB Flash 和 192KB RAM，配置浮点运算单元（Floating Point Unit, FPU）、数字信号处理单元（Digital Signal Processing，DSP）、信号间互联矩阵 MindSwitch、可配置逻辑单元 CLU、三角函数加速单元 CORDIC等算法加速单元，并集成了丰富的外设模块和充足的 I/O 端口。MM32F5270 相较于现有产品全面提升了性能、存储容量、总线架构和外设配置，旨在覆盖更广泛的工业、汽车和 IoT 应用。

![5.png](http://iot.sjtu.edu.cn/ueditor/net/upload/image/20230403/6381613174308900786147481.png)
图1 使用“星辰”STAR-MC1处理器的MM32F5270微控制器产品选型
MM32F0140 系列微控制器是上海灵动微电子设计生产的搭载Arm Cortex-M0微控内核的 MCU 产品，其工作频率可达72MHz，内置64KB Flash和8KB RAM，集成常规的定时器、通信类外设，以及模拟外设模块等。特别地，其部分型号还集成了FlexCAN总线通信引擎，可以实现接入CAN网络的设备节点。

![6.png](http://iot.sjtu.edu.cn/ueditor/net/upload/image/20230403/6381613175967683042576626.png)
图2 集成FlexCAN外设模块的MM32F0140微控制器产品选型

【赛题任务】
请参赛队基于 MM32F5270 微控制器，实现下列题目的一个：

（1）IoT智门口道监控系统

* 使用 MM32F5270 微控制器作为主控芯片。
* 使用MindSDK或MicroPython作为软件开发平台。
* 通过中远距离接近传感器（毫米波雷达、dToF、红外接近传感器、摄像头或其他），检测是否有人通过门口的检测区域（暂定义为前后1-2M范围，模拟一个走廊）使得灯光亮起照射检测区域。
* 在门口刷卡、密码正确则可开门。
* 监控系统在门口停留超过10秒后发出警告，并通过无线通信网络传输模块（4G、Wifi、BLE、ZigBee等），将监控数据上传至云端。
* 云端数据库保存每次开门、警报的记录。
* 加分项：通过语音警告、实现云台的自动跟随、捕获图像数据上传至云端、捕获图像数据保存在本地、通过微信小程序或者网页在云端实现超控等。

【注意事项】

（1）基于 MM32F5270 / MM32F0140 微控制器平台进行开发，不限定使用灵动官方提供的软件包：

* 参赛者可以使用 C 语言基于 MindSDK 进行开发。
* 参赛者可以使用 Python 语言基于预编译的 MicroPython 进行开发。
* 参赛者可以在 C 语言层面上对 MicroPython 进行二次开发，增加更多的类组件，以支撑实现参赛任务的功能。

（2）需要参赛者自行实现参赛作品的机械结构设计，推荐但不限定使用 3D 打印技术。
（3）参赛者提交能够复现作品的完整参赛资料，包括描述参赛作品的实现原理和关键技术的技术报告，完整的源程序代码、PCB工程等。

## 购买的硬件

* [MM32F5270](https://www.mindmotion.com.cn/products/mm32mcu/mm32f/mm32f_performance/mm32f5270/)
* oranegpi 5
* [MFRC-522 RC522 RFID射频IC卡感应模块刷卡读卡 送S50复旦卡](https://detail.tmall.com/item.htm?ali_refid=a3_430582_1006:1106005875:N:gqL%20DTLSaVcwiFxwIPt6QFttIGZ5/0H4:3c6e9e14af4ab415bebc02b419444745&ali_trackid=1_3c6e9e14af4ab415bebc02b419444745&id=19577018810)
* [24G雷达模组FMCW测距人体存在感应毫米波雷达串口通信模块](https://item.taobao.com/item.htm?spm=a230r.1.14.11.55c85195bGS8aF&id=713159647387&ns=1&abbucket=15#detail)
* ESP32-CAM
