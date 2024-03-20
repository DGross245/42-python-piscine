import time
import datetime

time_past = time.time()
formatted_by_e_time = "{:,}".format(time_past)
formatted_by_comma_time = "{:e}".format(time_past)
current_date = time.strftime("%b %d %Y", time.gmtime())

print("Seconds since January 1, 1970: {} or {} in scientific notation".format(formatted_by_e_time, formatted_by_comma_time))
print(current_date)

# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>