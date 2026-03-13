# -*- coding: utf-8 -*-
"""
福库心理APP图标生成器
直接生成各种尺寸的PNG图标
"""

import os
from PIL import Image, ImageDraw

# 确保icons文件夹存在
icons_dir = 'icons'
if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)
    print(f"✅ 创建了 {icons_dir} 文件夹")

# 需要生成的图标尺寸
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    # 创建图像
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    # 创建绘图对象
    draw = ImageDraw.Draw(img)

    # 绘制圆形背景（渐变效果用多层圆）
    center = size // 2
    radius = int(size * 0.47)

    # 外圈渐变（绿色到蓝色）
    for i in range(15):
        alpha = max(50, 255 - i * 10)
        color = (0, 200, 83, alpha) if i < 8 else (33, 150, 243, alpha)
        current_radius = max(10, radius - i * 3)
        draw.ellipse([center - current_radius, center - current_radius,
                     center + current_radius, center + current_radius],
                    fill=color)

    # 绘制白色叶子形状
    leaf_scale = size / 512 * 0.8
    cx, cy = center, center

    # 主叶子
    points1 = [
        (cx, cy - 180 * leaf_scale),
        (cx + 40 * leaf_scale, cy - 120 * leaf_scale),
        (cx, cy - 60 * leaf_scale),
        (cx - 40 * leaf_scale, cy - 120 * leaf_scale)
    ]
    draw.polygon(points1, fill=(255, 255, 255, 242))

    # 左侧叶子
    points2 = [
        (cx, cy - 40 * leaf_scale),
        (cx - 60 * leaf_scale, cy),
        (cx - 90 * leaf_scale, cy + 40 * leaf_scale),
        (cx - 60 * leaf_scale, cy - 20 * leaf_scale)
    ]
    draw.polygon(points2, fill=(255, 255, 255, 217))

    # 右侧叶子
    points3 = [
        (cx, cy - 40 * leaf_scale),
        (cx + 60 * leaf_scale, cy),
        (cx + 90 * leaf_scale, cy + 40 * leaf_scale),
        (cx + 60 * leaf_scale, cy - 20 * leaf_scale)
    ]
    draw.polygon(points3, fill=(255, 255, 255, 217))

    # 底部叶子
    points4 = [
        (cx, cy + 20 * leaf_scale),
        (cx + 30 * leaf_scale, cy + 80 * leaf_scale),
        (cx, cy + 140 * leaf_scale),
        (cx - 30 * leaf_scale, cy + 80 * leaf_scale)
    ]
    draw.polygon(points4, fill=(255, 255, 255, 217))

    # 外围光晕圆环
    halo_radius = int(size * 0.43)
    draw.ellipse([center - halo_radius, center - halo_radius,
                 center + halo_radius, center + halo_radius],
                outline=(255, 255, 255, 51), width=3)

    # 保存图像
    filename = f'icon-{size}x{size}.png'
    filepath = os.path.join(icons_dir, filename)
    img.save(filepath, 'PNG')
    print(f"✅ 生成: {filename}")

print(f"\n🎉 所有图标已生成到 {icons_dir} 文件夹！")
print(f"📱 共生成 {len(sizes)} 个图标")
