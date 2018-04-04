#!/usr/bin/env python

from flask import Flask,request,escape,session,redirect,url_for,render_template,make_response
from flask import jsonify
import sqlite3
import time
import jieba

app = Flask(__name__)


#用户注册表单数据过滤函数
def saferegister(req):
    not_safe = ['/','\\','*','#','$','^',')','(','+','-','%','!','~','?','[',']','{','}','<','>','=']
    email_need = ['@','.']
    email = req.form['email']
    password = req.form['password']
    repeate = req.form['repeate']
    if password == repeate:
        if email_need[0] in email:
            if email_need[1] in email:
                for x in not_safe:
                    if x in email:
                        return False
                        break
                    else:
                        if x in password:
                            return False
                            break
                        else:
                            return True
            else:
                return False
        else:
            return False


#用户登陆数据过旅函数
def safelogin(req):
    not_safe = ['/','\\','*','#','$','^',')','(','+','-','%','!','~','?','[',']','{','}','<','>','=']
    email_need = ['@','.']
    email = req.form['email']
    password = req.form['password']
    if email_need[0] in email:
        if email_need[1] in email:
            for x in not_safe:
                if x in email:
                    return False
                    break
                else:
                    if x in password:
                        return False
                        break
                    else:
                        return True
    else:
        return False

#bbs过滤函数
def safebbs(req):
    not_safe=['/','\\','*','#','$','^',')','(','+','-','%','!','~','?','[',']','{','}','<','>','=']
    theme = req.form['theme']
    content = req.form['content']
    for x in not_safe:
        if x in theme:
            return False
            break
        else:
            if x in content:
                return False
                break
            else:
                return True

#sns过滤函数
def safesns(req):
    not_safe = ['/','\\','*','#','$','^',')','(','+','-','%','!','~','?','[',']','{','}','<','>','=']
    gsname = req.form['gsname']
    jobname = req.form['jobname']
    salary = req.form['salary_min']+req.form['salary_max']
    city = req.form['city']
    more = req.form['more']
    for x in not_safe:
        if x in gsname:
            return False
            break
        else:
            if x in jobname:
                return False
                break
            else:
                if x in salary:
                    return False
                    break
                else:
                    if x in city:
                        return False
                        break
                    else:
                        if x in more:
                            return False
                            break
                        else:
                            return True






@app.route('/')
def index():
    try:
        names = request.cookies['user']
        return render_template('index.html',name=names)
    except:
        return render_template('index.html')       #返回首页



@app.route('/data_charts/<q>',methods=['GET'])          #ajax 数据获取接口
def data_charts(q):
    if  q == 'q1':
        data = {
        "job":["html5","web前端","android","u3d","delphi","c++","asp","c#",".net","php","hadoop","ios","wp","c","自然语言处理","node.js","java","javascript","go","perl","cocos2d-x","ruby","python","flash","vb","数据挖掘"],
        "salary":[8315,8609,10223,13744,9649,10339,9225,9667,9299,9409,19074,10772,11643,9099,23603,14750,9736,11668,20783,15334,12598,15345,14343,6972,12122,16663]}
        return jsonify(data)
    if q == 'q2':
        data = {
            "jieduan":["天使轮","初创型","成长型","A轮","B轮","C轮","D轮","上市"],
            "salary":[13737,11822,14515,15541,18346,19006,19629,16881]
        }
        return jsonify(data)
    if q == 'q3':
        data = {"bili":[2.34,6.20,2.08,6.20,1.86,1.21,10.20,1.97,2.15,2.23,2.06,2.85,0.41,4.50,2.49,2.60,1.85,6.20,6.19,1.65,6.20,6.20,2.87,8.53],
                "job":["javaScript", "java", "go", "_net", "perl", "ziranyuyanchuli", "c", "vb", "u3d", "node_js", "ruby", "shujuwajue", "wp", "csharp", "hadoop", "flash", "delphi", "php", "android", "cocos2d_x", "web前端", "asp", "ios", "cplusplus", "python", "html5"]
                }
        return jsonify(data)
    if q == 'q4':
        data = {
            "field":['移动互联网','电子商务','O2O','数据服务','信息安全','企业服务','游戏','硬件','金融','教育','旅游','广告','医疗'],
            "bili":[41.15,10.08,4.39,8.56,1.54,8.59,7.93,2.30,7.22,3.88,0.97,1.58,1.82]
        }
        return jsonify(data)
    if q == 'q5':
        data = {'city': ['杭州', '武汉', '广州', '厦门', '南京', '西安', '成都', '北京', '深圳', '上海'], 'count': [648, 252, 827, 114, 161, 119, 402, 2936, 1163, 1655]}
        return jsonify(data)










@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if safelogin(request):
            conn = sqlite3.connect('database/user_info/user_account.db')
            cursor = conn.cursor()
            sql = "select password from account where email=?"
            a = cursor.execute(sql,(request.form['email'],))
            b = a.fetchall()
            cursor.close()
            conn.close()
            try:
                if b[0][0] == request.form['password'] :
                    resp = make_response(render_template('index.html',name=request.form['email']))
                    resp.set_cookie('user',request.form['email'])
                    return resp
                else:
                    return render_template('login.html',content='账户错误')
            except:
                    return render_template('login.html',content='账户错误')
        else:
            return render_template('login.html',content='非法字符！')

    if request.method == 'GET':
        try:
            if request.cookies['Isregister'] == 'True':
                return render_template('login.html',content='您已完成注册，请登录')    #这个页面这里会显示注册过后进行登陆的提示语
        except:
            try:
                if request.cookies['user']:
                    username = request.cookies['user']
                    return render_template('user.html',name=username)
                else:
                    return render_template('login.html')              #这里返回直接点击登陆后的登陆页面
            except:
                return render_template('login.html')


@app.route('/logout')
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('user','',expires=0)
    return resp


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if saferegister(request):
            conn = sqlite3.connect('database/user_info/user_account.db')
            cursor = conn.cursor()
            sql = 'insert into account values(?,?)'
            cursor.execute(sql,(request.form['email'],request.form['password']))
            conn.commit()
            cursor.close()
            conn.close()
            return render_template('login.html',content='您已完成注册，请登录')
        else:
            resp = make_response(render_template('register.html',content='非法字符或者重复密码不一致'))
            resp.set_cookie('q3','qqwasas')
            return resp
    if request.method == 'GET':
        return render_template('register.html')      #返回注册界面



@app.route('/user')
def user():
    try:
        if request.cookies :
            c = request.cookies['user']
            return render_template('user.html',username=c)
        else:
            return redirect(url_for('login'))
    except:
        return redirect(url_for('login'))





@app.route('/search',methods=['POST'])
def search():
    if request.method == 'POST':
        s = request.form['keyword']
        keyword = jieba.cut(s)
        jobs = ['Java','Python','PHP','C','.NET','C#','C++','VB','Delphi',
                 'Perl','Ruby','Hadoop','Node.js','Go','ASP',
                 '数据挖掘','自然语言处理','HTML5','Android','iOS','WP',
                 'web前端','Flash','JavaScript','U3D','COCOS2D-X',
               ]




@app.route('/api',methods=['GET'])
def api():
    return '<script>alert("本站之前采集了十几万的招聘职位数据，可以提供未经清洗过的数据API，请发邮件至我的邮箱，我将提供key，' \
           'api请求格式为get /undata/site/yourkey/job 返回格式为json")</script>'



@app.route('/undata/<site>/<job>',methods=['GET'])
def undata(site,job):
    if site in ['lagou','zhilian','51job']:
        if job in ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x']:
            if request.method == 'GET':
                try:
                    username = request.args['auth']
                    password = request.args['pass']
                    conn = sqlite3.connect('database/user_info/user_account.db')
                    cursor = conn.cursor()
                    sql = "select password from account where email=?"
                    a = cursor.execute(sql, (username,))
                    b = a.fetchall()
                    cursor.close()
                    conn.close()
                    if b[0][0] == password:
                        conn = sqlite3.connect('database/undata/'+site+'.db')
                        cursor = conn.cursor()
                        sql = 'select * from'+' '+job
                        a = cursor.execute(sql)
                        b = a.fetchall()
                        return jsonify(b)
                except:
                    return 'error auth'
            else:
                return 'error method'
        else:
            return 'error job'
    else:
        return 'error site'






@app.route('/bbs',methods=['GET','POST'])
def bbs():           #bbs内容返回结构：[(xxx,xxx,xxx)...]
    if request.method == 'GET':
        try:
            c = request.cookies['user']
            conn = sqlite3.connect('database/user_info/bbs.db')
            cursor = conn.cursor()
            sql = 'select * from bbs'
            a = cursor.execute(sql)
            b = a.fetchall()
            cursor.close()
            conn.close()
            return render_template('bbs.html',name=c,content=b)
        except:
            return redirect(url_for('login'))

    if request.method == 'POST':
        if safebbs(request):
            c = request.cookies['user']
            theme = request.form['theme']
            content = request.form['content']
            conn = sqlite3.connect('database/user_info/bbs.db')
            cursor = conn.cursor()
            sql = 'insert into bbs values(?,?,?)'
            cursor.execute(sql,(c,theme,content))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('bbs'))
        else:
            return render_template('bbs.html',Issafe='非法字符！')


@app.route('/sns',methods=['GET','POST'])
def sns():
    if request.method == 'GET':
        try:
            c = request.cookies['user']
            conn = sqlite3.connect('database/user_info/sns.db')
            cursor = conn.cursor()
            sql = 'select gsname,jobname,city,time,rowid from sns'
            x = cursor.execute(sql)
            content = x.fetchall()
            return render_template('salary.html',name=c,content=content)
        except:
            return render_template('salary.html')
    if request.method == 'POST':
        if safesns(request):
            try:
                c = request.cookies['user']

                gsname = request.form['gsname']
                jobname = request.form['jobname']
                salary = request.form['salary_min']+'-'+request.form['salary_max']
                city = request.form['city']
                more = request.form['more']
                star = '0'
                gettime = time.strftime('%Y-%m-%d', time.localtime())

                conn = sqlite3.connect('database/user_info/sns.db')
                cursor = conn.cursor()
                sql = 'insert into sns values(?,?,?,?,?,?,?)'
                cursor.execute(sql,(gsname,jobname,salary,city,more,star,gettime))
                conn.commit()
                cursor.close()
                conn.close()

                return redirect(url_for('sns'))

            except:
                return redirect(url_for('login'))
        else:
            return render_template('salary.html',Issafe='存在不安全的字符')

@app.route('/vote/<Is>',methods=['POST'])
def vote(Is):
    try:
        c = request.cookies['user']
        id = request.form['rowid']
        if Is == 'up':
            conn = sqlite3.connect('database/user_info/sns.db')
            cursor = conn.cursor()
            sql = 'select star from sns where rowid ='+id
            a = cursor.execute(sql)
            b = a.fetchall()
            st = int(b[0][0])
            st = st+1
            st = str(st)
            sql = 'update sns set star='+str(st)+' '+'where rowid='+id
            d = cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('sns'))
        if Is == 'down':
            conn = sqlite3.connect('database/user_info/sns.db')
            cursor = conn.cursor()
            sql = 'select star from sns where rowid =' + id
            a = cursor.execute(sql)
            b = a.fetchall()
            st = int(b[0][0])
            st = st - 1
            st = str(st)
            sql = 'update sns set star=' + str(st) + ' ' + 'where rowid = ' + id
            d = cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('sns'))
    except:
        return 'error auth'


@app.route('/detail/<rowid>')
def detail(rowid):
    try:
        c = request.cookies['user']
        if rowid:
            conn = sqlite3.connect('database/user_info/sns.db')
            cursor = conn.cursor()
            sql = 'select * from sns where rowid='+rowid
            a = cursor.execute(sql)
            b = a.fetchall()
            cursor.close()
            conn.close()
            return render_template('salary_detail.html',name=c,content=b,id=rowid)
        else:
            return redirect(url_for('sns'))
    except:
        return redirect(url_for('login'))






if __name__ == '__main__' :
    app.config['SECRET_KEY'] = '19941111'
    app.run(host='0.0.0.0',debug=True)