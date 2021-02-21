def add_time(start, duration, day=None):
           
    #START VALUES
    rep_start = start.replace(" ", ":")
    sp_start = rep_start.split(":")
    actualhour = int(sp_start[0])
    actualminutes = int(sp_start[1])
    period = sp_start[2]
    actualperiod = period.upper()
    
    #TIME TO ADD VALUES
    sp_duration = duration.split(":")
    hour = int(sp_duration[0])
    minutes = int(sp_duration[1]) 
    
    #NEW VALUES
    totalhours = actualhour + hour
    newperiod = actualperiod   
    newminutes = actualminutes + minutes
    #print("new minutes: ", newminutes)

    #HANDLING 24H FORMAT (only used for conditions in output)
    if actualperiod == "PM":
        twentyfour_actualhour_format = actualhour + 12
        twentyfour_totalhours_format = twentyfour_actualhour_format + hour
    elif actualperiod == "AM":
        twentyfour_totalhours_format = actualhour + hour

    #HANDLING MINUTES
    if newminutes == 0:
        newminutes = "00"
    elif newminutes > 60:
        additionalhour = int(newminutes/60)
        newminutes = newminutes - 60
        if newminutes == 0:
            newminutes = "00"
        totalhours += additionalhour
        twentyfour_totalhours_format += additionalhour
    if 0 < newminutes < 10:
        newminutes = "0" + str(newminutes)

    #HANDLING PERIODS
    totalperiods = totalhours/12
    if not isinstance(totalperiods,int):
        totalperiods += 1
        periods = int(totalperiods)
    elif isinstance(totalperiods,int):
        periods = totalperiods
    #print("periods ",periods)

    
    checkparity = periods%2
    if totalhours >= 12 and checkparity == 0:
        if actualperiod == "AM":
            newperiod = "PM"
        elif actualperiod == "PM":
            newperiod = "AM"
    elif totalhours >= 12 and checkparity != 0:
        if actualperiod == "AM":
            newperiod = "AM"
        elif actualperiod == "PM":
            newperiod = "PM"

    #HANDLING DAYS COUNT
    dayslater = totalhours/24
    #print(dayslater)
    if dayslater < 1:
        days = 0
    else:
        days = round(dayslater)
    #print("days ",days)

    #HANDLING 12H FORMAT
    if totalhours <= 12:
        newhour = totalhours
    elif totalhours > 12:
        newhour = totalhours%12
        if newhour == 0:
            newhour = "12"

    #HANDLING NEW DAY
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day != None:
        correctedday = day.capitalize()
        actualdayindex = week.index(correctedday)
        newdayindex = (actualdayindex + days) % 7
        newday = ", " + week[newdayindex]
    elif day == None:
        newday = ""

    #FINAL OUTPUT
    
    if 24 <= twentyfour_totalhours_format < 48: 
        new_time = str(newhour) + ":" + str(newminutes) + " " + newperiod + newday + " (next day)"
    elif twentyfour_totalhours_format < 24:
        new_time = str(newhour) + ":" + str(newminutes) + " " + newperiod + newday
    elif twentyfour_totalhours_format >= 48:
        new_time = str(newhour) + ":" + str(newminutes) + " " + newperiod + newday + " (" + str(days) + " days later)" 
    
    #return new_time
    print(new_time)

#TEST EXAMPLES
add_time("11:59 PM", "24:05",)
# expected: "12:04 AM (2 days later)"
add_time("11:59 PM", "24:05", "Wednesday")
# expected: "12:04 AM, Friday (2 days later)"
add_time("11:55 AM", "3:12")
# expected = "3:07 PM"
add_time("5:01 AM", "0:00")
# expected = "5:01 AM"
add_time("3:30 PM", "2:12")
# expected = "5:42 PM"
add_time("11:55 AM", "3:12")
# expected = "3:07 PM"
add_time("11:40 AM", "0:25")
# expected = "12:05 PM"
add_time("3:00 pm", "3:10")
# expected: 6:10 PM
add_time("11:43 AM", "00:20")
# expected: 12:03 PM
add_time("6:30 PM", "205:12")
# expected: 7:42 AM (9 days later)
add_time("3:30 PM", "2:12", "Monday")
# expected = "5:42 PM, Monday"
add_time("8:16 PM", "466:02", "tuESDay")
#expected = "6:18 AM, Monday (20 days later)"
add_time("2:59 AM", "24:00", "Saturday")
# expected: "2:59 AM, Sunday (next day)"
add_time("9:15 PM", "5:30")
# expected = "2:45 AM (next day)"
