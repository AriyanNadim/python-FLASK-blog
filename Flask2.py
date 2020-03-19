from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy,os
from flask_mail import Mail
from datetime import datetime
from werkzeug import secure_filename
import math
import json
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(autoescape=select_autoescape(['html', 'xml']))


local_server = True  #on the local server
with open('config.json', 'r') as c:
    params = json.load(c)["params"]  #json configuration
app = Flask(__name__)




app.secret_key = 'SECRET_KEY'
app.config['UPLOAD_FOLDER']=params["upload_location"]

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)


# mysql://root:@localhost/Best_Blog_3'!'#connect to the database
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params[ 'local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
















# for contact  table in database
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(80), nullable=False)
    msg = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=True)


# for post  table in database
class postss(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    img_file = db.Column(db.String(12), nullable=True)
    date = db.Column(db.String(12), nullable=True)



@app.route('/')
def home():
    posts=postss.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['num_of_posts']))
    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['num_of_posts']):(page-1)*int(params['num_of_posts'])+int(params['num_of_posts'])]
    if (page==1):
        prev="#"
        next="/?page="+str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page-1)
        next ="#"
    else:
        prev = "/?page=" + str(page- 1)
        next = "/?page=" + str(page+ 1)

    return render_template('index.html',params=params,posts=posts,prev=prev,next=next)



#basic teplate to  show html page
@app.route('/about')
def about():
    return render_template('about.html', params=params)



@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = postss.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)




@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        posts = postss.query.all()
        return render_template('dashboard.html', posts=posts, params=params)

    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if (username== params['admin_user'] and userpass==params['admin_password']):
            session['user']=username
            posts=postss.query.all()
            return render_template('dashboard.html',params=params,posts=posts)
    return render_template('login.html', params=params)




@app.route("/edit1/<string:sno>",methods=['GET','POST'])
def edit1(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method =='POST':
            title = request.form.get('title')
            tagline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno=='0':
                t=postss(title=title,slug=slug,content=content,tagline=tagline,img_file=img_file,date=date)
                db.session.add(t)
                db.session.commit()
            else:
                t = postss.query.filter_by(sno=sno).first()
                t.title = title
                t.tagline = tagline
                t.slug = slug
                t.content = content
                t.img_file = img_file
                t.date = date
                db.session.commit()
                return redirect('/edit1/'+sno)
        t = postss.query.filter_by(sno=sno).first()
        return render_template('edit1.html', params=params, sno=sno,t=t)




@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post=postss.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard') #delete


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            f=request.files['datafile']
            f.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(f.filename)))
            return "Uploaded successfully"



@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')  # init table contacts
        message = request.form.get('message')

        # data entry to the database
        entry = Contacts(name=name, phone_num=phone, email=email, msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params=params)


app.run(debug=True)
