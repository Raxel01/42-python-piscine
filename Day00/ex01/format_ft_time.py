import datetime
import time
_time_now_ = datetime.datetime.now()
# year| moth| day | hour | minute | second | microsecond

_seconds_origine_ =time.time()

_seconds_formated = f"{_seconds_origine_:,.4f}"

_second_scientific_notation = f'{_seconds_origine_:.2e}'


_month_ = _time_now_.strftime("%b")
_year_  = _time_now_.year
_day_   = _time_now_.day

_first_part_ = f"Seconds since January 1, 1970: {_seconds_formated} or {_second_scientific_notation} in scientific notation"
_second_part_ = f"{_month_} {_day_} {_year_}"
print(_first_part_)
print(_second_part_)

# transform secnds to readable format using ctime()
# format date objects to readable strings