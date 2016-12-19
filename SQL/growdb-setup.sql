##
## ./SQL/growdb-setup.sql
##

CREATE DATABASE IF NOT EXISTS growsys;

USE growsys;


## Currently used for collecting environmental data about grow tent.
## Collection rate for data is every 15 seconds.
## 

CREATE TABLE IF NOT EXISTS tent_env
(
    r_id        INT         NOT NULL AUTO_INCREMENT,
    r_time      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    temp        FLOAT       NULL,
    humidity    FLOAT       NULL,
    pressure    FLOAT       NULL,
    tent_id     VARCHAR(55) NULL

    PRIMARY KEY (r_id)

) COMMENT="Table for collection of enviromental sensor data";


## Table for details about tents available/in use. 
## Primary use will be information tracking and squared/cubic footage.

CREATE TABLE IF NOT EXISTS tent_info (

    tent_id     VARCHAR(55)     NOT NULL,
    height      INT             NOT NULL,
    width       INT             NOT NULL,
    length      INT             NOT NULL,
    ducts_4     INT             NULL,
    ducts_6     INT             NULL,
    


) COMMENT="Table for information about individual tents available";

INSERT INTO tent_info( tent_id, height, width, length, ducts_4, ducts_6 ) VALUES( "Primary", 63, 32, 32, 2, 2 );


CREATE TABLE IF NOT EXISTS log_water
(
	w_id		INT			NOT NULL AUTO_INCREMENT,
	w_time		TIMESTAMP	NOT NULL DEFAULT CURRENT_TIMESTAMP,
	amount		INT			NOT NULL
	
	PRIMARY KEY ( w_id )
	

);


# User for sensor device
CREATE USER 'tentsense'@'FAKEHOST' IDENTIFIED BY "FAKEPASSWORD";
GRANT INSERT,SELECT ON growsys.tent_env TO 'FAKEHOST'@locahost;