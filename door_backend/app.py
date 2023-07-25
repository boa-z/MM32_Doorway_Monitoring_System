from flask import Flask, request
from flask_cors import CORS
from flask.views import MethodView

from extension import db
from models import Guest, User, Alarm

import base64
import datetime

from flask import send_file
import io

app = Flask(__name__)
CORS().init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guests.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alarms.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Guest.init_db()
    User.init_db()


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome Guests!'

class GuestApi(MethodView):
    def get(self, guest_id):
        if not guest_id:
            guests: [Guest] = Guest.query.all()
            results = [
                {
                    'id': guest.id,
                    'card_number': guest.card_number,
                    'guest_name': guest.guest_name,
                    'guest_type': guest.guest_type,
                    'guest_time': guest.guest_time,
                    'guest_login_type': guest.guest_login_type,
                } for guest in guests
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        guest: Guest = Guest.query.get(guest_id)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': guest.id,
                'card_number': guest.card_number,
                'guest_name': guest.guest_name,
                'guest_type': guest.guest_type,
                'guest_time': guest.guest_time,
                'guest_login_type': guest.guest_login_type,
            }
        }

    def post(self):
        form = request.json
        guest = Guest()
        guest.card_number = form.get('card_number')
        guest.guest_name = form.get('guest_name')
        guest.guest_type = form.get('guest_type')
        guest.guest_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 获取当前时间
        guest.guest_login_type = form.get('guest_login_type')
        db.session.add(guest)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, guest_id):
        guest = Guest.query.get(guest_id)
        db.session.delete(guest)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据删除成功'
        }

    def put(self, guest_id):
        guest: Guest = Guest.query.get(guest_id)
        guest.card_number = request.json.get('card_number')
        guest.guest_name = request.json.get('guest_name')
        guest.guest_type = request.json.get('guest_type')
        guest.guest_time = request.json.get('guest_time')
        guest.guest_login_type = request.json.get('guest_login_type')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }

class UserApi(MethodView):
    def get(self, user_id):
        if not user_id:
            users: [User] = User.query.all()
            results = [
                {
                    'id': user.id,
                    'card_number': user.card_number,
                    'guest_name': user.guest_name,
                    'guest_type': user.guest_type,
                } for user in users
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        user: User = User.query.get(user_id)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': user.id,
                'card_number': user.card_number,
                'guest_name': user.guest_name,
                'guest_type': user.guest_type,
            }
        }
    def post(self):
        form = request.json
        user = User()
        user.card_number = form.get('card_number')
        user.guest_name = form.get('guest_name')
        user.guest_type = form.get('guest_type')
        db.session.add(user)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据删除成功'
        }
    
    def put(self, user_id):
        user: User = User.query.get(user_id)
        user.card_number = request.json.get('card_number')
        user.guest_name = request.json.get('guest_name')
        user.guest_type = request.json.get('guest_type')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }

# 下面是一个使用 flask 写的 RESTful API 的例子，用于管理数据表 Alarm 的数据。

class AlarmApi(MethodView):
    # 请修改代码 get 方法用于查询数据，如果不传入 alarm_id，则返回所有数据，如果传入 alarm_id，则返回对应的数据。将 alarm_photo 中的二进制数据转化为 jpg 图片。
    def get(self, alarm_id):
        if not alarm_id:
            alarms: [Alarm] = Alarm.query.all()
            results = [
                {
                    'id': alarm.id,
                    'alarm_time': alarm.alarm_time,
                    'alarm_photo': 'http://127.0.0.1:5000/alarms/%s/file' % alarm.id,
                } for alarm in alarms
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        alarm: Alarm = Alarm.query.get(alarm_id)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': alarm.id,
                'alarm_time': alarm.alarm_time,
                'alarm_photo': 'http://127.0.0.1:5000/alarms/%s/file' % alarm.id,
            }
        }
    
    # 请修改代码 post 方法，用于添加数据。
    # 将 request data 中的内容转化为二进制数据并保存在 alarm_photo 中。
    # alarm_time 为 接收到数据的时间。
    def post(self):
        # if not (request.content_type.startswith('image/jpeg') or request.content_type.startswith('image/png')): # 判断图片格式
        #     return {'status': 'error', 'message': 'The image format is incorrect'}
        # form = request.json
        alarm = Alarm()
        alarm.alarm_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 获取当前时间
        print (request.files) # 打印请求中的文件参数
        image = request.files.get("image") # 获取图片文件
        print (image) # 打印文件对象
        alarm.alarm_photo = image.read() # 读取二进制数据
        db.session.add(alarm)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }
    
    def delete(self, alarm_id):
        alarm = Alarm.query.get(alarm_id)
        db.session.delete(alarm)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据删除成功'
        }
    
    def put(self, alarm_id):
        alarm: Alarm = Alarm.query.get(alarm_id)
        alarm.alarm_time = request.json.get('alarm_time')
        alarm.alarm_photo = request.json.get('alarm_photo')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }
    
class FileApi(MethodView):
    # 修改下面的代码，用于返回 alarm_photo 的二进制数据，由于json大小限制，请直接返回二进制数据。
    def get(self, alarm_id):
        if not alarm_id:
            alarms: [Alarm] = Alarm.query.all()
            results = [
                {
                    'alarm_photo': alarm.alarm_photo,
                } for alarm in alarms
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        alarm: Alarm = Alarm.query.get(alarm_id)
        return send_file(
            io.BytesIO(alarm.alarm_photo),
            mimetype='image/jpeg',
        )

guest_api = GuestApi.as_view('guest_api')
user_api = UserApi.as_view('user_api')
alarm_api = AlarmApi.as_view('alarm_api')
alarm_file_api = FileApi.as_view('alarm_file_api')
app.add_url_rule('/guests', view_func=guest_api, methods=['GET', ], defaults={'guest_id': None})
app.add_url_rule('/guests', view_func=guest_api, methods=['POST', ])
app.add_url_rule('/guests/<int:guest_id>', view_func=guest_api, methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/users', view_func=user_api, methods=['GET', ], defaults={'user_id': None})
app.add_url_rule('/users', view_func=user_api, methods=['POST', ])
app.add_url_rule('/users/<int:user_id>', view_func=user_api, methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/alarms', view_func=alarm_api, methods=['GET', ], defaults={'alarm_id': None})
app.add_url_rule('/alarms', view_func=alarm_api, methods=['POST', ])
app.add_url_rule('/alarms/<int:alarm_id>', view_func=alarm_api, methods=['GET', 'PUT', 'DELETE'])
app.add_url_rule('/alarms/<int:alarm_id>/file', view_func=alarm_file_api, methods=['GET', ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)