from Model import db_class
from Model import db_conn

enginconn = db_conn.engineconn()

def table_install():
    db_class.Task.__table__.create(bind=enginconn.engine, checkfirst=True)