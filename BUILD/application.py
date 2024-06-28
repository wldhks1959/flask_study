from flask import Flask, render_template
import sys 
application = Flask(__name__)

@application.route("/") # 기본 페이지 
def hello():
    return render_template("hello.html")

@application.route("/apply") # apply
def apply():
    return render_template("apply.html")

@application.route("/list") # list
def list_items(): # list라는 함수 이름은 파이선 기본 메서드와 겹치니 list_items로 변경 
    return render_template("list.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')