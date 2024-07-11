import requests
import os

# 定义要爬取的年份范围
start_year = 1984
end_year = 2024

folder_path = 'D:\Projects\Project1_TeamUSA\data\htmls'

for year in range(start_year, end_year + 1):
    # 构造每个年份的URL
    teams_url = f'https://basketball.realgm.com/nba/transactions/composition/{year}'
    
    # 获取NBA球队页面的HTML内容
    response = requests.get(teams_url)
    
    # 保存HTML到本地文件，以便手动检查
    file_path = os.path.join(folder_path, f'teams_page_{year}.html')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    print(f'网页内容已保存到{file_path}')

print('所有年份的网页内容已保存。')
