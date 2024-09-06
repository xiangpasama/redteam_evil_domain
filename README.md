# redteam_evil_domain
用于生成变体域名供红队或钓鱼演练使用。

```
程序思路，google.com为例

1-google中的单个字符依次被0-9a-z所替代，有216次变形

2-google的左右以及字符空隙依次添加0-9a-z，有252次变形

3-google中的单个字符依次被去掉，有6次变形

4-1/2/3的变形域名后添加常见的域名后缀，替换.com【redteam_evil_domain_plus.py专属】

```

# 使用方法

```
纯python3.11版本环境下编写

pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

redteam_evil_domain.py变体较少，数百到数千

python redteam_evil_domain.py google.com

redteam_evil_domain_plus.py变体较多，数万到数十万

python redteam_evil_domain_plus.py google.com

```
