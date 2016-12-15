#! /usr/bin/env python

import bme280
import time
import random
import mysql.connector


# setup mysql connector
cnx = mysql.connector.connect(user='tentsense', password='Love2CollectData!', host='byte.zer0ed0ut.net', database='growsys')

cursor = cnx.cursor()

add_record = ("INSERT INTO growsys.tent_env (temp, humidity, pressure) VALUES(%s, %s, %s)")

while (cnx):

	tentTemp,tentPressure,tentHumidity = bme280.readBME280All()
	sensor_data = (tentTemp, tentHumidity, tentPressure)
	
	cursor.execute(add_record, sensor_data)

	cnx.commit()

	time.sleep(15)



