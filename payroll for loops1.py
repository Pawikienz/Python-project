
def main():
    print('')
    print("-----------------------Payroll System-----------------------")
    print('')
    print("Notice: This Payroll System is only for 'EMPLOYEE' Thankyou. ")

    #Yes
    yeslist = ['Y', 'y', 'YES', 'yes', 'Yes']

    #employee
    namelist = ["Paul", "paul", "Keneth'", "keneth", "mateo",
                "Mateo", "Sydney", "'sydney", "ralph", "Ralph"]

    month1 = ['february'] # 28days

    month2 = ['april', 'june', 'september', 'november'] # 30days

    month3 = ['january', 'march', 'may', 'july', 'august', 'october', 'december'] #31 days

    month123 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                'ocotober', 'november', 'december']

    print('')

    x = 5
    for i in range(5):
        fname = input("Employee Firstname: ")
        lname = input('Employee Lastname: ')
        if fname in namelist:
            print('')
            print('---------------------------------Please select Month---------------------------------')
            print('january,', 'february,', 'march,', 'april,', 'may,', 'june,', 'july,', 'august,', 'september,',
                    'october,', 'november,', 'december')
            print('')
            month = input("Month: ")
            if month in month123:
                print('')
                print("----TYPE 0 IF N/A----")
                print('')
                num_hrs = int(input("Number of hrs. worked in a day: "))

                print('')
                rate = float(input("Rate per hour: "))
                print('')
                dayoff = int(input("DayOff/Holiday: "))
                dayoff = dayoff * num_hrs * rate
                print('')
                absent = int(input("Absent: "))
                absent = absent * num_hrs * rate
                print('')
                halfday = int(input("Halfday: "))
                halfday = halfday * (num_hrs / 2) * rate
                print("                                                     ")
                overtime = int(input("Overtime: "))

                #program will calculate deduction depend on how many days in a month.
                if month in month1:
                    num_hrs = (num_hrs * 24)
                elif month in month2:
                    num_hrs = (num_hrs * 26)
                elif month in month3:
                    num_hrs = (num_hrs * 26)

                #this will total the salary of the employee.
                gross_pay = (num_hrs * rate) + (overtime * rate * 1.25)

                #Deduction of total gross depend on employee salary.

                if gross_pay >= 1000 and gross_pay <= 1249.99:
                    sss = 36.30
                    philhealth = 100
                    pagibig = 29.98
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 1250 and gross_pay <= 1749.99:
                    sss = 54.50
                    philhealth = 100
                    pagibig = 29.98
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 1750 and gross_pay <= 2249.99:
                    sss = 72.70
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 2250 and gross_pay <= 2749.99:
                    sss = 90.80
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 2750 and gross_pay <= 3249.99:
                    sss = 109
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 3250 and gross_pay <= 3749.99:
                    sss = 127.20
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 3750 and gross_pay <= 4249.99:
                    sss = 145.30
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 4250 and gross_pay <= 4749.99:
                    sss = 163.50
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 4750 and gross_pay <= 5249.99:
                    sss = 181.70
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 5250 and gross_pay <= 5749.99:
                    sss = 199.80
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 5750 and gross_pay <= 6249.99:
                    sss = 218
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 6250 and gross_pay <= 6749.99:
                    sss = 236.20
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 6750 and gross_pay <= 7249.99:
                    sss = 254.20
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay

                elif gross_pay >= 7250 and gross_pay <= 7749.99:
                    sss = 272.50
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 7750 and gross_pay <= 8249.99:
                    sss = 290.70
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 8250 and gross_pay <= 8749.99:
                    sss = 308.80
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 8750 and gross_pay <= 9249.99:
                    sss = 327
                    philhealth = 100
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 9250 and gross_pay <= 9749.99:
                    sss = 345.20
                    philhealth = 112
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 9750 and gross_pay <= 10249.99:
                    sss = 363.30
                    philhealth = 112
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 10250 and gross_pay <= 10749.99:
                    sss = 381.50
                    philhealth = 125
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 10750 and gross_pay <= 11249.99:
                    sss = 399.70
                    philhealth = 125
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 11250 and gross_pay <= 11749.99:
                    sss = 417.80
                    philhealth = 137
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 11750 and gross_pay <= 12249.99:
                    sss = 436
                    philhealth = 137
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 12250 and gross_pay <= 12749.99:
                    sss = 454.20
                    philhealth = 150
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 12750 and gross_pay <= 13249.99:
                    sss = 472.30
                    philhealth = 150
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 13250 and gross_pay <= 13749.99:
                    sss = 490.50
                    philhealth = 162
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 13750 and gross_pay <= 14249.99:
                    sss = 508.70
                    philhealth = 162
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 14250 and gross_pay <= 14749.99:
                    sss = 526.80
                    philhealth = 175
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 15250 and gross_pay <= 15749.99:
                    sss = 545
                    philhealth = 175
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay >= 15250 and gross_pay <= 15749.99:
                    sss = 563.20
                    philhealth = 187
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay
                elif gross_pay > 15750:
                    sss = 581
                    philhealth = 187
                    pagibig = 60
                    total_deduct = (sss + philhealth + pagibig + absent + halfday + dayoff)
                    net_pay = (gross_pay - total_deduct)
                    gross = gross_pay
                    total = total_deduct
                    netpay = net_pay



                #receipt
                def Print():
                    print("======================DETAILS======================")
                    print('')
                    print('---------------', month.upper(), '---------------')
                    print('')
                    print('EMPLOYEE NAME:', fname.upper(),lname.upper())
                    print('')
                    print('--GROSS PAY  : {:.1f}--'.format(gross))
                    print('')
                    print('**********DEDUCTION**********')
                    print('PHILHEALTH   : {}'.format(philhealth), ' Pesos')
                    print('PAGIBIG      : {}'.format(pagibig), '  Pesos')
                    print('SSS          : {}'.format(sss), 'Pesos')
                    if dayoff == 0:
                        print("DAYOFF       : NO DAYOFF")
                    else:
                        print('DAYOFF       :', dayoff, 'PESOS')
                    if absent == 0:
                        print("ABSENT       : NO ABSENCE")
                    else:
                        print('ABSENT       :', absent, 'PESOS')
                    if halfday == 0:
                        print("HAFTDAY      : NO HAFTDAY")
                    else:
                        print('HAFTDAY      :', halfday, 'PESOS')
                    print('--TOTAL DEDUCT : {:.1f}--'.format(total))
                    print('**********DEDUCTION**********')
                    print('')
                    print('--NETPAY     : {:.1f}--'.format(netpay))
                    print('')
                    print('---------------', month.upper(), '---------------')
                    print('')
                    print("======================DETAILS======================")
                    Return = input("Do you want to return Main? (Y/N):")
                    print("                                                    ")
                    if Return in yeslist:
                        main()

                # this will ask the employee if he/she wants to see the reciept or restart the system.
                print('')
                menu = input("Do you want to see reciept type Y or N to restart:")
                if menu in yeslist:
                    Print()
                    break
                else:
                    main()


            else:
                print('')
                print("--Please select only from the selection above thankyou--")
                print('')
                # if employee mistaken, the system will ask to restart the system or not to.
                Return = input("Do you want to return Main? (Y/N):")
                print('')
                if Return in yeslist:
                    main()
                else:
                    print('')
                    print("-------------Thankyou Come again!-------------")


        else:
            print('')
            x = x - 1
            print('you have', x, 'tries left')
            print('')
            if x == 0:
                print('')
                print("-----Try Again next Year-----")

main()


