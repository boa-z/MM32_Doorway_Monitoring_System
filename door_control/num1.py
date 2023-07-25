import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QMessageBox, QInputDialog
from functools import partial
import wiringpi; 
from wiringpi import GPIO; 
wiringpi.wiringPiSetup() ; 
wiringpi.pinMode(2, GPIO.OUTPUT) ; 
class NumberInputWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.NUM = None
        self.MAX_DIGITS = 4  # Set the maximum number of digits
        self.password_file = "password.txt"  # File to store the password
        self.PRESET_PASSWORD = self.load_password()

        self.init_ui()

    def init_ui(self):
        # 设置窗口标题
        self.setWindowTitle("Door password")

        layout = QVBoxLayout()

        # 创建一个 QLineEdit 用于输入数字
        self.number_input = QLineEdit(self)
        layout.addWidget(self.number_input)

        # 创建数字按钮的布局
        num_layout = QGridLayout()

        num_buttons = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "0"
        ]

        # 将数字按钮添加到布局中
        row, col = 0, 0
        for btn_text in num_buttons:
            button = QPushButton(btn_text, self)
            button.clicked.connect(partial(self.on_num_button_clicked, btn_text))
            num_layout.addWidget(button, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # 添加"确认"按钮
        confirm_button = QPushButton("确认", self)
        confirm_button.clicked.connect(partial(self.on_num_button_clicked, "确认"))
        num_layout.addWidget(confirm_button, 3, 1)

        # 添加"退格"按钮
        backspace_button = QPushButton("退格", self)
        backspace_button.clicked.connect(self.on_backspace_button_clicked)
        num_layout.addWidget(backspace_button, 3, 2)


        # 添加"设置密码"按钮
        set_password_button = QPushButton("设置密码", self)
        set_password_button.clicked.connect(self.on_set_password_button_clicked)
        num_layout.addWidget(set_password_button, 5, 1, 1, 2)

        layout.addLayout(num_layout)

        # 设置布局
        self.setLayout(layout)

    def on_num_button_clicked(self, char):
        if char == "确认":
            # 获取 QLineEdit 中的文本并尝试转换为数字
            try:
                self.NUM = int(self.number_input.text())
            except ValueError:
                # 如果无法转换为数字，将 NUM 设置为 None
                self.NUM = None
            finally:
                # 清空输入框
                self.number_input.setText("")

            # 显示提示框
            message_box = QMessageBox()
            if self.NUM is not None:
                if self.NUM == self.PRESET_PASSWORD:
                    message_box.setText("密码正确！门已解锁。")
                    wiringpi.digitalWrite(2, GPIO.HIGH)
                    time.sleep(5)
                    wiringpi.digitalWrite(2, GPIO.LOW)
                else:
                    message_box.setText("密码错误！请重试。")
            else:
                message_box.setText("未输入有效的数字。")
            message_box.exec_()

        else:
            current_text = self.number_input.text()
            if len(current_text) < self.MAX_DIGITS:
                self.number_input.setText(current_text + char)
            elif len(current_text) == self.MAX_DIGITS:
                # Automatically trigger the "确认" action when the input reaches the specified digit limit
                self.on_num_button_clicked("确认")

    def on_backspace_button_clicked(self):
        current_text = self.number_input.text()
        self.number_input.setText(current_text[:-1])

    def on_change_password_button_clicked(self):
        new_password, ok = QInputDialog.getInt(self, "修改密码", "请输入新的密码:", self.PRESET_PASSWORD, 0, 9999)
        if ok:
            self.PRESET_PASSWORD = new_password
            self.save_password()

    def on_set_password_button_clicked(self):
        current_password, ok = QInputDialog.getInt(self, "设置密码", "请输入当前密码:", 0, 0, 9999)
        if ok:
            if current_password == self.PRESET_PASSWORD:
                new_password, ok = QInputDialog.getInt(self, "设置密码", "请输入新的密码:", 0, 0, 9999)
                if ok:
                    self.PRESET_PASSWORD = new_password
                    self.save_password()
            else:
                message_box = QMessageBox()
                message_box.setText("当前密码错误！无法设置新密码。")
                message_box.exec_()

    def load_password(self):
        if os.path.exists(self.password_file):
            with open(self.password_file, "r") as file:
                try:
                    return int(file.read())
                except ValueError:
                    pass
        # Return the default password if the file doesn't exist or an error occurred
        return 1234

    def save_password(self):
        with open(self.password_file, "w") as file:
            file.write(str(self.PRESET_PASSWORD))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NumberInputWidget()
    window.show()

    sys.exit(app.exec_())
