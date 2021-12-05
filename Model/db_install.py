from Model import db_class
from Model import db_conn

enginconn = db_conn.engineconn()

# 만약 db에 해당 테이블이 없다면 테이블과 컬럼 생성
def table_install():
    db_class.Task.__table__.create(bind=enginconn.engine, checkfirst=True)