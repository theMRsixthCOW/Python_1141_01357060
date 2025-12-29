import pandas as pd
import os
import re
from datetime import datetime
import glob


def extract_year_from_filename(file):
    """从文件名提取年份（民国年）"""
    match = re.search(r'(\d{3})年', file)
    if match:
        return int(match.group(1))
    return None

def read_ods_file(filepath):
    """读取.ods文件并返回DataFrame"""
    try:
        df = pd.read_excel(filepath, engine='odf', header=None)
        return df
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def parse_crime_data(df):
    """解析犯罪数据，返回案件类别和发生数的字典"""
    crime_data = {}
    
    if df is None or df.empty:
        return crime_data
    
    # 查找包含案件类别的行（通常是"案類別"所在的行）
    header_row_idx = None
    occurrence_row_idx = None
    solved_row_idx = None
    
    for idx, row in df.iterrows():
        # 检查第一列或第二列
        for col_idx in range(min(3, len(df.columns))):
            cell_value = str(row[col_idx]).strip() if pd.notna(row[col_idx]) else ''
            
            if '案類別' in cell_value or '案件別' in cell_value:
                header_row_idx = idx
            elif cell_value == '發生合計' or cell_value == '发生合计':
                occurrence_row_idx = idx
            elif cell_value == '破獲合計' or cell_value == '破获合计':
                solved_row_idx = idx
    
    if header_row_idx is None or occurrence_row_idx is None:
        return crime_data
    
    # 提取案件类别（从标题行）
    header_row = df.iloc[header_row_idx]
    occurrence_row = df.iloc[occurrence_row_idx]
    solved_row = df.iloc[solved_row_idx] if solved_row_idx is not None else None
    
    # 遍历列，提取每个案件类别的数据
    for col_idx in range(len(df.columns)):
        case_type = str(header_row[col_idx]).strip() if pd.notna(header_row[col_idx]) else ''
        
        # 跳过空列和非案件类别列
        if not case_type or case_type == 'nan' or case_type == '案類別' or case_type == '案件別':
            continue
        
        # 提取发生数
        occurrence = 0
        try:
            val = occurrence_row[col_idx]
            if pd.notna(val) and val != '' and val != '-' and val != '--':
                occurrence = int(float(val))
        except:
            continue
        
        # 提取破获数
        solved = 0
        if solved_row is not None:
            try:
                val = solved_row[col_idx]
                if pd.notna(val) and val != '' and val != '-' and val != '--':
                    solved = int(float(val))
            except:
                pass
        
        # 记录数据
        if case_type and occurrence >= 0:
            if case_type not in crime_data:
                crime_data[case_type] = {'occurrence': 0, 'solved': 0, 'count': 0}
            crime_data[case_type]['occurrence'] += occurrence
            crime_data[case_type]['solved'] += solved
            crime_data[case_type]['count'] += 1
    
    return crime_data

def function_1(file_list, base_path):
    """功能1：合并112-113年数据，输出总发生量和前三类别"""
    all_data = {}
    files_processed = 0
    
    for filename in file_list:
        year = extract_year_from_filename(filename)
        if year and 112 <= year <= 113:
            filepath = os.path.join(base_path, filename)
            if not os.path.exists(filepath):
                continue
            df = read_ods_file(filepath)
            if df is None:
                continue
            crime_data = parse_crime_data(df)
            if crime_data:
                files_processed += 1
            
            for case_type, data in crime_data.items():
                if case_type not in all_data:
                    all_data[case_type] = {'occurrence': 0, 'solved': 0, 'count': 0}
                all_data[case_type]['occurrence'] += data['occurrence']
                all_data[case_type]['solved'] += data['solved']
                all_data[case_type]['count'] += data['count']
    
    if not all_data:
        print("Error: No valid crime data found for years 112-113")
        return
    
    # 计算总发生量
    total_occurrence = sum(data['occurrence'] for data in all_data.values())
    print(f"合併後發生量總和:{total_occurrence}")
    print()
    
    # 找出前三类别
    sorted_data = sorted(all_data.items(), key=lambda x: x[1]['occurrence'], reverse=True)
    print("前三類別:")
    for i in range(min(3, len(sorted_data))):
        case_type, data = sorted_data[i]
        print(f"{case_type}:{data['occurrence']}")

def function_2(file_list, base_path):
    """功能2：113年发生量最多的前三类别"""
    all_data = {}
    files_processed = 0
    
    for filename in file_list:
        year = extract_year_from_filename(filename)
        if year == 113:
            filepath = os.path.join(base_path, filename)
            if not os.path.exists(filepath):
                continue
            df = read_ods_file(filepath)
            if df is None:
                continue
            crime_data = parse_crime_data(df)
            if crime_data:
                files_processed += 1
            
            for case_type, data in crime_data.items():
                if case_type not in all_data:
                    all_data[case_type] = {'occurrence': 0}
                all_data[case_type]['occurrence'] += data['occurrence']
    
    if not all_data:
        print("Error: No valid crime data found for year 113")
        return
    
    # 找出前三类别
    sorted_data = sorted(all_data.items(), key=lambda x: x[1]['occurrence'], reverse=True)
    print("前三類別:")
    for i in range(min(3, len(sorted_data))):
        case_type, data = sorted_data[i]
        print(f"{case_type}:{data['occurrence']}")

def function_3(file_list, base_path):
    """功能3：112-113年各类别平均发生量前三名"""
    all_data = {}
    files_processed = 0
    
    for filename in file_list:
        year = extract_year_from_filename(filename)
        if year and 112 <= year <= 113:
            filepath = os.path.join(base_path, filename)
            if not os.path.exists(filepath):
                continue
            df = read_ods_file(filepath)
            if df is None:
                continue
            crime_data = parse_crime_data(df)
            if crime_data:
                files_processed += 1
            
            for case_type, data in crime_data.items():
                if case_type not in all_data:
                    all_data[case_type] = {'occurrence': 0, 'count': 0}
                all_data[case_type]['occurrence'] += data['occurrence']
                all_data[case_type]['count'] += data['count']
    
    if not all_data:
        print("Error: No valid crime data found for years 112-113")
        return
    
    # 计算平均值
    avg_data = {}
    for case_type, data in all_data.items():
        if data['count'] > 0:
            avg_data[case_type] = data['occurrence'] / data['count']
    
    # 找出前三名
    sorted_data = sorted(avg_data.items(), key=lambda x: x[1], reverse=True)
    print("平均發生量前三:")
    for i in range(min(3, len(sorted_data))):
        case_type, avg_val = sorted_data[i]
        print(f"{case_type}:{avg_val:.2f}")

def function_4(file_list, base_path):
    """功能4：113年案件总数和平均破获率"""
    all_data = {}
    total_occurrence = 0
    total_solved = 0
    files_processed = 0
    
    for filename in file_list:
        year = extract_year_from_filename(filename)
        # 113年数据，算到113年12月30日至114年1月5日
        if year == 113 or (year == 114 and '1月' in filename and ('1日' in filename or '5日' in filename)):
            filepath = os.path.join(base_path, filename)
            if not os.path.exists(filepath):
                continue
            df = read_ods_file(filepath)
            if df is None:
                continue
            crime_data = parse_crime_data(df)
            if crime_data:
                files_processed += 1
            
            for case_type, data in crime_data.items():
                if case_type not in all_data:
                    all_data[case_type] = {'occurrence': 0, 'solved': 0}
                all_data[case_type]['occurrence'] += data['occurrence']
                all_data[case_type]['solved'] += data['solved']
    
    if not all_data:
        print("Error: No valid crime data found for year 113")
        return
    
    # 计算总案件数
    total_occurrence = sum(data['occurrence'] for data in all_data.values())
    total_solved = sum(data['solved'] for data in all_data.values())
    
    print(f"113案件總數:{total_occurrence}")
    print()
    
    # 计算平均破获率
    if total_occurrence > 0:
        avg_solve_rate = total_solved / total_occurrence
        print(f"平均破獲率:{avg_solve_rate:.2f}")
    else:
        print("平均破獲率:0.00")

def main():
    # 读取file.csv
    csv_path = 'file.csv'
    
    if not os.path.exists(csv_path):
        print("Error: file.csv not found")
        print(f"Current directory: {os.getcwd()}")
        return
    
    # 读取文件列表
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            file_list = [line.strip() for line in f if line.strip()]
    except:
        try:
            with open(csv_path, 'r', encoding='big5') as f:
                file_list = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error reading file.csv: {e}")
            return
    
    # 如果csv包含表头，去掉
    if file_list and not file_list[0].endswith('.ods'):
        file_list = file_list[1:]
    
    if not file_list:
        print("Error: No .ods files found in file.csv")
        return
    
    base_path = '.'  # .ods文件在当前目录
    
    while True:
        try:
            choice = input("輸入功能代碼：")
            choice = choice.strip()
            
            if not choice.isdigit():
                print("Error:Invalid input")
                continue
            
            choice = int(choice)
            
            if choice < 1 or choice > 4:
                print("Error:Invalid input")
                continue
            
            if choice == 1:
                function_1(file_list, base_path)
            elif choice == 2:
                function_2(file_list, base_path)
            elif choice == 3:
                function_3(file_list, base_path)
            elif choice == 4:
                function_4(file_list, base_path)
            
            print()  # 额外换行
            
        except KeyboardInterrupt:
            print("\n程序结束")
            break
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()