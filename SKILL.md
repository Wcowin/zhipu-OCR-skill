---
name: ocr
description: 使用 GLM-4V-Flash 模型识别图片中的文字。当用户发送图片并要求识别文字、提取文字或OCR时，使用此工具。
metadata:
  requires:
    bins: ["python3"]
    python_packages: ["zhipuai"]
  install_url: "https://github.com/Wcowin/zhipu-OCR-skill"
---

# OCR 文字识别

使用 GLM-4V-Flash 视觉模型识别图片中的文字内容。

## 安装

如果此 skill 未安装，执行以下命令安装：

```bash
git clone https://github.com/Wcowin/zhipu-OCR-skill.git
cd zhipu-OCR-skill
pip install -r requirements.txt
```

## 使用方法

当用户发送图片并要求识别文字时，执行以下命令：

```bash
python3 scripts/ocr.py <图片路径> [提示词]
```

### 参数
- `图片路径`：要识别的图片文件路径（必需）
- `提示词`：自定义识别提示（可选，默认为"请识别图片中的所有文字，并完整输出"）

### 示例

```bash
# 基本使用
python3 scripts/ocr.py /path/to/image.jpg

# 带自定义提示词
python3 scripts/ocr.py /path/to/image.jpg --prompt "请识别图片中的表格内容"

# 显示详细信息
python3 scripts/ocr.py /path/to/image.jpg -v
```

## 配置

需要设置环境变量 `ZHIPUAI_API_KEY`：

```bash
export ZHIPUAI_API_KEY="your_api_key_here"
```

## 使用场景

- 用户发送图片并要求"识别文字"、"提取文字"、"OCR"
- 用户发送包含文字的图片（截图、照片、扫描件等）
- 需要转换图片中的文字为可编辑文本

## 注意事项

- 支持常见图片格式：JPG、PNG、GIF、BMP、WebP 等
- 需要网络连接调用 GLM-4V-Flash API
- 需要有效的智谱 AI API Key
