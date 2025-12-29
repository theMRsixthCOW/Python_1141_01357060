import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os

# Set Chinese font for Windows
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

def get_pyramid_data(file_path):
    df = pd.read_excel(file_path, sheet_name='113', header=None)
  
    male_row = None
    female_row = None
    
    for i in range(len(df)):
        val_0 = str(df.iloc[i, 0]).replace(' ', '').replace('\n', '').replace('\u3000', '').strip()
        val_1 = str(df.iloc[i, 1]).strip()
        
        if '總計' in val_0 and val_1 == '男':
            male_row = df.iloc[i]
            female_row = df.iloc[i+1]
            break
            
    if male_row is None:
        raise ValueError("Could not find '總計' row for Male.")

    age_bins = []
    male_counts = []
    female_counts = []
    
    age_bins.append('0-4')
    male_counts.append(male_row[3] + male_row[4])
    female_counts.append(female_row[3] + female_row[4])

    col_start = 9
    col_end = 28
    current_age = 5
    
    for col in range(col_start, col_end + 1):
        if col == 28:
            label = '100+'
        else:
            label = f"{current_age}-{current_age+4}"
        
        age_bins.append(label)
        male_counts.append(male_row[col])
        female_counts.append(female_row[col])
        current_age += 5
        
    return age_bins, male_counts, female_counts

def get_aging_trend_data(file_path):
    trend_data = {} # Key: City, Value: {Year: Index}
    years = [str(y) for y in range(103, 114)]
    
    for year in years:
        try:
            df = pd.read_excel(file_path, sheet_name=year, header=None)
        except:
            print(f"Sheet {year} not found.")
            continue

        for i in range(len(df)):
            val_1 = str(df.iloc[i, 1]).strip()
            
            if val_1 == '男':
                region_raw = str(df.iloc[i, 0])
                region = region_raw.replace(' ', '').replace('\n', '').replace('\u3000', '').strip()
                
                # Filter out 'nan', '總計', '省'
                if region == 'nan' or '總計' in region or '省' in region:
                    continue
                
                total_row = df.iloc[i-1]
                
                if str(total_row[1]).strip() != '計':
                    continue
                
                
                p0_4 = total_row[3] + total_row[4]
                p5_9 = total_row[9]
                p10_14 = total_row[10]
                pop_0_14 = p0_4 + p5_9 + p10_14
                
                pop_65_plus = sum(total_row[col] for col in range(21, 29))
                
                if pop_0_14 == 0:
                    idx = 0
                else:
                    idx = (pop_65_plus / pop_0_14) * 100
                
                if region not in trend_data:
                    trend_data[region] = {}
                trend_data[region][int(year)] = idx

    return pd.DataFrame(trend_data).sort_index()

def main():
    file_path = '縣市人口按性別及五齡組.xlsx'
    
    print("Processing Pyramid Data...")
    bins, male, female = get_pyramid_data(file_path)
    
    print("Processing Aging Index Trend...")
    trend_df = get_aging_trend_data(file_path)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    
    y = range(len(bins))
    ax1.barh(y, [-m for m in male], color='cornflowerblue', label='男性')
    ax1.barh(y, female, color='lightcoral', label='女性')
    
    ax1.set_yticks(y)
    ax1.set_yticklabels(bins)
    ax1.set_xlabel('人口數')
    ax1.set_ylabel('年齡組 (歲)')
    ax1.set_title('台灣人口金字塔 (113年)')
    ax1.legend()
    
    from matplotlib.ticker import FuncFormatter
    ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(abs(x))}'))
    
    ax1.grid(axis='x', linestyle='--', alpha=0.7)

    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h', 'H', '+', 'x', 'd']
    
    for i, city in enumerate(trend_df.columns):
        marker = markers[i % len(markers)]
        ax2.plot(trend_df.index, trend_df[city], marker=marker, label=city, linewidth=1.5, markersize=4)
    
    ax2.set_title('各縣市老化指數趨勢 (103-113年)')
    ax2.set_xlabel('年份')
    ax2.set_ylabel('老化指數 (65歲以上/0-14歲 * 100)')
    # ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', ncol=2, fontsize='small')
    ax2.legend(loc='best', ncol=3, fontsize='x-small') 
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_xticks(trend_df.index)
    ax2.set_xticklabels([f'{y}年' for y in trend_df.index])

    plt.suptitle('台灣人口結構與老化趨勢分析', fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
