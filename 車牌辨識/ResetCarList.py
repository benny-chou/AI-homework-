import csv

with open('CarList.cvs', 'w', newline='') as csvFile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvFile)

    # 1.直接寫出-標題
    writer.writerow(['車牌', '進場時間',], )