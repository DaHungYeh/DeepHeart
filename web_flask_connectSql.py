from flask import Flask, request, render_template, redirect, url_for, flash
import pymysql

app = Flask(__name__)


db = pymysql.connect(host='13.113.77.146', port=3306, user='root', passwd='123456', db='user', charset='utf8mb4')
cursor = db.cursor()

### 比對傳入的檔案內容，驗證是否成功登入
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("hello4")

        # if login_check(request.values['username'], request.values['password']):
        #     flash('Login Success!')
        #     return redirect(url_for('hello', username=request.form.get('username')))
        if request.values['username'] == 'admin' and request.values['password'] == 'hello':
            print("hello")
            return "登入成功"
            # return True
            flash('Login Success!')
            #return redirect(url_for('hello', username=request.form.get('username')))
        else:
            print("hello2")
            return "登入失敗"

        a = request.values['content']
        print("hello3")


    return render_template('login.html')

# ### 把從前端接到的參數，傳進mysql
# @app.route('/', methods=['GET', 'POST'])
# def login():
#
#     if request.method == 'POST':
#
#         insert_sql = "insert into userdb (username, password, email)VALUES('" + request.values['username'] + "','" + request.values['password'] + "','" + request.values['email'] + "');"
#         #print(insert_sql)
#         result = cursor.execute(insert_sql)
#         # 提交至 SQL
#         db.commit()
#         return render_template('0302.html')
#
#     return render_template('0302.html')

### 設定3個變數，從PyCharm輸入(username, password, email)，傳送至MYSQL ###
# @app.route('/') #test
# def db():
#
#     username = input("Enter username:")
#     password = input("Enter password:")
#     email = input("Enter email:")
#
#     #insert_sql = "insert into userdb (username, password, email)VALUES('" + username + "','" + password +  "','" + email + "');"
#
#     print(insert_sql)
#     result = cursor.execute(insert_sql)
#     # 提交至 SQL
#     db.commit()
#
#     return "result"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    # 程式結束時釋放資料庫資源
    cursor.close()
    db.close()  # 關閉連線