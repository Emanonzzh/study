# 遥感监测智能助手（Remote Sensing AI Assistant）

基于 RAG + Agent 的遥感地质灾害智能问答系统，支持自然语言查询地面沉降、滑坡预警、矿山形变等监测数据。

> **线上地址**：http://47.76.101.97:8501 （Docker 部署于阿里云 ECS，Ubuntu 22.04）

## 功能

- **RAG 知识库问答**：基于 LangChain + Chroma，对遥感知识文档实现检索增强生成
- **多工具 Agent**：基于 Function Calling + LangGraph，LLM 自主决策调用监测数据查询工具
- **Web 界面**：Streamlit 网页交互，输入问题回车即答
- **RESTful API**：FastAPI 封装，支持 URL 查询并返回引用来源

## 技术栈

Python · LangChain · LangGraph · Chroma · FastAPI · Streamlit · 通义千问 qwen-plus · text-embedding-v3

## 项目结构

| 文件 | 说明 |
|------|------|
| `rag_from_scratch.py` | 手写 RAG 全链路（切片 → 向量化 → 检索 → 生成）|
| `rag_langchain.py` | LangChain 框架版 RAG |
| `agent_function_calling.py` | 手写 Function Calling 循环（理解 Agent 底层机制）|
| `agent_langgraph.py` | LangGraph `create_agent` 版多工具 Agent |
| `api_rag.py` | FastAPI 封装 RAG 的 RESTful API |
| `web_rag.py` | Streamlit 网页版 RAG 问答 |
| `web_agent.py` | Streamlit 网页版多工具 Agent |
| `知识库.txt` | RAG 使用的遥感知识文档 |
| `地质灾害防治条例.txt` | 网页版 RAG 问答使用的真实法规文档（gov.cn 来源）|
| `监测报告.txt` / `点位数据.json` | 遥感监测数据文件 |

## 快速开始

1. 安装依赖：

```
pip install openai chromadb langchain langchain-openai langchain-chroma langchain-text-splitters langgraph fastapi uvicorn streamlit
```

2. 配置 API Key：将代码中的 `YOUR_DASHSCOPE_API_KEY` 替换为你自己的阿里云百炼密钥（申请地址：https://dashscope.aliyuncs.com）

3. 运行网页版 RAG 问答：

```
streamlit run web_rag.py
```

4. 运行网页版多工具 Agent：

```
streamlit run web_agent.py
```

5. 运行 API 服务：

```
python api_rag.py
```

然后浏览器访问：`http://127.0.0.1:8001/ask?question=什么是PS-InSAR`

## 作者

遥感科学与技术背景，AI 应用开发方向求职者。目标岗位：AI 应用开发工程师。

## Docker 部署

```bash
docker build -t rs-assistant .
docker run -d -p 8501:8501 -e DASHSCOPE_API_KEY=你的密钥 --name rs-app rs-assistant
```
