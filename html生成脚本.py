import json
import os

# 设置生成详情页的文件夹
output_dir = "product_pages"
os.makedirs(output_dir, exist_ok=True)

# 读取产品 JSON 数据
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# 遍历每个产品生成 HTML
for p in products:
    # 生成 HTML 内容
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['name']} - Analogue Keeper</title>
<style>
  body {{ font-family: Arial, sans-serif; background:#fff; margin:0; padding:0; }}

  /* 顶部返回按钮 */
  .back-btn {{
      display:inline-block;
      margin:20px;
      text-decoration:none;
      color:#333;
      font-weight:bold;
  }}

  /* 上半部分容器，图片+信息 */
  .product-detail {{
      display:flex;
      gap:40px;
      padding:20px;
      flex-wrap: wrap;
      background-color:#fff;

      max-width:900px;       /* 最大宽度 */
      margin:0 auto;         /* 水平居中整个容器 */
      align-items:center;     /* 图片和文字垂直居中 */
      justify-content:center; /* 图片+文字水平居中 */
  }}

  /* 左侧主图 */
  .main-img {{
      width:350px;           /* 可调整主图大小 */
      height:350px;
      object-fit:cover;
      flex-shrink:0;
      user-drag:none;
      -webkit-user-drag:none;
      -moz-user-drag:none;
      -o-user-drag:none;
      -ms-user-drag:none;
  }}

  /* 右侧信息 */
  .product-info {{
      flex:1;
      max-width:400px;       /* 右侧信息最大宽度 */
      display:flex;
      flex-direction:column;
      justify-content:center; /* 垂直居中信息 */
  }}

  .product-info h2 {{ margin-bottom:10px; }}
  .product-info p {{ margin:5px 0; }}

  /* 下面详情图片容器 */
  .detail-images {{
      display:flex;
      flex-wrap:wrap;
      gap:10px;
      max-width:900px;
      margin:20px auto;
  }}
  .detail-images img {{
      width:200px;
      height:200px;
      object-fit:cover;
  }}
</style>
</head>
<body>

<a class="back-btn" href="../analogue.html">&larr; 返回主页</a>

<div class="product-detail">
    <!-- 左侧主图 -->
    <img class="main-img" src="../{p['img']}" alt="{p['name']}">

    <!-- 右侧信息 -->
    <div class="product-info">
        <h2>{p['name']}</h2>
        <p><strong>原价：</strong>￥{p['original_price']}</p>
        <p><strong>发售渠道：</strong>{p.get('tags', '')}</p>
        <p><strong>发售日期：</strong>{p.get('release_date', '')}</p>
        <p><strong>尺寸：</strong>{p.get('size', '')}</p>
        <p><strong>产品背景：</strong>{p.get('background', '')}</p>
    </div>
</div>

<!-- 下面的其他详情图 -->
<div class="detail-images">
"""
    # 添加其他详情图
    for img_path in p.get("other_images", []):
        html_content += f'    <img src="../{img_path}" alt="{p["name"]}">\n'

    html_content += """
</div>
</body>
</html>"""

    # 写入 HTML 文件
    filename = os.path.join(output_dir, f"product-{p['id']}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

print("所有详情页生成完成！")
