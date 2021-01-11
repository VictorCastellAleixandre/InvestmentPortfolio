# -------------------- Controller.py --------------------
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from Database.Connection import connection
from Model import Model

#PDF
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import numpy as np
from datetime import datetime

style.use('ggplot')

def graphPortfolio(id_user):
	
	#GRAFICO
	mydb = connection()
	db_list_date = Model(connection()).loadDate(id_user)#Load equity and date
	db_list_date.sort()
	to_plot = pd.DataFrame(db_list_date, columns=['equity_date', 'equity']).set_index('equity_date')#Dataframe with equity and date like index
	return to_plot #return dataframe

def portfolioRentability(id_user):
	
	mydb = connection()
	db_list_date = Model(connection()).loadDate(id_user)#Load equity and date
	db_list_date.sort()
	to_plot = pd.DataFrame(db_list_date, columns=['equity_date', 'equity']).set_index('equity_date')
	try:
		inicial_date = to_plot['equity'].iloc[0]
		last_date = to_plot['equity'].iloc[-1]
		if inicial_date == 0:
			return 'First date equity = 0'

		else:
			rentability = ((last_date - inicial_date) * 100)/inicial_date
			return rentability
	except:
		return '0'
def archivoPDF(id_user):

	estiloHoja = getSampleStyleSheet()
	story = []
	cabecera = estiloHoja['Heading4']
	cabecera.pageBreakBefore = 0
	cabecera.keepWithNext = 0
	cabecera.backColor = colors.white
	date = str(datetime.now())
	parrafo = Paragraph('Date: '+ date, cabecera)#paragraph with date
	story.append(parrafo)
	parrafo_2 = Paragraph('Investments Portfolio', cabecera)#paragraph with the title
	story.append(parrafo_2)
	story.append(Spacer(0, 20))
	story.append(Spacer(0, 20))
	doc = SimpleDocTemplate("Investments.pdf", pagesize=(1000, 1000))
	db_list_pdf = Model(connection()).loadPDF(id_user)#Database portfolio data
	to_plot = pd.DataFrame(db_list_pdf, columns=[ 'acr', 'stock', 'num', 'purchase', 'price', 'mrkt', 'rentability', 'percentage', 'per', 'dividend', 'pb'])	
	data=[]
	data.append([ 'acr', 'stock', 'num', 'purchase', 'price', 'mrkt', 'rentability', 'percentage', 'per', 'dividend', 'pb'])#Add firt line with column names
	for row in db_list_pdf:
		data.append(list(row))#Load all data 
	t=Table(data, style=[('GRID', (0,0), (-1,-1),0.5,colors.black), ('ALIGN',(0,0),(-1,-1),'CENTER'),])#Create the table
	story.append(t)#add de table
	doc.build(story)#build the pdf with all data


portfolioRentability(42)