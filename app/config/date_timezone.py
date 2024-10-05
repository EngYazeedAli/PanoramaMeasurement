from datetime import datetime
from dateutil import parser
import pytz



bosnia_timezone = pytz.timezone('Europe/Sarajevo')
current_date = parser.isoparse(datetime.now(bosnia_timezone).strftime("%Y-%m-%dT%H:%M:%S"))