import pymysql

def conectar(host='none', user='none', senha='', banco='none'):
    return pymysql.connect(
        host=host,
        user=user,
        password=senha,
        database=banco
    )