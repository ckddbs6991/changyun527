import pymysql

def dbcon():
    return pymysql.connect(host='ckddbs527.mysql.pythonanywhere-services.com,
                   user='ckddbs527', password='ckddbs527@',
                   db='ckddbs527$mydb', charset='utf8')

def create_table():
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE user_info (user_email varchar(50), user_name varchar(50), user_pw varchar(50))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_user(email, name, password):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (email, name, password)
        c.execute("INSERT INTO user_info VALUES (%s, %s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM user_info')
        ret = c.fetchall()
        # for row in c.execute('SELECT * FROM student'):
        #     ret.append(row)
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

def select_user(email, password):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (email, password)
        c.execute('SELECT * FROM user_info WHERE user_email = %s and user_pw = %s', setdata)
        # ret는 위 query문을 동작하여 결과 값을 반환 받는다. fetchone() 함수를 통해서
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

