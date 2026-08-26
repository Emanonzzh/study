# Day 12：Agent —— 让 LLM 自己决定调工具
import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from openai import OpenAI

api_key = "YOUR_DASHSCOPE_API_KEY"
client = OpenAI(api_key=api_key, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

# ① 工具清单：这是给 LLM 看的"说明书"，告诉它有哪些工具能用
tools = [{
    "type": "function",
    "function": {
        "name": "get_subsidence",
        "description": "查询某个城市的地面沉降速率，单位毫米/年",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名，例如 北京、上海"}
            },
            "required": ["city"]
        }
    }
},
{
    "type": "function",
    "function": {
        "name": "get_landslide",
        "description": "查询某个地区的滑坡预警",
        "parameters": {
            "type": "object",
            "properties": {
                "region": {"type": "string", "description": "地区，例如 四川山区、云南河谷"}
            },
            "required": ["region"]
        }
    }
}]



# ② 真正的工具函数：LLM 不执行它，是你的代码执行
def get_subsidence(city):
    db = {"北京": 45.2, "上海": 30.8, "广州": 12.5}
    return db.get(city, "未知城市")


def get_landslide(region):
    db = {"四川山区": "橙色预警", "云南河谷": "黄色预警", "贵州": "蓝色预警"}
    return db.get(region, "未知地区")

# ③ 第一轮：问题 + 工具清单发给 LLM
question = input("你：")
messages = [{"role": "user", "content": question}]
resp = client.chat.completions.create(model="qwen-plus", messages=messages, tools=tools)
msg = resp.choices[0].message

# ④ 如果 LLM 说"要调工具"，就执行工具
if msg.tool_calls:
    tc = msg.tool_calls[0]                      # 取出第一个工具调用
    args = json.loads(tc.function.arguments)    # LLM 给的参数是字符串，转成字典


    if tc.function.name == "get_subsidence":
        result = get_subsidence(**args)
    elif tc.function.name == "get_landslide":
        result = get_landslide(**args)
    # 把"我要调工具"+"工具返回的结果"都回传给 LLM（这两行是固定格式，先照抄）
    messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": [{"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}}]})
    messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})

    # ⑤ 第二轮：LLM 根据结果生成最终答案
    resp2 = client.chat.completions.create(model="qwen-plus", messages=messages, tools=tools)
    print("AI：", resp2.choices[0].message.content)
else:
    print("AI：", msg.content)   # LLM 觉得不用工具，直接答