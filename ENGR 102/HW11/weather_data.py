# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo
# Section:      599
# Assignment:   11.3 LAB: weather data
# Date:         11/13/2022
#

# open file
with open('WeatherDataCLL.csv') as f:
    lines = f.readlines()

header = lines[0].strip().split(',')
lines.remove(lines[0])

# dictionary
data = {}
for line in lines:
    date = line.strip().split(',')
    # dictionary for current date
    data[date[0]] = {}
    for i in range(1, len(header)):
        data[date[0]][header[i]] = float(date[i])

highTemp = []
lowTemp = []
precip = []

for key in data:
    highTemp.append(data[key]['Maximum Temperature (F)'])
    lowTemp.append(data[key]['Minimum Temperature (F)'])
    precip.append(data[key]['Precipitation (in)'])
maxTemp = max(highTemp)
minTemp = min(lowTemp)
average_precip = sum(precip) / len(precip)

# outputting initial information
print(f'3-year maximum temperature: {maxTemp:.0f} F'
      f'3-year minimum temperature: {minTemp:.0f} F'
      f'3-year average precipitation: {average_precip:.3f} inches\n')

iMonth = input("Please enter a month: ")
iYear = input("Please enter a year: ")
print()

month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}
Date0 = str(month[iMonth]) + '/'
Date1 = '/' + iYear

# create empty lists
avg = []
wind = []
precipitation = []

# loop through the number of days in a month
for i in range(31):
    dates = Date0 + str(i + 1) + Date1
    if dates in data:
        avg.append(data[dates]['Maximum Temperature (F)'])
        wind.append(data[dates]['Average Daily Wind Speed (mph)'])
        precipitation.append(data[dates]['Precipitation (in)'])
avgTemp = sum(avg) / len(avg)
meanWind = sum(wind) / len(wind)

highWind = 0
for day in wind:
    if day > 10:
        highWind += 1
highWind /= len(wind) / 100
meanPrecip = sum(precipitation) / len(precipitation)
daysRain = 0

for day in precipitation:
    if day > 0:
        daysRain += 1
daysRain /= len(precipitation) / 100

print(f'For {iMonth} {iYear}:'
      f'Mean maximum daily temperature: {avgTemp:.1f} F'
      f'Mean daily wind speed: {meanWind:.2f} mph'
      f'Percentage of days with precipitation: {daysRain:.1f}%')
