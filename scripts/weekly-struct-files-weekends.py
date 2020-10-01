months = {
    1: 31,
    2: 28, # unless it's leap
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month_name = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

start_month = 10 # Oct
start_monday = 5 # Oct 5
start_week = 1
exclude_weekends = True
end_month = 12 # Dec
end_day = 18 # Dec 18, last day of classes
num_days = 7

if exclude_weekends:
    num_days = 5


month = start_month
cur_day = start_monday
week = start_week

while week < 53: # loop through the year
    # write week-##.md
    filename = "week-" + str(week).zfill(2) + ".md" # pad with zeros
    print("Writing", filename)
    md_file = open(filename, "w")
    md_file.write("---\n")
    md_file.write("title: Week " + str(week) + "\n")
    md_file.write("---\n")

    for day in range(0, num_days):
        if cur_day > months[month]:
            cur_day = cur_day - months[month] # e.g., 10/31->11/1
            month += 1
        if month == end_month:
            if cur_day == end_day:
                #md_file.write(str(month) + "/" + str(cur_day)+ "\n")
                md_file.write(month_name[month] + " " + str(cur_day)+ "\n")
                md_file.write(": [](#)\n\n")
                md_file.close()
                break # Finish processing
        md_file.write(month_name[month] + " " + str(cur_day)+ "\n")
        md_file.write(": [](#)\n\n")
        cur_day += 1

    if month == end_month and cur_day >= end_day:
        md_file.close()
        break # Finish processing

    md_file.close() # finish writing this week's dates
    week += 1
    if exclude_weekends:
        cur_day +=2
