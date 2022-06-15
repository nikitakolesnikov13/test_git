ROLE_STUDENT = 1
ROLE_TEACHER = 2
ROLE_ADMIN = 3
ROLE_UNKNOWN = 0

#на вход id - идентификатор пользователя в телеграм
#функция определеяет известен ли такой пользователь телеграм нашей системе или нет
#на выход возвращается одно из значений: ROLE_STUDENT, ROLE_TEACHER,ROLE_ADMIN,ROLE_UNKNOWN
def isUserInSystem(id):
    pass

#на вход передается номер телефона
#функция ищет человека в  базе данных учетной  системы. Если человек с таким номером найден,
#то к этому человеку прикрепляется его телеграм идентификатор
#Если человек нашелся, то возрващает идентификатор его роли
def addUser(phone_number, telegram_id):
    pass

#pip install mysql-connector-python
import mysql.connector as m
def db_connect():


    server_ip = '37.140.192.146'
    user = 'u0551355_student'
    pwd = 'program2018'
    db_name = 'u0551355_itcode24bot'
    try:
        con = m.connect(host=server_ip, user=user, password=pwd, database=db_name)
        cur = con.cursor()
        # with m.connect(host=server_ip, user=user, password=pwd, database=db_name) as con:
        #     with con.cursor() as cur:
                print('Connection established')
                # cur.execute('SELECT * FROM students')
                # a = cur.fetchall()
                #
                # for s in a:
                #     print(s[1])
    except Exception as e:
        print(e)

