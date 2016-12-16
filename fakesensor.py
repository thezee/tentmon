#!/usr/bin/env python
"""Module for producing fake sensor data for programming development"""

import random




class FakeBME280(object):
    """Reproduce output from bme280.py module for BME280 i2c sensor"""
    def readBME280All():
        """Produce output that mimics BME280 sensor data"""
        temperature = random.uniform(18.9, 31.4)
        humidity = random.uniform(21.0, 70.0)
        pressure = random.uniform(980.0, 1020.1)

        return temperature, pressure, humidity

def main():
    """Default results from running script"""

    temperature, pressure, humidity = FakeBME280.readBME280All()
    print("Fake BME280 Sensor\n")
    print("Temperature : ", temperature, "C")
    print("Pressure : ", pressure, "hPa")
    print("Humidity : ", humidity, "%")

if __name__ == "__main__":
    main()



