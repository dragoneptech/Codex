# Qwen Chat

基于 `requests` 调用 Qwen 大模型进行对话的 Python 脚本，支持 OpenAI 兼容 API。

## 快速开始

### 1. 安装依赖

```bash
pip install requests python-dotenv
uv pip install requests python-dotenv
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件，填入以下内容：

```env
# API 密钥（必填）
API_KEY=sk-your-api-key-here

# API 端点地址（必填）
TOKEN_PLAN_URL=https://your-api-host.com/compatible-mode/v1
```