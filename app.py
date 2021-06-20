# ddb 모듈을 사용할 것이라고 선언함
import ddb;
from flask import Flask, request, render_template, redirect, session
from gameFunction import cash_multiply
import loginModule

app = Flask(__name__)

# 로그인 처리 때문에 'session'을 사용하기 위한 임의의 값
app.secret_key = b'aaa!111/'

# 메인화면
@app.route('/')
def hello():
    return render_template("main.html")

# 적금관리 페이지
@app.route('/money')
def money():
    # 로그인된 사용자들만 적금관리 페이지를 사용할 수 있다
    # 세션 체크
    if 'email' in session:
        return render_template("money.html")
    else:
        return redirect('/signin')

# 어떤 방법으로 데이터를 주든 'GET', 'POST' 전부 쓸 수 있다
@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        return "GET으로 들어온 페이지"
    else:
        money = request.form["money"]
        money = cash_multiply(int(money)) # 돈 곱해주는 함수
        return render_template("show.html", money=money)

# 회원가입
@app.route('/signup', methods=['GET', 'POST']) 
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        user_name = request.form["user_name"]
        user_email = request.form["user_email"]
        user_pwd = request.form["user_pwd"]
        # 위 데이터를 토대로하여 db에 삽입시킴
        ddb.insert_user(user_email, user_name, user_pwd)

        # 회원가입이 정상적으로 되었다면 메인으로 리다이렉트 시킨다
        return redirect('/')
        # return "회원 정보 <br>NAME : {}<br>EMAIL : {}<br>PASSWORD : {}".format(user_name, user_email, user_pwd)

# 로그인
@app.route('/signin', methods=['GET', 'POST']) 
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        user_email = request.form["user_email"]
        user_pwd = request.form["user_pwd"]
        #return "{} {}".format(user_email, user_pwd)

        #isLogin = loginModule.LoginChecker(user_email, user_pwd)
        #if(isLogin):
            #return "Login Success"
        #else:
            #return "Login Failed"
        
        ret = ddb.select_user(user_email, user_pwd)
        if ret != None:
            # 아이디가 존재할 경우 로그인이 성공되고 세션에 email 값을 넣어준다.
            session['email'] = user_email
            return redirect('/')
        else:
            return redirect('/signin')

@app.route('/logout')
def logout(): 
    session.pop('email', None) 
    return redirect('/')

@app.route('/showmoney')
def showmoney():
    return '''
        <iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY">
        </iframe>
    '''
# render_template을 사용하여 HTML 코드들을 불러올 수 있다.
@app.route('/htmlShowmoney')
def showmoneyHTML():
    return render_template("youtube.html")

# if __name__ == '__main__':
#      # with app.test_request_context();  
#      #     print(url_for('daum'))
#  app.run(debug=True)
