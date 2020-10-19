import re


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

# {'0AM': 0, ..., '12PM':12, ..., '11PM':23}
military_map = {f'{i}AM' if i in range(0,12) else f'{i%12}PM' if i != 12 else '12PM':i for i in range(0,24)}

# {0:0, ..., 12:12, 13:1, ..., 23:11}
am_pm_map = {i : i%12 if i != 12 and i != 0 else 12 for i in range(0,24)}


def hoursMap(hrs):
    '''Maps hours from AM/PM' to military time'''
    return military_map[hrs]

def invMap(hrs):
    '''Maps hours from military time to AM/PM'''
    return am_pm_map[hrs]

def calcHrMin(st_hrs, dur_hrs, st_min, dur_min, sgn):
    ''''''
    # Convert input hours to 0-23 and add duration hours
    hr_mapped = hoursMap(st_hrs + sgn)
    total_hours = hr_mapped + dur_hrs
    
    # Calculate the total minutes and adjust the total hours if necessary 
    total_min = st_min + dur_min
    if total_min > 59:
        total_hours += 1
        total_min = total_min % 60
        
    return total_hours, total_min

def add_time(start, duration, starting_day=None):
    '''
    Args:
        start (str): a start time in the 12-hour clock format (ending in AM or PM)
        
        duration (str): a duration time that indicates the number of hours and minutes
        
        starting_day (str or None): (optional) a starting day of the week, case insensitive
    
    Returns:
        new_time (str):
    
    Notes:
        - Assumes that the start times are valid times. The minutes in the duration time will be 
          a whole number less than 60, but the hour can be any whole number.
          
        - If the result will be the next day, it should show (next day) after the time. If the 
          result will be more than one day later, it should show (n days later) after the time, 
          where "n" is the number of days later.
        
        - If the function is given the optional starting day of the week parameter, then the output 
          should display the day of the week of the result. The day of the week in the output should 
          appear after the time and before the number of days later.
        
        - Example implementations include:
        
            >> add_time("3:00 PM", "3:10")
            6:10 PM

            >> add_time("11:30 AM", "2:32", "Monday")
            2:02 PM, Monday

            >> add_time("11:43 AM", "00:20")
            12:03 PM

            >> add_time("10:10 PM", "3:30")
            1:40 AM (next day)

            >> add_time("11:43 PM", "24:20", "tueSday")
            12:03 AM, Thursday (2 days later)

            >> add_time("6:30 PM", "205:12")
            7:42 AM (9 days later)
    '''      
    # Parse the input information
    rgx_start, rgx_duration = r'(\d+):(\d+)\s([A|P]M)', r'(\d+):(\d+)'
    parsed_start, parsed_duration = re.findall(rgx_start, start), re.findall(rgx_duration, duration)
    
    # Extract the parsed information
    hr_start, min_start, sign = parsed_start[0][0], int(parsed_start[0][1]), parsed_start[0][2]
    hr_dur, min_dur =  int(parsed_duration[0][0]), int(parsed_duration[0][1])
        
    # Check for formatting error
    if min_start > 59 or min_dur > 59:
        return 'Error: The start/duration is in an incorrect format'
    
    total_hours, total_min = calcHrMin(hr_start, hr_dur, min_start, min_dur, sign) 
        
    # Calculate how many days have passed
    n = total_hours // 24
    
    new_hrs = invMap(total_hours % 24) 
    new_sign = 'AM' if total_hours % 24 < 12 else 'PM'    
    new_time = f"{new_hrs}:{'' if total_min > 9 else 0}{total_min} {new_sign}"
    
    calc_day = ''
    if starting_day != None:
        temp = [*map(lambda x: x.lower(), days)] # lowercase days of the week
        idx = temp.index(starting_day.lower()) + n
        calc_day = f', {days[idx%7]}'
    return f"{new_time}{calc_day}{'' if n==0 else ' (next day)' if n==1 else f' ({n} days later)'}" 

add_time("6:30 PM", "205:12")