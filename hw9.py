import requests
import csv
import sys
from io import StringIO
import pandas as pd

CSV_FILE = 'file.csv' 

def read_ods_file(filename):
    try:
        df = pd.read_excel(filename, engine='odf')
        return df
    except Exception as e:
        print(f"讀取失敗:{filename}")
        return None
    
    
def download_data():
    r = requests.get('https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=FD234310-90DB-42C8-845B-5E405051D8DD',verify=False)
    r.encoding = 'utf-8'
    return list(csv.DictReader(StringIO(r.text)))

def is_year_in_range(row, start, end):
    year = int(row["統計年"])
    return start <= year <= end

def get_year(row):
    return int(row["統計年"])

def get_count(row):
    return int(row["發生數"])

def get_rate(row):
    try:
        return float(row["破獲率"])
    except:
        return 0.0

def get_type(row):
    return row["案件類別"]

def top3_types(data):
    stat = {}
    for r in data:
        t = get_type(r)
        c = get_count(r)
        stat[t] = stat.get(t, 0) + c
    top3 = sorted(stat.items(), key=lambda x: x[1], reverse=True)[:3]
    return top3

def func1(rows):
    data = [r for r in rows if is_year_in_range(r, 112, 113)]
    total = sum(get_count(r) for r in data)
    print(f"合併後發生量總和:{total}")
    print("前三類別:")
    for t, c in top3_types(data):
        print(f"{t}:{c}")

def func2(rows):
    data = [r for r in rows if get_year(r) == 113]
    print("前三類別:")
    for t, c in top3_types(data):
        print(f"{t}:{c}")

def func3(rows):
    data = [r for r in rows if is_year_in_range(r, 112, 113)]
    stat = {}
    count_years = 2

    for r in data:
        t = get_type(r)
        c = get_count(r)
        stat[t] = stat.get(t, 0) + c

    avg = [(t, stat[t] / count_years) for t in stat]
    top3 = sorted(avg, key=lambda x: x[1], reverse=True)[:3]

    print("平均發生量前三:")
    for t, a in top3:
        print(f"{t}:{a:.2f}")

def func4(rows):
    data = [r for r in rows if get_year(r) == 113]
    total_cases = sum(get_count(r) for r in data)

    rates = [get_rate(r) for r in data if get_rate(r) > 0]
    avg_rate = sum(rates) / len(rates) if rates else 0

    print(f"該年份案件總數:{total_cases}")
    print(f"平均破獲率:{avg_rate:.2f}")

def main():
    data = download_data()

    try:
        mode = input().strip()
        if not mode.isdigit():
            print("Error:Invalid input")
            return
        mode = int(mode)

        if mode == 1:
            func1(data)
        elif mode == 2:
            func2(data)
        elif mode == 3:
            func3(data)
        elif mode == 4:
            func4(data)
        else:
            print("Error:Invalid input")
    except:
        print("Error:Invalid input")

if __name__ == "__main__":
    main()
