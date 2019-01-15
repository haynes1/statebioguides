import os
import csv
import psycopg2
import re


class StateBioguides:

	def __init__(self):
		self.csvpath = "../existingbioguides.csv"
		self.conn = psycopg2.connect(database=os.environ['SBIDDBNAME'],
										user=os.environ['SBIDDBUSER'],
										password=os.environ['SBIDDBPASSWORD'],
										host=os.environ['SBIDDBHOST'], 
										port=os.environ['SBIDDBPORT'])
		self.cursor = self.conn.cursor()

	def importBioguides(self):
		a = 1

	def updateCsv(self):
		file = open(self.csvpath,"w")
		bioguides = self.getBioguides()
		csvWriter = csv.writer(file,delimiter=',')
		csvWriter.writerows(bioguides)

	def getBioguides(self,):
		bioguides = {}
		self.cursor.execute("SELECT * FROM statebioguides")
		rows = self.cursor.fetchall()
		return rows


	def generateBioguide(self,lastname,firstname,district):
		self.cursor.execute("SELECT * FROM statebioguides WHERE letter = %s", (lastname[0]))
		state = district.split("/")[1].split(":")[1]
		bioguide = state.upper() + "SL" + lastname[0] + "%06d" % (self.cursor.rowcount)
		self.cursor.execute("""INSERT INTO statebioguides
						(bioguide,letter,lastname,firstname,district)
						VALUES(%s,%s,%s,%s,%s)""",(bioguide,lastname[0].upper(),lastname,firstname,district))
		self.conn.commit()
		self.updateCsv()
		return [bioguide,lastname,firstname,state,district]

	def checkBioguide(self,lastname,firstname=None,district=None):
		if lastname == None:
			return -1

		query_fields = ["lastname"]
		query_values = [lastname]
		if firstname:
			query_fields.append("firstname")
			query_values.append(firstname)
		if district:
			query_fields.append("district")
			query_values.append(str(district))

		query_string_a = []
		for field in query_fields:
			temp = field + " = %s"
			query_string_a.append(temp)
		query_string =  " AND ".join(query_string_a)

		query = "SELECT * FROM statebioguides WHERE	" + query_string
		self.cursor.execute(query,query_values)
		return self.cursor.fetchall()

	#returns an array of bioguide ids and other relevant info for input
	def getBioguide(self,lastname,firstname=None,district=None):
		ret = []
		bids = self.checkBioguide(lastname,firstname,district)
		if len(bids) == 0:
			ret.append(self.generateBioguide(lastname,firstname,district))
		else:
			ret = bids
		return ret