mport pymysql
pymysql.install_as_MySQLdb()

config = {
	host = 'localhost',
	user = 'root',
	password = '123456',
	database = 'database_name',
	}

conn = pymysql.connect(**config)
