from datetime import datetime, timedelta
from pytz import timezone
import pytz
utc = pytz.utc
eastern = timezone('US/Eastern')
amsterdam = timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d % H: % M: % S % Z % z'
