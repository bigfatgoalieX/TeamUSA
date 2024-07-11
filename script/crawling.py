from bs4 import BeautifulSoup

# 打开并读取HTML文件
with open('info_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取每个队伍的信息
team_blocks = soup.find_all('h2', style='line-height: 42px;')

skip_First = True

for team_block in team_blocks:
    if skip_First:
        skip_First = False
        continue
    
    team_name = team_block.text.strip()  # 提取队伍名字
    print(f"------ {team_name} ------")

    # 找到当前队伍信息块的下一个兄弟节点，直到下一个队伍信息块出现或者文档结束
    next_node = team_block.find_next_sibling()
    while next_node and next_node.name != 'h2':
        
        if next_node.name == 'table':
            # 找到每个球队的相关信息
            player_names = set()
            rows = next_node.find_all('tr')
            for row in rows:
                data_cells = row.find_all('td')
                for cell in data_cells:
                    # 提取球员信息等
                    player_links = cell.find_all('a')
                    for player_link in player_links:
                        player_name = player_link.text.strip()
                        player_names.add(player_name)
            
            # 打印当前队伍的球员名字
            for name in player_names:
                print(name)
        
        # 移动到下一个节点
        next_node = next_node.find_next_sibling()