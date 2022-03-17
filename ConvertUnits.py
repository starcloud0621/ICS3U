number = int(input())
unit = input()



def ConvertUnits(ToConvert,FinalUnits):
    units = {"cm": 2.54, "in": 0.393701, "lb": 2.20462, "kg":0.453592}
    print(units[FinalUnits]*ToConvert)

ConvertUnits(number,unit)
