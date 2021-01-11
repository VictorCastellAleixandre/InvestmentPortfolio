# -------------------- Model.py --------------------
class Model():
    def __init__(self,mydb):
        self.mydb = mydb
        
    def loadData(self, id_user):
        
        with self.mydb.cursor() as cursor:
            query = "SELECT id, acr, stock, num, purchase, price, mrkt, rentability, percentage, per, dividend, pb FROM myportfolio WHERE id_user = %s"#La instrucción SQL
            cursor.execute(query, (id_user,))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor

        return result

    def deleteData(self, itemtext):
        
        with self.mydb.cursor() as cursor:
            query = "DELETE FROM myportfolio WHERE id = %s"#La instrucción SQL
            cursor.execute(query, (itemtext,))#Sirve para hacer las consultas SQL
            result = self.mydb.commit()#Nos devuelve los resultados almacenados en el cursor        
       

    def addData(self, id_user, acronym, name, number, purchase_price, price_sh, mrkt_cap, rentability, percentage, per, dividend, pb):
       
        with self.mydb.cursor() as cursor:
            query = query = "INSERT INTO myportfolio (id_user, acr, stock, num, purchase, price, mrkt, rentability, percentage, per, dividend, pb) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"#La instrucción SQL
            cursor.execute(query, (id_user, acronym, name, number, purchase_price, price_sh, mrkt_cap, rentability, percentage, per, dividend, pb))#Sirve para hacer las consultas SQL
            self.mydb.commit()#Nos devuelve los resultados almacenados en el cursor

    def loadAcronym(self, id_user):
        with self.mydb.cursor() as cursor:
            query = query = "SELECT  acr FROM myportfolio WHERE id_user = %s GROUP BY acr"#La instrucción SQL
            cursor.execute(query, (id_user, ))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor
            return result

    def loadNumber(self):
        with self.mydb.cursor() as cursor:
            query = query = "SELECT num FROM myportfolio GROUP BY acr"#La instrucción SQL
            cursor.execute(query)#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor
            return result

    def loadLogin(self, name):
        with self.mydb.cursor() as cursor:
            query = query = "SELECT id_user FROM user WHERE name = %s" #La instrucción SQL
            cursor.execute(query, (name, ))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor
            return result

    def loadPassword(self, password, name):
        with self.mydb.cursor() as cursor:
            query = query = "SELECT id_user FROM user WHERE password = %s AND name = %s"#La instrucción SQL
            cursor.execute(query, (password, name ))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor
            return result

    def addUser(self, name, password, email, phone):
       
        with self.mydb.cursor() as cursor:
            query = query = "INSERT INTO user (name, password, email, phone) VALUES (%s, %s, %s, %s)"#La instrucción SQL
            cursor.execute(query, (name, password, email, phone))#Sirve para hacer las consultas SQL
            self.mydb.commit()#Nos devuelve los resultados almacenados en el cursor

    def loadUser(self):
        
        with self.mydb.cursor() as cursor:
            query = "SELECT name FROM user"#La instrucción SQL
            cursor.execute(query)#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor

        return result
        
    def loadDate(self, user):
        
        with self.mydb.cursor() as cursor:
            query = "SELECT equity_date, pf_equity FROM portfolio_equity WHERE id_user = %s"#La instrucción SQL
            cursor.execute(query, (user, ))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor

        return result

    def loadOnlyDate(self, user):
        
        with self.mydb.cursor() as cursor:
            query = "SELECT equity_date FROM portfolio_equity WHERE id_user = %s"#La instrucción SQL
            cursor.execute(query, (user, ))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor

        return result

    def addDate(self, date, equity, id_user):
       
        with self.mydb.cursor() as cursor:
            query = query = "INSERT INTO portfolio_equity (equity_date, pf_equity, id_user) VALUES (%s, %s, %s)"#La instrucción SQL
            cursor.execute(query, (date, equity, id_user))#Sirve para hacer las consultas SQL
            self.mydb.commit()#Nos devuelve los resultados almacenados en el cursor

    def deleteDataGraph(self, date):
        with self.mydb.cursor() as cursor:
            query = "DELETE FROM portfolio_equity WHERE equity_date = %s"#La instrucción SQL
            cursor.execute(query, (date,))#Sirve para hacer las consultas SQL
            result = self.mydb.commit()#Nos devuelve los resultados almacenados en el cursor  

    def loadPDF(self, id_user):
        
        with self.mydb.cursor() as cursor:
            query = "SELECT acr, stock, num, purchase, price, mrkt, rentability, percentage, per, dividend, pb FROM myportfolio WHERE id_user = %s"#La instrucción SQL
            cursor.execute(query, (id_user,))#Sirve para hacer las consultas SQL
            result = cursor.fetchall()#Nos devuelve los resultados almacenados en el cursor

        return result

    def addAuditoria(self, id_user, action, date_auditoria):
       
        with self.mydb.cursor() as cursor:
            query = query = "INSERT INTO auditoria (id_user, action, date_auditoria) VALUES (%s, %s, %s)"#La instrucción SQL
            cursor.execute(query, (id_user, action, date_auditoria))#Sirve para hacer las consultas SQL
            self.mydb.commit()#Nos devuelve los resultados almacenados en el cursor