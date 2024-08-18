
def convert():
    userinp=input('To what units are you converting today? Metric or Imperial? ')

    if userinp.lower() =='metric' or userinp.lower() == 'm':
        metric_input=input('Temperature(t) or Weight(w) or Measurements(m)? ')
        if metric_input.lower() == 'temperature' or  metric_input.lower()=='t':
            print('Enter Fahrenit Degree:')
            fdegree= int(input())
            #convert
            cdegree = (fdegree - 32)/(1.8)
            cdegree = round(cdegree,2)
            print(f'{fdegree} F,equals {cdegree} C')
        elif metric_input.lower() =='weight' or metric_input.lower() =='w':
            print('Enter Pounds(lbs):')
            pweight= float(input())
            #convert
            kgweight = pweight * 0.4536
            kgweight = round(kgweight, 2)
            print (f'{pweight}lbs is equals to {kgweight}kg')
        elif metric_input.lower() == 'measurements' or metric_input.lower() =='m':
            print('Enter Feet(s):')
            Feet = float(input())
            Meter = Feet/3.28084
            Meter = round(Meter,2)
            print (f'{Feet}ft is equals to {Meter}m')
    
    elif userinp.lower() == 'imperial' or userinp.lower() == 'i':
        metric_input2=input('Temperature(t) or Weight(w) or Measurements(m)? ')
        if metric_input2.lower() == 'temperature' or metric_input2.lower() == 't':
            print('Enter Celsius Degree:')
            cdegree= int(input())
            #convert
            fdegree = (cdegree *(9/5))+32
            fdegree = round(fdegree,2)
            print(f'{cdegree}C,equals {fdegree} F')
        elif metric_input2.lower() == 'weight' or metric_input2.lower() =='w':
            print('Enter Kilogram(s):')
            kgweight = float(input())
            pweight = kgweight / 0.4536
            pweight = round(pweight,2)
            print (f'{kgweight}kg is equals to {pweight}lbs')
        elif metric_input2.lower() == 'measurements' or metric_input2.lower() =='m':
            print('Enter Meter(s):')
            meter = float(input())
            feet = meter*3.28084
            feet = round(feet,2)
            print (f'{meter}m is equals to {feet}ft')
    else:
        print('error') 

def main():
    while True:
        convert()
        repeat = input("Do you want to make another conversion? Yes/No: ")
        if repeat.lower()!='yes':
            print("Goodbye :)")
            break
    
if __name__=="__main__":
    main()
