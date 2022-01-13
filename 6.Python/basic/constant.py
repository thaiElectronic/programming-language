# ADC
ADC_BIT = 11
COUNT_ADC = 1 << ADC_BIT
DC_SOURCE = 5060

# STATION CONFIG
STATION_CODE = "TN01"

# STATE CONFIG
CHARGE = "CHARGE"
DISCHARGE = "DISCHARGE"
FULL = "FULL"
NO_LOAD = "NO_LOAD"
BAT_OFF = "BAT_OFF"

# SERVER CONFIG
URL = "https://giamsat03.breedlife.com/api/v1/data"
URL_CONFIG = "https://giamsat03.breedlife.com/api/v1/stations1"
HEADER = {"Content-type": "application/json",
          "Accept": "text/plain"}

# MYSQL CONFIG
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "breedlife@2021"
MYSQL_DB = "bb03"
MYSQL_TABLE_STATION_INFO = "station"
MYSQL_TABLE_DATA = "data"
MYSQL_TABLE_SOH = "soh"
MYSQL_TABLE_CALC_SOH = "calc_soh"

# TIMER CONFIG
TIMER_LOG_DATA = 5
TIMER_SEND_DATA_TO_SERVER = 10
TIMER_TAKE_SAMPLE_SOH = 10
TIMER_SAVE_SOH = 60
TIMER_SEND_SERIAL = 2

# SERIAL CONFIG
SERIAL_PORT = "/dev/ttyMT1"
SERIAL_BAUD = 57600

# PIN LED
PIN_LED = ["140", "24", "25"]


# LOGO
LOGO_TEXT = '''
   ____  ____  ________________  __    ________________     
   / __ )/ __ \/ ____/ ____/ __ \/ /   /  _/ ____/ ____/     
  / __  / /_/ / __/ / __/ / / / / /    / // /_  / __/        
 / /_/ / _, _/ /___/ /___/ /_/ / /____/ // __/ / /___        
/_____/_/_|_/_____/_____/_____/_____/___/_/  _/_____/________
   /  |/  / __ \/ | / /  _/_  __/ __ \/ __ \/  _/ | / / ____/
  / /|_/ / / / /  |/ // /  / / / / / / /_/ // //  |/ / / __  
 / /  / / /_/ / /|  // /  / / / /_/ / _, _// // /|  / /_/ /  
/_/  /_/\____/_/ |_/___/ /_/  \____/_/ |_/___/_/ |_/\____/
'''
