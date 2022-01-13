import constant
import mysql.connector
import json
from helper import array_zeros

TABLES = {}

TABLES[constant.MYSQL_TABLE_STATION_INFO] = (
        "CREATE TABLE IF NOT EXISTS %s("
        " station_code VARCHAR(50) PRIMARY KEY,"
        " num_current_metter INT(3) NOT NULL,"
        " llvd INT(3) NOT NULL,"
        " hhtt INT(3) NOT NULL,"
        " charge_circle INT(3) NOT NULL,"
        " soh VARCHAR(300) NOT NULL,"
        " adc_bit INT(3) NOT NULL,"
        " dc_source INT(5) NOT NULL,"
        " url_data VARCHAR(100) NOT NULL,"
        " url_config VARCHAR(100) NOT NULL,"
        " timer_log_data INT(5) NOT NULL,"
        " timer_send_data_to_server INT(5) NOT NULL,"
        " timer_take_sample_soh INT(5) NOT NULL,"
        " timer_save_soh INT(5) NOT NULL,"
        " timer_send_serial INT(5) NOT NULL,"
        " serial_port VARCHAR(50) NOT NULL,"
        " serial_baud INT(6) NOT NULL"
        ")"
        % constant.MYSQL_TABLE_STATION_INFO
)

DATA_TABLES = {}
DATA_TABLES[constant.MYSQL_TABLE_STATION_INFO] = (
        "INSERT INTO %s("
        " station_code,"
        " num_current_metter,"
        " llvd,"
        " hhtt,"
        " charge_circle,"
        " soh,"
        " adc_bit,"
        " dc_source,"
        " url_data,"
        " url_config,"
        " timer_log_data,"
        " timer_send_data_to_server,"
        " timer_take_sample_soh,"
        " timer_save_soh,"
        " timer_send_serial,"
        " serial_port,"
        " serial_baud"
        ") VALUES("
        " '%s', %d, %d, %d, %d, %d, %d, %d, '%s', '%s', %d, %d, %d, %d, %d, '%s', %d"
        ")"
        % (
            constant.MYSQL_TABLE_STATION_INFO,
            "TN01",
            3, 45, 50, 100, 100, 11, 5060,
            "https://giamsat03.breedlife.com/api/v1/data",
            "https://giamsat03.breedlife.com/api/v1/stations1",
            5, 10, 10, 60, 2, "/dev/ttyMT1", 57600
        )
)


class StationSQL:
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect(self):
        self.db = mysql.connector.connect(
            host=constant.MYSQL_HOST,
            user=constant.MYSQL_USER,
            password=constant.MYSQL_PASS)
        self.cursor = self.db.cursor(dictionary=True)

        # Init database, tables
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + constant.MYSQL_DB)
        self.cursor.execute("USE " + constant.MYSQL_DB)
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS " +
            constant.MYSQL_TABLE_DATA +
            "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, voltage FLOAT NOT NULL, current VARCHAR(100) NOT NULL, "
            "temperature FLOAT NOT NULL, time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")

    def check_table_exist(self, table):
        sql = "SHOW TABLES LIKE '%s'" % table
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if len(result):
            return True
        return False

    def log_data(self, data):
        current_item = []
        for item in data["current_item"]:
            current_item.append(round(item, 1))
        sql = "INSERT INTO data(voltage, current, temperature) VALUES(%.1f, '%s', %.1f)" \
              % (round(data["voltage"], 1), json.dumps(current_item), round(data["temperature"], 1))

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def log_calc_soh(self, data, NUM_CURRENT_METER):
        sql = "SELECT * FROM " + constant.MYSQL_TABLE_CALC_SOH
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        current_wattage = array_zeros(NUM_CURRENT_METER)

        if len(result) == 0:
            for i in range(0, NUM_CURRENT_METER):
                current_wattage[i] = data[i]
            sql = "INSERT INTO %s(wattage='%s')" % (
                constant.MYSQL_TABLE_CALC_SOH, json.dumps(current_wattage))
        else:
            current_wattage = json.loads(result[0][1])
            if len(current_wattage) != NUM_CURRENT_METER:
                current_wattage = array_zeros(NUM_CURRENT_METER)
            else:
                for i in range(0, NUM_CURRENT_METER):
                    current_wattage[i] += data[i]
            sql = "UPDATE TABLE %s SET wattage='%s' WHERE ID=1" % (
                constant.MYSQL_TABLE_CALC_SOH, json.dumps(current_wattage))

        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def init_table_calc_soh(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS " +
            constant.MYSQL_TABLE_CALC_SOH +
            "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, wattage VARCHAR(200) NOT NULL)")

    def drop_table_calc_soh(self):
        self.cursor.execute(
            "DROP TABLE IF EXISTS " +
            constant.MYSQL_TABLE_CALC_SOH)

    #
    def init_table_soh(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS " +
            constant.MYSQL_TABLE_SOH +
            "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, soh VARCHAR(200) NOT NULL)")

    def drop_table_soh(self):
        self.cursor.execute(
            "DROP TABLE IF EXISTS " +
            constant.MYSQL_TABLE_SOH)

    def init_table_station_info(self):
        if not self.check_table_exist(constant.MYSQL_TABLE_STATION_INFO):
            self.cursor.execute(TABLES[constant.MYSQL_TABLE_STATION_INFO])
            self.cursor.execute(DATA_TABLES[constant.MYSQL_TABLE_STATION_INFO])
            try:
                self.db.commit()
            except:
                self.db.rollback()

    def get_station_info(self):
        sql = "SELECT * FROM %s" % constant.MYSQL_TABLE_STATION_INFO
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if len(results):
            return results[0]
        return False

    def update_station_info(self, data):
        keys = data.keys()
        sql = "UPDATE TABLE %s SET " % constant.MYSQL_TABLE_STATION_INFO
        for key in keys:
            sql += key + "="
            if isinstance(data[key], str):
                sql += "'%s'" % data[key]
            else:
                sql += str(data[key])
            sql += " "
        sql += "LIMIT 1"
        self.cursor.execute(sql)
        try:
            self.db.commit()
        except:
            self.db.rollback()
