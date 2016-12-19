#! /usr/bin/env python
"""Tentmon script for collecting and storing sensor data"""
import time
import mysql.connector
import bme280


# setup mysql connector
cnx = mysql.connector.connect(user='tentsense', password='FAKEPASS', host='FAKEHOST', database='growsys')

cursor = cnx.cursor()

# Construct SQL query to insert sensor data into database
add_record = ("INSERT INTO growsys.tent_env (temp, humidity, pressure) VALUES(%s, %s, %s)")

# While the connection is valid, perform sensor reads
while (cnx):

    t_temp, t_pressure, t_humidity = bme280.readBME280All()
    sensor_data = (t_temp, t_humidity, t_pressure)

    cursor.execute(add_record, sensor_data)

    cnx.commit()

    time.sleep(15)



