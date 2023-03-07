import datetime

def scrubName(string):
  return string.replace("-", " ").title()

def scrubUrl(string):
  return string.replace(" ", "-").lower()

def relevantTimes(t):
    timeObj = datetime.datetime.strptime("1970-01-01 "+t, "%Y-%m-%d %I:%M %p")
    roundedTime = datetime.datetime(
        timeObj.year, timeObj.month, timeObj.day,
        timeObj.hour, 15 * (timeObj.minute // 15), 0
    )

    relevantTimes = []
    for i in range(-2, 3):
        if i == 0:
            continue
        relevantTime = roundedTime + datetime.timedelta(minutes=i * 15)
        formattedTime = relevantTime.strftime("%I:%M %p")
        if formattedTime[0] == "0":
            formattedTime = formattedTime[1:]
        relevantTimes.append(formattedTime)

    return relevantTimes