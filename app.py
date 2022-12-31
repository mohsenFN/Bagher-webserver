#!/usr/bin/python

from flask import Flask
from flask import render_template, send_file
from flask import abort, request

from werkzeug.utils import secure_filename


app = Flask(__name__)


from dotenv import load_dotenv
import os

load_dotenv()

ip_address = os.getenv("ip_address_from_dotenv")
port_number = os.getenv("port_number_from_dotenv", 5000)

print(len (port_number) )

print(app.config['MAX_CONTENT_LENGTH'])

@app.route("/")
@app.route("/up")
def upload_func():
    return render_template("upload.html", ip_address=ip_address,port_number=port_number)


@app.route("/uploader", methods = ["GET","POST"])
def uploader():
    if request.method == "POST":
        print("before getting files as list")
        print(request.stream.tell())
        uped_files = request.files.getlist("file")

        print(uped_files)
        for uped_file in uped_files:    
            try:
                print("started saving file")
                uped_file.save(f"../server_files/{uped_file.filename}")

            except IsADirectoryError:
                return "<b>No file is selected</b>"
    

    return f"Done <br> Check <a href='http://{ip_address}:{str(port_number)}/server_files'>Here</a><br><hr><a href='http://{ip_address}:{str(port_number)}/'>Upload Again</a>"


@app.route("/<path:req_path>")
def index_files_func(req_path):
    base_dir = "../"
    abs_path = os.path.join(base_dir, req_path)
    
    if not os.path.exists(abs_path):
        return f"{abs_path}"
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    return render_template("index_files.html", files=files)



if __name__ == "__main__":
    app.run(host=ip_address, port=port_number, debug=True)
