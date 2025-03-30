'''
某宿舍有6个人A、B 、C、D、E、F，
分别有现金10万元，20万元，30万元，40万，50万元，60万元。
银行提供一种5年期利率为5%的定期存单，
请编写python程序，计算每个人在5年后的资产价值，
并保存到CSV文件中，表头为“姓名、资产现值、资产未来值”。
提交代码和结果文件
'''

import  csv
def calculate(cash):
    return float(cash)*(1+0.05)**5

Name=['A','B','C','D','E','F']
Assets=[10,20,30,40,50,60]
Items=[]

for i in range(len(Name)):
    PV=Assets[i]
    FV=calculate(PV)
    Items.append([Name[i],PV,FV])

with open("Asset_value.csv","w",encoding="utf-8")as file:
    writer=csv.writer(file)
    writer.writerow(["姓名","资产现值","资产未来值"])
    for Item in Items:
        writer.writerow(Item)