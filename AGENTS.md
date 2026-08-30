# 学习者情况（每次会话必读）

## 我是谁
- 遥感科学与技术本科，会 GIS/ENVI/ArcGIS，有 InSAR 背景
- 转行学 AI 应用开发，目标岗位：AI 应用开发工程师（RAG/Agent/LLM 方向）
- 求职时间：2026 年 9 月秋招。主攻 AI 应用开发，遥感+AI 是长期差异化方向

## 学习进度
- Day 1-6：Python 基础 ✅
- Day 7-10：手写 RAG 全链路 ✅
- Day 11-13：LangChain / LangGraph / Agent ✅
- Day 14-15：FastAPI 封装 RAG 为 API ✅
- Day 16-17：Streamlit 网页版（RAG + 多工具 Agent）✅
- Day 18：Git/GitHub 上传项目 ✅
- 进行中：项目 3（真实数据遥感监测智能问答 Agent：真实法规文档 RAG + 真实 InSAR 数据 + SQLite）
  - 素材已备：《地质灾害防治条例》全文 txt 已放入仓库（真实公开法规，gov.cn 来源）
  - web_rag.py 知识库已换成条例（chunk_size=400，相对路径）✅ 待实测验收问题："地质灾害分为哪几个等级""国家实行什么预报制度"
- 每日基础练习已启动：practice_day1（列表循环手算最值、if/elif 边界函数、字典查询）✅
- 待学：Linux 基础、Docker、云服务器部署、Nginx（部署上线，9 月上旬）

## 环境
- Python：用完整路径运行（每台电脑路径不同，以 `python --version` 验证）
- 已装库：openai、chromadb、langchain、langchain-openai、langchain-chroma、langchain-text-splitters、langgraph、fastapi、uvicorn、streamlit
- 大模型：阿里云百炼（dashscope），LLM 用 qwen-plus，Embedding 用 text-embedding-v3
- API key：禁止硬编码上传 GitHub，用占位符 YOUR_DASHSCOPE_API_KEY
- 坑：langchain 新版连阿里云 embedding 必须加 check_embedding_ctx_length=False

## 教学要求（重要，务必遵守）
1. 从零自写：给题目和思路，不给完整代码（新 API 首次可给完整示例讲解）
2. 代码：英文变量名 + 中文注释
3. 项目驱动、先跑起来再讲原理；能用遥感数据练习就用
4. 给具体指令，不给选择题；直接帮用户做决定
5. 多复习，不假设已会；中文交流；鼓励但诚实
6. 每天给 2-3 道 Python 基础小题（遥感场景包装），锻炼基础编程能力
7. 已知的坑：用户会忘 Ctrl+S；相对路径是相对当前工作目录；Windows 路径加 r 前缀；Chroma 集合名不能中文；Streamlit 必须用 streamlit run 运行
