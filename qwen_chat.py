import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
TOKEN_PLAN_URL = os.getenv("TOKEN_PLAN_URL")

if not API_KEY:
    raise ValueError("请在 .env 文件中设置 API_KEY")
if not TOKEN_PLAN_URL:
    raise ValueError("请在 .env 文件中设置 TOKEN_PLAN_URL")

# 如果 URL 不以 /chat/completions 结尾，自动追加
if not TOKEN_PLAN_URL.rstrip("/").endswith("/chat/completions"):
    TOKEN_PLAN_URL = TOKEN_PLAN_URL.rstrip("/") + "/chat/completions"

MODEL = "qwen3.7-max"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好！你能做什么？"},
    # {"role": "user", "content": "你好！请用一句话介绍一下你自己。"},
]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": MODEL,
    "messages": messages,
}

print(f"请求URL: {TOKEN_PLAN_URL}")
print(f"请求体: {json.dumps(payload, ensure_ascii=False, indent=2)}")
print()

response = requests.post(
    TOKEN_PLAN_URL,
    headers=headers,
    json=payload,
    timeout=60,
    # proxies={"http": None, "https": None},
)

print(f"HTTP 状态码: {response.status_code}")
try:
    resp_json = response.json()
    print(f"响应体: {json.dumps(resp_json, ensure_ascii=False, indent=2)}")
except Exception:
    print(f"响应体(文本): {response.text}")

response.raise_for_status()

reply = resp_json["choices"][0]["message"]["content"]
print(f"\nQwen 回复:\n{reply}")
