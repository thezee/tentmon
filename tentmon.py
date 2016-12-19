#! /usr/bin/env python
"""Tentmon script for collecting and storing sensor data"""
import time
import mysql.connector
import bme280



def main():
    """Primary function: fetch sensor data and desposit into MySQL database"""
    ### MySQL setup

    # setup mysql connector
    cnx = mysql.connector.connect(user='tentsense', password='FAKEPASS' \
    , host='FAKEHOST', database='growsys')
    # setup cursor for input
    cursor = cnx.cursor()
    # Construct SQL query to insert sensor data into database
    addrecord = ("INSERT INTO growsys.tent_env (temp, humidity, pressure) VALUES(%s, %s, %s)")


	# While the connection is valid, perform sensor reads
    while cnx:

        temp, pressure, humidity = bme280.readBME280All()
        sensor_data = (temp, humidity, pressure)

        cursor.execute(addrecord, sensor_data)

        cnx.commit()

		# Wait 60 seconds
        time.sleep(60)


if __name__ == '__main__':
    main()
