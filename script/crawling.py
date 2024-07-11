import os
from bs4 import BeautifulSoup

# 定义文件夹路径
folder_name = r'D:\Projects\Project1_TeamUSA\data\htmls'
output_folder = r'D:\Projects\Project1_TeamUSA\data\txts'

# 获取文件夹中所有HTML文件
html_files = [file for file in os.listdir(folder_name) if file.endswith('.html')]

# 处理每个HTML文件
for html_file in html_files:
    input_path = os.path.join(folder_name, html_file)
    
    # 打开并读取HTML文件
    with open(input_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取每个队伍的信息
    team_blocks = soup.find_all('h2', style='line-height: 42px;')

    skip_First = True

    # 创建输出文件
    output_file_name = f"{os.path.splitext(html_file)[0]}_roster_composition.txt"
    output_path = os.path.join(output_folder, output_file_name)
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for team_block in team_blocks:
            if skip_First:
                skip_First = False
                continue
            
            team_name = team_block.text.strip()  # 提取队伍名字
            output_file.write(f"------ {team_name} ------\n")

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
                    
                    # 写入当前队伍的球员名字
                    for name in player_names:
                        output_file.write(f"{name}\n")
                
                # 移动到下一个节点
                next_node = next_node.find_next_sibling()

    print(f'内容已保存到 {output_path}')

print('所有文件处理完毕。')
