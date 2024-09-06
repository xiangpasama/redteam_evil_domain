import itertools
import sys
import os

def generate_domain_variations(domain, tlds, possible_chars):
    unique_domains = set()

    # 替换字符
    for i, char in enumerate(domain):
        for replacement in possible_chars:
            new_domain_part = domain[:i] + replacement + domain[i+1:]
            for tld in tlds:
                new_domain = f"{new_domain_part}.{tld}"
                unique_domains.add(new_domain)

    # 删除字符
    for i in range(len(domain)):
        new_domain_part = domain[:i] + domain[i+1:]
        for tld in tlds:
            new_domain = f"{new_domain_part}.{tld}"
            unique_domains.add(new_domain)

    # 插入字符的函数
    def insert_chars(base_chars, possible_chars):
        for i in range(len(base_chars) + 1):
            for char in possible_chars:
                new_domain_part = base_chars[:i] + char + base_chars[i:]
                yield new_domain_part

    # 插入字符
    for new_domain_part in insert_chars(domain, possible_chars):
        for tld in tlds:
            new_domain = f"{new_domain_part}.{tld}"
            unique_domains.add(new_domain)

    return unique_domains

# 检查是否有足够的命令行参数
if len(sys.argv) != 2:
    print("Usage: python <script_name>.py <domain>")
    sys.exit(1)

# 从命令行参数获取原始域名
original_domain = sys.argv[1]

# 分割出需要处理的部分和顶级域名(TLD)
domain_part, _ = original_domain.split('.')

# 定义所有可能的字符，0-9和a-z
possible_chars = '0123456789abcdefghijklmnopqrstuvwxyz'

# 读取后缀文件
try:
    with open('domain_suffix.txt', 'r') as file:
        tlds = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("domain_suffix.txt file not found.")
    sys.exit(1)

# 生成所有可能的域名变体
unique_domains = generate_domain_variations(domain_part, tlds, possible_chars)

# 获取当前工作目录
current_dir = os.getcwd()

# 输出所有独特的域名到文件
output_file_path = os.path.join(current_dir, 'redteam_evil_domain_plus.txt')
with open(output_file_path, 'w') as file:
    for domain in sorted(unique_domains):
        file.write(domain + '\n')

# 打印完成信息和文件路径
print(f"Generation complete. Results saved to local folder: {output_file_path}")