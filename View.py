# -------------------- View.py --------------------
import sys
import yfinance as yf
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QTableWidgetItem, QAbstractItemView)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.uic import loadUi
from Database.Connection import connection
from Model import Model
#Graficos
import numpy as np
import pandas as pd
import Controller
from datetime import *

# ----------------- LOGIN ----------------- 
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)
        self.mydb = connection()
        str(self.pushButton_2.clicked.connect(self.comprobarLogin))#Acces to the menu with credentials
        self.pushButton_4.clicked.connect(self.abrirSignIn)#Acces to SignIn

    def abrirPrueba(self):#Open main menu
        self.hide()
        otraventana = Prueba(self)
        otraventana.show() 

    def abrirSignIn(self):#Open SignIn
        self.hide()
        otraventana = SignIn(self)
        otraventana.show() 

    def comprobarLogin(self):
        user = self.textEdit_6.toPlainText()
        password = self.textEdit_7.toPlainText()
        db_user = Model(self.mydb).loadLogin(user)
        db_password = Model(self.mydb).loadPassword(password, user)

        try:
            if db_user[0] == db_password[0]:
                self.abrirPrueba()
                global id_user
                id_user = int(str(db_password[0]).replace(',', '').replace("'", "").replace(")", "").replace("(", ""))

                action = 'login'
                date_auditoria = datetime.now()
                Model(self.mydb).addAuditoria(id_user, action, date_auditoria)

            else:
                self.textEdit_6.setText('Wrong username or password')
                self.textEdit_7.setText('Wrong username or password')
        except:
            self.textEdit_6.setText('Wrong username or password')
            self.textEdit_7.setText('Wrong username or password')


# ----------------- SIGN IN ----------------- 

class SignIn(QMainWindow):
    def __init__(self, parent = None):
        super(SignIn, self).__init__(parent)
        loadUi('signin.ui', self)
        self.pushButton_2.clicked.connect(self.registrarUsuario)#Add the user to DB
        self.pushButton_4.clicked.connect(self.abrirLogin)#Open login menu
        self.mydb = connection()

    def abrirLogin(self):#Open login
        self.parent().show()
        self.close()

    def registrarUsuario(self):#Save data user if it's not registered
        signin_name = self.textEdit_6.toPlainText()
        signin_password = self.textEdit_7.toPlainText()
        signin_email = self.textEdit_8.toPlainText()
        signin_phone = self.textEdit_9.toPlainText()
        db_user_name = Model(self.mydb).loadUser()
        
        clean_db_user_name = []
        for element in db_user_name:
            clean_element = str(element).replace(',', '').replace("'", "").replace(")", "").replace("(", "")
            clean_db_user_name.append(clean_element)

        if signin_name not in clean_db_user_name:
            Model(self.mydb).addUser(signin_name, signin_password, signin_email, signin_phone)
            self.abrirLogin()
        else:
            self.textEdit_6.setText('The name is already in use.')
            self.textEdit_7.setText('')
            self.textEdit_8.setText('')
            self.textEdit_9.setText('')


# ----------------- PRINCIPAL MENU ----------------- 

class Prueba(QMainWindow):
    def __init__(self, parent = None):
        super(Prueba, self).__init__(parent)
        loadUi('prueba.ui', self)
        self.pushButton_2.clicked.connect(self.abrirSecond)#Open calculator
        self.pushButton_3.clicked.connect(self.abrirThird)#Open portfolio

    def abrirSecond(self):
        self.hide()
        otraventana = Second(self)
        otraventana.show()

    def abrirThird(self):
        self.hide()
        otraventana = Cartera(self)
        otraventana.show()    
    
# ----------------- CALCULATOR ----------------- 

class Second(QMainWindow):
    def __init__(self, parent = None):
        super(Second, self).__init__(parent)
        loadUi('second.ui', self)
        self.mydb = connection()
        self.pushButton_3.clicked.connect(self.abrirPrueba)#Open menu
        self.pushButton_2.clicked.connect(self.clean)#Clean
        self.pushButton.clicked.connect(self.calcular)#Calculate

        action = 'financial_calculator'#Save the action
        date_auditoria = datetime.now()
        Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
    
    def calcular(self):#Calculator
        try:
            #variables
            equity= float(self.textEdit_14.toPlainText())
            ebitda=float(self.textEdit_3.toPlainText())
            mrkt_price=float(self.textEdit.toPlainText())
            fcf=float(self.textEdit_4.toPlainText())
            acciones=float(self.textEdit_5.toPlainText())
            debt=float(self.textEdit_6.toPlainText())
            net_income=float(self.textEdit_7.toPlainText())
            #results
            resultado_price_fcf = mrkt_price/fcf
            resultado_per = mrkt_price/net_income
            resultado_ev_fcf = (mrkt_price+equity-debt)/fcf
            resultado_ev = equity/debt
            resultado_enterprise_value = mrkt_price+equity-debt
            resultado_ev_ebitda = resultado_enterprise_value/ebitda
            #float to string
            st_resultado_price_fcf = str(resultado_price_fcf)
            st_resultado_per = str(resultado_per)
            st_resultado_ev_fcf = str(resultado_ev_fcf)
            st_resultado_cash_debt = str(resultado_ev)
            st_resultado_ev_ebitda = str(resultado_ev_ebitda)
            st_resultado_enterprise_value = str(resultado_enterprise_value)
            #Show data
            self.textEdit_8.setText(st_resultado_price_fcf)
            self.textEdit_9.setText(st_resultado_per)
            self.textEdit_10.setText(st_resultado_ev_fcf)
            self.textEdit_11.setText(st_resultado_cash_debt)
            self.textEdit_12.setText(st_resultado_ev_ebitda)
            self.textEdit_13.setText(st_resultado_enterprise_value)

        except ValueError:
            self.textEdit_8.setText('Be sure to fill in the fields')
            self.textEdit_9.setText('Values ​​have to be numeric')
            self.textEdit_10.setText('')
            self.textEdit_11.setText('')
            self.textEdit_12.setText('')
            self.textEdit_13.setText('')
            self.textEdit_14.setText('')
            self.textEdit_3.setText('')
            self.textEdit.setText('')
            self.textEdit_4.setText('')
            self.textEdit_5.setText('')
            self.textEdit_6.setText('')
            self.textEdit_7.setText('')

    def clean(self):#Clean text
        self.textEdit_8.setText('')
        self.textEdit_9.setText('')
        self.textEdit_10.setText('')
        self.textEdit_11.setText('')
        self.textEdit_12.setText('')
        self.textEdit_13.setText('')
        self.textEdit_14.setText('')
        self.textEdit_3.setText('')
        self.textEdit.setText('')
        self.textEdit_4.setText('')
        self.textEdit_5.setText('')
        self.textEdit_6.setText('')
        self.textEdit_7.setText('')

    def abrirPrueba(self):#Open menu
        self.parent().show()
        self.close()


# ----------------- PORTFOLIO ----------------- 

class Cartera(QMainWindow):
    def __init__(self, parent = None):
        super(Cartera, self).__init__(parent)
        loadUi('cartera.ui', self)
        self.pushButton_4.clicked.connect(self.abrirPrueba)#Open menu
        self.pushButton_6.clicked.connect(self.loadData)#Load data from DB to table
        self.pushButton_7.clicked.connect(self.addData)#Add data to DB
        self.pushButton_9.clicked.connect(self.deleteData)#Delete data from DB
        self.pushButton_8.clicked.connect(self.addDataGraph)#Add data to graph DB
        self.pushButton_10.clicked.connect(self.deleteDataGraph)#Delete data drom graph DB
        self.pushButton_11.clicked.connect(self.generatePDF)#Generate PDF with user portfolio data
        
        # Deshabilitar edición
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tableWidget.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        # Deshabilitar clasificación
        self.tableWidget.setSortingEnabled(False)
        # Alineación del texto del encabezado
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.tableWidget.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.tableWidget.setAlternatingRowColors(True) 
        # self.tabla.verticalHeader().setHighlightSections(True)
        nombreColumnas = ("ID", "Acronym", "Stock Name", "Nº", "Purchase price", "Price", "Mrkt price", "+/-€", "+/-%", "PER", "Dividend", "P/B" )
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)

        self.mydb = connection()
        self.loadData()
        self.update_graph()
        self.showRentability()
        action = 'portfolio_evolution'
        date_auditoria = datetime.now()
        Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
    
    def loadData(self):#Load data from DB to table
        result = Model(self.mydb).loadData(id_user)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.update_graph()

    def deleteData(self, connection):#Delete data from DB
        try:
            action = 'delete_data'
            date_auditoria = datetime.now()
            Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
            itemx = self.tableWidget.item(self.tableWidget.currentRow(), 0)
            itemtext = itemx.text()  
            result = Model(self.mydb).deleteData(itemtext)
            self.loadData()
            self.update_graph()
        except AttributeError:
            pass

    def addData(self, connection):#Add data to DB
        try:
            action = 'add_data'
            date_auditoria = datetime.now()
            Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
            acronym = self.textEdit_3.toPlainText()
            name = yf.Ticker(acronym).info['shortName']
            number = float(self.textEdit_4.toPlainText())
            purchase_price = float(self.textEdit_5.toPlainText())
            price_sh = float(yf.Ticker(acronym).info['previousClose'])
            mrkt_cap = float(yf.Ticker(acronym).info['marketCap'])
            rentability = (price_sh * number) - (purchase_price * number)
            percentage = (rentability*100/(purchase_price * number))
            per = float(yf.Ticker(acronym).info['forwardPE'])
            try:
                dividend = float(yf.Ticker(acronym).info['dividendRate'])
            except TypeError:
                dividend = 0
            pb = float(yf.Ticker(acronym).info['priceToBook'])

            result = Model(self.mydb).addData(id_user, acronym, name, number, purchase_price, price_sh, mrkt_cap, rentability, percentage, per, dividend, pb)            
            self.loadData()
            self.update_graph()
        except :
            self.textEdit_3.setText('Invalid acronym or data')
            pass

    def update_graph(self): #Load graph
        
        df = pd.DataFrame() 
        df = Controller.graphPortfolio(id_user)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot( df.index.values, df['equity'])
        self.MplWidget.canvas.axes.legend(('Portfolio'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Portfolio') 
        self.MplWidget.canvas.axes.tick_params(colors='white')
        self.MplWidget.canvas.axes.set_facecolor('#353535')
        self.MplWidget.canvas.draw()
    
    def addDataGraph(self, connection):#Add datat to graph database
        action = 'add_date'
        date_auditoria = datetime.now()
        Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
        date = self.dateEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        equity = self.textEdit_6.toPlainText()
        db_date = Model(self.mydb).loadOnlyDate(id_user)
        clean_db_date = []
        try:
            prueba_float = float(equity)
            for i in range(len(db_date)):
                selected_element = db_date[i][0]
                clean_date = str(selected_element).replace(',', '').replace("'", "").replace(")", "").replace("(", "")
                clean_db_date.append(clean_date)

            if date not in clean_db_date:
                Model(self.mydb).addDate(date, equity, id_user)

            elif date in clean_db_date:
                Model(self.mydb).deleteDataGraph(date)
                Model(self.mydb).addDate(date, equity, id_user)

            else:
                self.textEdit_6.setText('Invalid date')

        except:
            self.textEdit_6.setText('Invalid data, input a number') 
         
        self.update_graph()
        self.showRentability()

    def deleteDataGraph(self, connection):#Delete datat to graph database
        action = 'delete_date'
        date_auditoria = datetime.now()
        Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
        date = self.dateEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
             
        result = Model(self.mydb).deleteDataGraph(date)
        self.loadData()
        self.update_graph()
        self.showRentability()

    def generatePDF(self):#Create a PDF
        action = 'generate_pdf'
        date_auditoria = datetime.now()
        Model(self.mydb).addAuditoria(id_user, action, date_auditoria)
        pdf = Controller.archivoPDF(id_user)
   
    def showRentability(self):#Muestra la rentabilidad de la cartera
        portfolio_rentability = str(Controller.portfolioRentability(id_user))
        self.textEdit_7.setText(portfolio_rentability)
    
    def abrirPrueba(self):#Open menu
        self.parent().show()
        self.close()


app = QApplication(sys.argv)
app.setStyle("Fusion")
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)
main = Login()
main.show()
sys.exit(app.exec_())