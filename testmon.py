"""Tentmon script for collecting and storing sensor data"""
import time
import mysql.connector
from fakesensor import FakeBME280


Temperature, Humdity,
