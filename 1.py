import requests

# 设置请求的URL和查询语句
url = 'https://dune.com/sixdegree/eths-query'
query = '''
select 
    block_time
    , from_utf8(data) as decode_data
    , "from" as creator
    , to as owner
    , hash
from ethereum.transactions 
where value = 0
    and block_time > timestamp '2023-06-10'
    and bytearray_starts_with(data, 0x646174613a)
order by block_time desc
'''

# 发起POST请求并获取结果
response = requests.post(url, data=query)

# 保存为txt文件
filename = 'query_result.txt'
with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.text)

print('查询结果已保存为', filename)
