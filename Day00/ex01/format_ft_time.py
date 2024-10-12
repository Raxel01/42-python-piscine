import datetime
import time
_time_now_ = datetime.datetime.now()
# year| moth| day | hour | minute | second | microsecond

_seconds_ = time.time()
_second_scientific_notation = "{:e}".format(_seconds_)


_month_ = _time_now_.strftime("%b")
_year_  = _time_now_.year
_day_   = _time_now_.day
_first_part_ = f"Seconds since January 1, 1970: {_seconds_} or {_second_scientific_notation} in scientific notation"
_second_part_ = f"{_month_} {_day_} {_year_}"
print(_first_part_)
print(_second_part_)

# transform seonds to readable format using ctime()

# format date objects to readable strings