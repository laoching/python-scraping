import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='None', db='mysql')

#연결 객체(conn), 커서 객체(cur)
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
pring(cur.fetchone())

#커서와 연결 사용을 마치면 연결 누수가 발생하지 않게 닫아줘야함
cur.close()
conn.close()