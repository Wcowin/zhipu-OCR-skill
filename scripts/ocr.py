#!/usr/bin/env python3
"""
使用 GLM-4V-Flash 识别图片文字
支持环境变量配置、批量识别、多种图片格式
"""

import os
import sys
import base64
import argparse
from pathlib import Path

try:
    import zhipuai
except ImportError:
    print("错误: 未安装 zhipuai 库，请运行: pip install zhipuai")
    sys.exit(1)

# 配置 API key（必须使用环境变量）
API_KEY = os.environ.get("ZHIPUAI_API_KEY")

if not API_KEY:
    print("错误: 未设置 ZHIPUAI_API_KEY 环境变量")
    print("请设置环境变量: export ZHIPUAI_API_KEY='your_api_key'")
    sys.exit(1)

# 支持的图片格式
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

def recognize_image(image_path, prompt="请识别图片中的所有文字，并完整输出", verbose=False):
    """
    识别图片中的文字

    Args:
        image_path: 图片路径
        prompt: 提示词
        verbose: 是否显示详细信息

    Returns:
        识别结果
    """
    try:
        image_path = Path(image_path)
        
        # 检查文件是否存在
        if not image_path.exists():
            return f"错误: 文件不存在 - {image_path}"
        
        # 检查文件格式
        if image_path.suffix.lower() not in SUPPORTED_FORMATS:
            return f"错误: 不支持的图片格式 - {image_path.suffix}，支持的格式: {', '.join(SUPPORTED_FORMATS)}"
        
        if verbose:
            print(f"正在识别: {image_path}")
            print(f"提示词: {prompt}")
        
        # 读取图片并转换为 base64
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        base64_data = base64.b64encode(image_data).decode('utf-8')
        
        # 调用 GLM-4V-Flash 模型
        client = zhipuai.ZhipuAI(api_key=API_KEY)
        response = client.chat.completions.create(
            model="glm-4v-flash",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_data}"
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            temperature=0.1
        )
        
        result = response.choices[0].message.content
        
        if verbose:
            print(f"识别成功: {len(result)} 字符")
        
        return result
        
    except Exception as e:
        return f"识别失败: {str(e)}"

def batch_recognize(image_paths, prompt="请识别图片中的所有文字，并完整输出", verbose=False):
    """
    批量识别多张图片

    Args:
        image_paths: 图片路径列表
        prompt: 提示词
        verbose: 是否显示详细信息

    Returns:
        识别结果字典 {图片路径: 识别结果}
    """
    results = {}
    
    for i, image_path in enumerate(image_paths, 1):
        if verbose:
            print(f"\n[{i}/{len(image_paths)}] ", end="")
        
        result = recognize_image(image_path, prompt, verbose)
        results[str(image_path)] = result
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description="使用 GLM-4V-Flash 识别图片文字",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 识别单张图片
  python3 ocr.py image.jpg
  
  # 自定义提示词
  python3 ocr.py image.jpg --prompt "请详细描述图片内容"
  
  # 批量识别
  python3 ocr.py image1.jpg image2.png image3.jpg
  
  # 使用环境变量配置 API key
  export ZHIPUAI_API_KEY="your_api_key"
  python3 ocr.py image.jpg
  
  # 显示详细信息
  python3 ocr.py image.jpg -v
        """
    )
    
    parser.add_argument('images', nargs='+', help='图片路径（支持多个）')
    parser.add_argument('prompt', nargs='?', default='请识别图片中的所有文字，并完整输出', help='提示词（可选）')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    parser.add_argument('--api-key', help='API Key（可选，优先使用环境变量）')
    
    args = parser.parse_args()
    
    # 如果提供了 API key，使用它
    if args.api_key:
        global API_KEY
        API_KEY = args.api_key
    
    # 单张图片
    if len(args.images) == 1:
        result = recognize_image(args.images[0], args.prompt, args.verbose)
        print(result)
    
    # 批量识别
    else:
        results = batch_recognize(args.images, args.prompt, args.verbose)
        
        print("\n" + "="*60)
        print("批量识别结果")
        print("="*60)
        
        for image_path, result in results.items():
            print(f"\n[图片] {image_path}")
            print(f"   {result}")

if __name__ == "__main__":
    main()
