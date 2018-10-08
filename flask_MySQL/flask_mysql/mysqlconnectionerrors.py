import pymysql.cursors

class MySQLConnection:
    def __init__(self, db,table):
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password=root,
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor, 
                                    autocommit=True)
        self.connection = connection

    def query_db(query, data=None):
        with self.connection.cursor() as curse:
            try:
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close() 
def connectToMySQL(db):
    return MySQLConnection(db)

E0401:Unable to import 'pymysql.cursors'

#error fixes:
# change password to a string
# remove __init__'s third parameter table
# add self to quer_db function paramters
# with self.connection.cursor() as curse has a typo. curse must be cursor

