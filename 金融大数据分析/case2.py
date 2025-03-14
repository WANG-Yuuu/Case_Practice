# Case 2：统计金融新闻中的关键词频率
news ="今日股市大幅上涨，债券市场表现平稳，黄金价格小幅下跌。股市的上涨主要得益于经济数据的改善。"
keywords = ["股市", "债券", "黄金", "上涨", "下跌"]

keyword_num = {}
for keyword in keywords:
    count = news.count(keyword)
    keyword_num[keyword] = count
print(keyword_num)

