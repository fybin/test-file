
from flask import Flask, current_app, request
app = Flask(__name__)

a = current_app   # 如果调试， 这里会出现unbund未绑定
d = current_app.config['DEBUG']
