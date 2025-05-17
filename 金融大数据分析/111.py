import json
import base64
from PIL import Image
import io
import numpy as np # 假设需要处理掩码

data_string = """
[
  {"box_2d": [120, 289, 193, 496], "mask": "data:image/png;base64,...(省略)...", "label": "显微镜"},
  {"box_2d": [894, 174, 957, 578], "mask": "data:image/png;base64,...(省略)...", "label": "实验装置示意图"},
  {"box_2d": [427, 253, 484, 518], "mask": "data:image/png;base64,...(省略)...", "label": "半透半反镜"},
  {"box_2d": [709, 96, 770, 382], "mask": "data:image/png;base64,...(省略)...", "label": "牛顿环装置"},
  {"box_2d": [471, 100, 526, 212], "mask": "data:image/png;base64,...(省略)...", "label": "钠灯"}
]
""" # 注意: mask 内容被省略了

# 1. 解析 JSON
parsed_data = json.loads(data_string)

# 2. 处理第一个对象 (显微镜)
microscope_data = parsed_data[0]
label = microscope_data['label']
box = microscope_data['box_2d']

# 3. 解码 Mask
mask_uri = microscope_data['mask']
# 分离出 Base64 部分
header, encoded_data = mask_uri.split(',', 1)
# 解码 Base64
decoded_data = base64.b64decode(encoded_data)
# 将解码后的二进制数据加载为图像对象 (例如使用 PIL/Pillow)
mask_image = Image.open(io.BytesIO(decoded_data))

# 4. 后续操作 (例如显示信息或处理图像)
print(f"找到物体: {label}")
print(f"边界框: {box}")
# mask_image.show() # 可以显示解码后的掩码图像
# 可以在这里添加代码，将 mask_image 应用到原始图像上