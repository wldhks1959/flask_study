from flask import Flask, render_template, request, redirect, url_for
import sys 
application = Flask(__name__)

@application.route("/") # 기본 페이지 
def hello():
    return render_template("hello.html")

@application.route("/apply") # apply
def apply():
    return render_template("apply.html")

@application.route("/applyPhoto") # apply
def applyPhoto():
    location =  request.args.get("location")
    clean = request.args.get("clean")
    built_in = request.args.get("built")
    print(location, clean, built_in)
    return render_template("photo.html")

@application.route("/upload_done", methods=["POST"]) # apply
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(1))

    return redirect(url_for("hello")) # hello라는 함수로 리다이렉트 
    

@application.route("/list") # list
def list_items(): # list라는 함수 이름은 파이선 기본 메서드와 겹치니 list_items로 변경 
    return render_template("list.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')