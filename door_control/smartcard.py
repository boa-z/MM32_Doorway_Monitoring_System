from smartcard.System import readers
from smartcard.util import toHexString

def read_smartcard_card_number():
    try:
        # 获取读卡器列表
        reader_list = readers()
        if not reader_list:
            print("未找到读卡器")
            return None

        # 获取第一个读卡器并连接
        reader = reader_list[0]
        connection = reader.createConnection()
        connection.connect()

        # 发送APDU命令来获取卡号，具体的APDU命令根据智能卡的类型而定
        # 这里的APDU命令是一个示例，具体的命令需要根据智能卡的厂商和卡号编码规则进行调整
        apdu_command = [0x00, 0xB0, 0x00, 0x00, 0x0A]  # 示例命令
        response, sw1, sw2 = connection.transmit(apdu_command)

        if sw1 == 0x90 and sw2 == 0x00:
            # 提取卡号并转换为字符串
            card_number = toHexString(response)
            return card_number
        else:
            print("无法读取智能卡卡号")
            return None

    except Exception as e:
        print("读取智能卡卡号时出现错误:", str(e))
        return None

if __name__ == "__main__":
    card_number = read_smartcard_card_number()
    if card_number:
        print("智能卡卡号:", card_number)