#!/usr/bin/env python
import sys

current_city = None
current_count = 0
cityCrimeCountList = {}
cityCrimeDetailsList = {}

for line in sys.stdin:
    line = line.strip()

    city, crime, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
        
    if current_city == city:
        current_count += count
        if (current_city in cityCrimeDetailsList and crime!=''):
            if (crime not in cityCrimeDetailsList[current_city]):
                cityCrimeDetailsList[current_city].append(crime)
        else:
            if crime!='':
            	cityCrimeDetailsList[current_city] = [crime]
    else:
        if current_city:
   	     cityCrimeCountList[current_city] = current_count
        current_count = count
        current_city = city

if current_city == city:
    cityCrimeCountList[current_city] = current_count
   
maxCrimeCity = max(cityCrimeCountList, key = cityCrimeCountList.get)

print('Most of the crimes happening in New York is : %s' % (maxCrimeCity))
print('Total number of crimes reported in that location is : %s' % (cityCrimeCountList[maxCrimeCity]))
print('Types of crimes happening in that location is : %s' % (cityCrimeDetailsList[maxCrimeCity]))


