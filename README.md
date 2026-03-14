# Zhipu OCR Skill

基于 GLM-4V-Flash 模型的图片文字识别工具，支持命令行和 Agent Skill 两种使用方式。

## 特性

- 使用 GLM-4V-Flash 视觉模型，识别准确率高
- 支持多种图片格式：JPG、PNG、GIF、BMP、WebP
- 支持自定义提示词，灵活应对各种场景
- 支持批量识别多张图片
- 可作为 Agent Skill 使用
- 支持环境变量配置 API Key

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/Wcowin/zhipu-OCR-skill.git
cd zhipu-OCR-skill
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

```bash
# 方式1：环境变量（推荐）
export ZHIPUAI_API_KEY="your_api_key_here"

# 方式2：创建 .env 文件
cp .env.example .env
# 编辑 .env 文件，填入你的 API Key
```

> 获取 API Key：[智谱 AI 开放平台](https://open.bigmodel.cn/)

## 使用方法

### 命令行使用

```bash
# 基本使用
python3 scripts/ocr.py image.jpg

# 自定义提示词
python3 scripts/ocr.py image.jpg "请识别图片中的所有文字"

# 批量识别
python3 scripts/ocr.py image1.jpg image2.png image3.jpg

# 显示详细信息
python3 scripts/ocr.py image.jpg -v
```

### 作为模块导入

```python
from scripts.ocr import recognize_image, batch_recognize

# 单张识别
result = recognize_image("image.jpg")
print(result)

# 批量识别
results = batch_recognize(["img1.jpg", "img2.png"])
for path, text in results.items():
    print(f"{path}: {text}")
```

### 作为 Agent Skill 使用

#### 方式一：AI 自动安装（推荐）

直接复制以下 prompt 发送给 AI：

```
请帮我安装 ocr skill，从 https://github.com/Wcowin/zhipu-OCR-skill 克隆到本地的 skills 目录，然后安装依赖。
```

AI 会自动执行：
```bash
git clone https://github.com/Wcowin/zhipu-OCR-skill.git
cd zhipu-OCR-skill
pip install -r requirements.txt
```

#### 方式二：手动安装

```bash
git clone https://github.com/Wcowin/zhipu-OCR-skill.git
cd zhipu-OCR-skill
pip install -r requirements.txt
```

#### 使用方法

安装完成后，发送图片并说"识别文字"即可。

## 使用场景

- 文档扫描件文字提取
- 截图文字识别
- 照片中的文字提取
- 表格内容识别
- 手写文字识别

## 配置说明

| 环境变量 | 说明 | 默认值 |
|---------|------|--------|
| `ZHIPUAI_API_KEY` | 智谱 AI API Key | 无（必填） |

## 依赖

- Python 3.8+
- zhipuai >= 2.0.0

## 开源协议

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 致谢

- [智谱 AI](https://open.bigmodel.cn/) 提供 GLM-4V-Flash 模型
