print("This is program for bmi calculation")
gender = input("Enter the gender: ")
HeightCm = float(input("Enter height: "))
WeightKg = float(input("Enter Weight: "))
bmi = WeightKg /( HeightCm ** 2 )
if bmi < 18.4:
    print("Under weight")
elif bmi >= 18.5 and bmi <= 24.9:
            print("Normal weight")
elif bmi>= 25 and bmi <= 29.9:
            print("Over weight")
elif bmi>= 30 and bmi <= 34.9:
            print("Moderately obese")
elif bmi>= 35 and bmi <= 39.9:
            print("Severly obese")
elif bmi>= 40:
                    print("Very Severly obese")
else:
                        print("Information incorrect")

#For Calculating count of overweight
import pandas as pd
from urllib.request import urlopen
import urllib
#import urlopen
data=('dataset.data')#assuming the data is stored in dataset
names=['Gender','HeightCm','WeightKg']
cd=pd.read_csv(urlopen(data),names=names)
datatemp=[cd]
cd.head()
bmi = WeightKg /( HeightCm ** 2 )
if bmi < 18.4:
    print("Under weight")
elif bmi >= 18.5 and bmi <= 24.9:
            print("Normal weight")
elif bmi>= 25 and bmi <= 29.9:
            print("Over weight")
elif bmi>= 30 and bmi <= 34.9:
            print("Moderately obese")
elif bmi>= 35 and bmi <= 39.9:
            print("Severly obese")
elif bmi>= 40:
                    print("Very Severly obese")
else:
                        print("Information incorrect")
a = bmi.count("Over weight")
print("overweight count=",a)