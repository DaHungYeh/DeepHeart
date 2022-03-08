from flask import Flask, request, render_template, redirect, url_for, flash
import pymysql

app = Flask(__name__)


db = pymysql.connect(host='13.113.77.146', port=3306, user='root', passwd='123456', db='user', charset='utf8mb4')
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def login():
    return redirect(url_for('post_admin'))

### 比對傳入的檔案內容，驗證是否成功登入
@app.route('/post_admin', methods=['GET', 'POST'])
def post_admin():
    if request.method == 'POST':
        # # 使用者帳號的值 = 查詢資料庫中，與使用者輸入的帳號的值，相同的使用者帳號的密碼
        # if request.values['username'] == "select * from userdb where username = '" + request.values['username'] + "'" and request.values['password'] == "select * from userdb where password = '" + request.values['password'] + "'":
        #     return "登入成功"
        #     # return True
        #
        #     #return redirect(url_for('hello', username=request.form.get('username')))
        # else:
        cursor.execute("select * from userdb where username = '" + request.values['username'] + "'")
        for row in cursor:
            if request.values['username'] == row[0] and request.values['password'] == row[1] : # 帳號 # 密碼
                return "登入成功"
            else:
            # a = "select * from userdb where username = 'fefe'"
            #a = "select * from userdb where username = '" + request.values['username'] + "'"
                return "登入失敗"

    return redirect(url_for('post_content'))

@app.route('/post_content', methods=['GET', 'POST'])
def post_content():
    if request.method == 'POST':

        input = request.values['content']
        print(input)

        # # if request.form['content'] is None :
        # #     a = request.values.get('content')
        # #     return "Hello" + a
        # return render_template('0302.html', user_content=user_content)
        return render_template('0302.html', user_content=input)

    return render_template('0302.html')

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