height = input('請輸入身高： ')
height = int(height)
weight = input('請輸入體重： ')
weight = int(weight)

height = height / 100 #換成公尺

bmi = weight / (height * height)
print(bmi)

if bmi < 18.5:
    print('您的BMI值為', int(bmi), ',屬於「過輕」')
elif bmi >= 18.5 and bmi < 24:
    print('您的BMI值為', int(bmi), ',屬於「正常」')
elif bmi >= 24 and bmi < 27:
    print('您的BMI值為', int(bmi), ',屬於「過重」')
elif bmi >= 27 and bmi < 30:
    print('您的BMI值為', int(bmi), ',屬於「輕度肥胖」')
elif bmi >= 30 and bmi < 35:
    print('您的BMI值為', int(bmi), ',屬於「標準肥胖」')
else:
    print('您的BMI值為', int(bmi), ',屬於「史詩級肥胖」')