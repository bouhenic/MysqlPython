import pymysql


class Bdd:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db


    def Lastselect(self):

        with connection.cursor() as cursor:
                sql = "SELECT * FROM `TEMPERATURE` ORDER BY ID DESC LIMIT 1"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    for row in result:
                        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))

                except:
                    print("Oops! Something wrong")

        connection.commit()


    def selectById(self,Id):

        with connection.cursor() as cursor:
                sql = f"SELECT * FROM `TEMPERATURE` WHERE ID={Id} LIMIT 1"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    for row in result:
                        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))

                except:
                    print("Oops! Something wrong")

        connection.commit()



    def insert(self,temp):

        with connection.cursor() as cursor:
                sql = f"INSERT INTO temperature(TEMP) VALUES({temp})"
                try:
                    cursor.execute(sql)

                except:
                    print("Oops! Something wrong")

        connection.commit()



    def update(self,temp,Id):

        with connection.cursor() as cursor:
                sql = f"UPDATE TEMPERATURE SET TEMP = {temp} WHERE id = {Id}"

                try:
                    cursor.execute(sql)

                except:
                    print("Oops! Something wrong")

        connection.commit()


    def delete(self,Id):

        with connection.cursor() as cursor:
                sql = f"DELETE FROM TEMPERATURE WHERE id={Id}"
                try:
                    cursor.execute(sql)

                except:
                    print("Oops! Something wrong")

        connection.commit()



bdd = Bdd('localhost', 8889, 'root', 'root', 'METEO')
connection = pymysql.connect(
    host=bdd.host,
    port=bdd.port,
    user=bdd.user,
    password=bdd.password,
    db=bdd.db
    )



bdd.insert(27)
bdd.delete(1008)
bdd.Lastselect()
bdd.selectById(1006)
connection.close()