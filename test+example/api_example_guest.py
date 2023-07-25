import requests

data = {
    'card_number': '1234567890',
    'guest_name': '张三',
    'guest_type': 'VIP',
    'guest_login_type': 1
}

# 定义要post的url，这里只是一个例子，你可以根据你的实际url进行修改
url = 'http://127.0.0.1:5000/guests'

# 发送post请求，并获取响应
response = requests.post(url, json=data)

# 打印响应的状态码和内容
print(response.status_code)
print(response.json())
