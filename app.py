from flask import (
    Flask,
    render_template,
    send_file,
    url_for,
    redirect,
    abort,
    request,
    json
)
from flask_login import current_user
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils import machine_local_ip, storage_init
import os


'''
This function will make a storage directory if not exists
You can use 'custom_storage_dir' function based in storage_init module to set a custom storage dir
'''
storage_init.init()

ip_address = machine_local_ip.get_local_ipv4()
port_number = 80 
username = "admin"
password = "admin"
secret = "MohsenFoolad"
files_dir = storage_init.init()[1]
files_dir_name = storage_init.init()[0]

login_manager = flask_login.LoginManager()


app = Flask(__name__)
app.secret_key  = secret
login_manager.init_app(app)

users = {username : {'password' : password}}
print(app.config['MAX_CONTENT_LENGTH'])

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["484 per day", "48 per hour"],
    storage_uri="memory://",
)



class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return render_template('upload.html', logged_in = True, ip_address=ip_address,port_number=port_number, files_dir_name=files_dir_name)

    return render_template("login.html", error = "Invalid Data !")


@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template("index_files.html")



@app.route('/logout')
def logout():
    flask_login.logout_user()
    return render_template("upload.html", ip_address=ip_address,port_number=port_number, message = "Logged out.")

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("unauth.html")


@app.route("/")
@app.route("/up")
def upload_func():
    if current_user.is_authenticated == False:
        return render_template("upload.html", ip_address=ip_address,port_number=port_number)
    else:
        return render_template("upload.html", ip_address=ip_address,port_number=port_number, logged_in = True, )



@app.route("/uploader", methods = ["GET","POST"])
def uploader():
    if request.method == "POST":
        # ! IMPORTANT NOTE FOR CONTRIBUTERS !
        # Even stream tell is not really a good method for uploading big files
        # IF YOU KNOW ANY GOOD METHOD PLEASE BE IN TOUCH !!!!!
        uped_files = request.files.getlist("file")
        print(uped_files)
        for uped_file in uped_files:    
            try:
                print("started saving file")
                uped_file.save(f"{files_dir}{uped_file.filename}")

            except IsADirectoryError:
                return render_template("upload.html", ip_address=ip_address,port_number=port_number, message = "No file is selected !")
    

    return render_template("up_done.html")


@app.route("/<path:req_path>")
@flask_login.login_required
def index_files_func(req_path):
    base_dir = "../"
    abs_path = os.path.join(base_dir, req_path)
    
    print(abs_path)
    if not os.path.exists(abs_path):
        return f"{abs_path}"
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    print(files)
    return render_template("index_files.html", files=files)







if __name__ == "__main__":
    app.run(host=ip_address, port=port_number, debug=True)
