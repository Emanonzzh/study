import streamlit as st
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

api_key = "YOUR_DASHSCOPE_API_KEY"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

llm = ChatOpenAI(model="qwen-plus", api_key=api_key, base_url=base_url)

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

agent = create_agent(llm, [get_subsidence, get_landslide, get_mine_name_deformation])

st.title("遥感监测智能助手")
st.write("可以查询地面沉降、滑坡预警、矿山形变数据")

with st.form("qa_form"):
    question = st.text_input("你的问题：", placeholder="例如：上海的地面沉降速率？")
    submitted = st.form_submit_button("提问")

if submitted and question:
    result = agent.invoke({"messages": [("user", question)]})

    st.markdown("### 回答")
    st.write(result["messages"][-1].content)

