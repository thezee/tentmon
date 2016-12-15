##
## ./SQL/growdb-setup.sql
##

CREATE DATABASE IF NOT EXISTS growsys;

USE growsys;

CREATE TABLE IF NOT EXISTS tent_env
(
    r_id        INT         NOT NULL AUTO_INCREMENT,
    r_time      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    temp        FLOAT       NULL,
    humidity    FLOAT       NULL,
    pressure    FLOAT       NULL,

    PRIMARY KEY (r_id)

);




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