# Day 13：用 LangGraph 一行搞定 Agent（75 行 → 30 行）
import sys
sys.stdout.reconfigure(encoding="utf-8")

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

api_key = "YOUR_DASHSCOPE_API_KEY"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

llm = ChatOpenAI(model="qwen-plus", api_key=api_key, base_url=base_url)

# ① 用 @tool 定义工具（比 Day 12 的 JSON 清单简洁太多）
@tool
def get_subsidence(city: str) -> str:
    """查询某个城市的地面沉降速率，单位毫米/年。"""
    db = {"北京": 45.2, "上海": 30.8, "广州": 12.5}
    return str(db.get(city, "未知城市"))

@tool
def get_landslide(region: str) -> str:
    """查询某个地区的滑坡预警等级。"""
    db = {"四川山区": "橙色预警", "云南河谷": "黄色预警", "贵州": "蓝色预警"}
    return str(db.get(region, "未知地区"))

@tool
def get_mine_name_deformation(mine_name:str) -> str:
    """查询某个矿山的形变程度。mine_name 是矿山名称，例如"新疆矿山"、"陕西矿山"。"""
    db = {"新疆矿山":"形变严重","陕西矿山": "形变中等" , "山西矿山": "形变轻微"}
    return str(db.get(mine_name,"未知矿山"))

# ② 一行创建 Agent：整个"判断→调用→执行→回传→生成"全自动
agent = create_agent(llm, [get_subsidence, get_landslide, get_mine_name_deformation])

# ③ 交互式提问
while True:
    question = input("\n你：")
    if question == "quit":
        print("再见！")
        break
    result = agent.invoke({"messages": [("user", question)]})
    print("AI：", result["messages"][-1].content)