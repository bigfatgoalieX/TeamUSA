import requests

# 获取NBA球队页面的HTML内容
teams_url = 'https://basketball.realgm.com/nba/transactions/composition'
response = requests.get(teams_url)

# 保存HTML到本地文件，以便手动检查
with open('info_page.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

print('网页内容已保存到teams_page.html')
