def talkingClock(numbers):
    """Deze functie  zet de cijfernotatie van de tijd om in woorden. De cijfernotatie is een string, numbers
    de output van de functie is ook een string. De klok maakt onderscheid tusssen AM en PM """

    AMorPM = ''
    hourstring = "It's "
    minutesstring = ''
    returnstring = ''
    stringisfound = False

    HoursDict = {'00': 'twelve',
                 '01': 'one',
                 '02': 'two',
                 '03': 'three',
                 '04': 'four',
                 '05': 'five',
                 '06': 'six',
                 '07': 'seven',
                 '08': 'eight',
                 '09': 'nine',
                 '10': 'ten',
                 '11': 'eleven',
                 '12': 'twelve',
                 '13': 'one',
                 '14': 'two',
                 '15': 'three',
                 '16': 'four',
                 '17': 'five',
                 '18': 'six',
                 '19': 'seven',
                 '20': 'eight',
                 '21': 'nine',
                 '22': 'ten',
                 '23': 'eleven'}

    MinutesDictTens = {'2': 'twenty',
                       '3': 'thirty',
                       '4': 'forty',
                       '5': 'fifty'}

    MinutesDictZeroes = {'00':  '',
                         '01': 'oh one',
                         '02': 'oh two',
                         '03': 'oh three',
                         '04': 'oh four',
                         '05': 'oh five',
                         '06': 'oh six',
                         '07': 'oh seven',
                         '08': 'oh eight',
                         '09': 'oh nine',
                         '0': '',
                         '1': 'one',
                         '2': 'two',
                         '3': 'three',
                         '4': 'four',
                         '5': 'five',
                         '6': 'six',
                         '7': 'seven',
                         '8': 'eight',
                         '9': 'nine',
                         '10': 'ten',
                         '11': 'eleven',
                         '12': 'twelve',
                         '13': 'thirteen',
                         '14': 'fourteen',
                         '15': 'fifteen',
                         '16': 'sixteen',
                         '17': 'seventeen',
                         '18': 'eighteen',
                         '19': 'nineteen'}

    hour = numbers[0:2]
    hourstring += (HoursDict.get(hour)) #dit werkt ook: hourstring += HoursDict[hour]

    if int(hour) >= 0 and int(hour)<= 12:
        AMorPM = 'am'
    else:
        AMorPM = 'pm'

    minutes = numbers[3:]
    while not stringisfound:
        key = minutes
        if key in MinutesDictZeroes:
            minutesstring += (MinutesDictZeroes.get(minutes)) # zie comment bij hoursstring
            returnstring = hourstring + ' ' + minutesstring + AMorPM
            stringisfound = True
        else:
            minutesstring += (MinutesDictTens.get(minutes[0])) # zie comment bij hoursstring
            minutesstring = minutesstring + ' ' + (MinutesDictZeroes.get(minutes[1])) # zie comment bij hoursstring
            returnstring = hourstring + ' ' + minutesstring + ' ' + AMorPM
            stringisfound = True
    return returnstring


#roep de functie aan en print de string
print(talkingClock('20:24'))


