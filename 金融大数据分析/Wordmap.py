import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#读取文本
text_path ='/Users/Zhuanz/Desktop/Case_Practice/金融大数据分析/报告.txt'
with open(text_path,'r',encoding='utf-8')as f:
    text = f.read()

# 中文分词
words =jieba.lcut(text)

#去除停用词
stopwords = set(['我们','的','了', '和','在','是','也','对','有','造','中','气','将']) # 可自行扩展
filtered_words = [word for word in words if word not in stopwords and len(word) >1 ]
text_filtered =" ".join(filtered_words)
# 设置字体路径
font_path ="/System/Library/Fonts/STHeiti Medium.ttc" # Mac
# Windows 示例:"C:llWindowsllFontsllsimhei.ttf"
#加载 logo 图像作为 mask(需是黑白图或透明 PNG)
mask_image = np.array(Image.open('/Users/Zhuanz/Desktop/Case_Practice/金融大数据分析/圆形.png')) # <-- 换成你的
#生成词云图
wc = WordCloud(
    font_path=font_path,
    width=400,
    height=200,
    background_color='white',
    max_words=70,
    mask=mask_image,
    colormap='rainbow'
).generate(text_filtered)     # colormap:Set2,tab10,cool,autumn,Blues,Greens,rainbow,dark2,viridis

#显示图像
plt.figure(figsize=(10,8))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.title("Analysis",fontsize=16)
plt.show()