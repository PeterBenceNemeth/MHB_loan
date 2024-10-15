# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy_financial as npf
from readable_number import ReadableNumber
import matplotlib.pyplot as plt
import numpy as np


creditAmount = 50000000 # 50 000 000 Ft
rate = 0.0719/12
years = 25
nper = years * 12 #months
nper_ori = nper
futureValue = 0 #expected to be repaid

Bank = 0#10000000 # Bank account

oriMonthly = npf.pmt(rate, nper, creditAmount, futureValue)



presentPaid = []
interestPaid = []
yeah = []
bAccount = []
bInterest = []
returned = []
currentValue = [creditAmount]
modCredit = [creditAmount]
i = range(1, nper+1)
for i in range(1, nper+1): #
    if currentValue[-1] > 0:

        yeah.append(i)
        bAccount.append(Bank)
        bInterest.append(bAccount[i-1]*rate)
        interestPaid.append( npf.ipmt(rate, i, nper, modCredit[-1]) )
        presentPaid.append( npf.ppmt(rate, i, nper, modCredit[-1]) )
        currentValue.append(currentValue[i-1] + presentPaid[i-1])

        if i%6 == 0: # Every sixth month credit amount to be lowered
            returned.append(bInterest[i - 6] + bInterest[i - 1] + bInterest[i - 2] + bInterest[i - 3] + bInterest[i - 4] + bInterest[i - 5])
            if returned[-1]*2 > currentValue[-1]*0.7: #max 70%
                returned[-1] = currentValue[-1]*0.7 / 2

            currentValue[i] = currentValue[-1] - returned[-1]
            modCredit.append(modCredit[-1]-returned[-1])

            # recalculate loan length
            #nper = npf.nper(rate,oriMonthly,modCredit[-1],0)
            nper = npf.nper(rate,oriMonthly,modCredit[-1]-currentValue[0]+currentValue[-1],0)

            tmp_i = npf.ipmt(rate,i,nper,modCredit[-1])

            tmp_p = npf.ppmt(rate, i, nper, modCredit[-1])


            tmp_pmt = npf.pmt(rate, nper, modCredit[-1], futureValue)




print("nper: ", nper)
print ("Hónapok", max(yeah),
       "; Évek: ", max(yeah)/12)
print("Törlesztő: ", oriMonthly)
print("Interest: ", str(ReadableNumber(sum(interestPaid))), " Ft")
print("Tőke: ", str(ReadableNumber(sum(presentPaid) - sum(returned))), " Ft")
print("Fizetett tőke: ", str(ReadableNumber(sum(presentPaid) )), " Ft")
print("Kamatozott Tőke: ", str(ReadableNumber( sum(returned))), " Ft")

print(presentPaid)



#print(oriMonthly)
#print(interestPaid)
#print(presentPaid)
#num = 7
#Egy = interestPaid[num]+presentPaid[num]
#print(oriMonthly)
#print(Egy)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#https://numpy.org/doc/1.17/reference/generated/numpy.ppmt.html


# Plotting
plt.figure(figsize=(10, 5))
plt.plot(years, presentPaid, label='Total Amount', color='blue')
plt.plot(years, interestPaid, label='Interest Amount', color='orange')
plt.title('Loan Amount and Interest Over Time')
plt.xlabel('Years')
plt.ylabel('Amount ($)')
plt.xticks(years)
plt.legend()
plt.grid()
plt.show()
