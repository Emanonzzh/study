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
- ✅ 项目 3 完整完成（真实数据遥感监测智能问答 Agent）
  - 第一步：真实法规 RAG（知识库=《地质灾害防治条例》）
  - 第二步：SQLite 数据库（monitoring.db 存 3 条国家数据中心真实元数据）
  - 第三步：day21.py 整合成品（一个 Agent 两工具：query_regulation 向量查条例 + query_dataset SQL 查数据集）
  - 踩坑记录：① embedding 必带 chunk_size=10（阿里云每批最多10条）② SQL LIKE 是连续子串匹配 ③ conn.close 必须在函数内 return 前 ④ 真实 API key 禁止硬编码 push（泄漏过一次，已吊销；代码用环境变量 DASHSCOPE_API_KEY）
- ✅ 部署上线：Docker 容器化部署于阿里云 ECS（Ubuntu 22.04，公网 IP 47.76.101.97），Streamlit 服务跑在 8501 端口，**公网可访问：http://47.76.101.97:8501**
  - 服务器操作：SSH 登录（root 用户）、git clone 拉项目、docker build/run、安全组已开 22 和 8501
  - Linux 基础已学：核心命令/权限/文件系统（见 Linux学习笔记.md）
- ⏭️ 下一阶段（2026-09 秋招冲刺）：
  1. **项目反刍**：关掉所有资料，从空白文件重搭 day21 骨架（练独立开发能力，允许查资料）
  2. 写简历（1 主打项目 + 2 支撑项目 + GitHub + 公网地址）
  3. 投递 AI 应用开发 / 大模型应用 / AI Agent 岗
- 每日基础练习：practice_day1（列表循环/if边界/字典查询）✅、practice_two_sum ✅（持续进行）

## 环境
- Python：用完整路径运行（每台电脑路径不同，以 `python --version` 验证）
- 已装库：openai、chromadb、langchain、langchain-openai、langchain-chroma、langchain-text-splitters、langgraph、fastapi、uvicorn、streamlit
- 大模型：阿里云百炼（dashscope），LLM 用 qwen-plus，Embedding 用 text-embedding-v3
- API key：禁止硬编码上传 GitHub；代码统一用环境变量 DASHSCOPE_API_KEY 读取（os.getenv），本地跑前先 `$env:DASHSCOPE_API_KEY = "xxx"`
- 坑：langchain 新版连阿里云 embedding 必须加 check_embedding_ctx_length=False

## 教学要求（重要，务必遵守）
1. 从零自写：给题目和思路，不给完整代码（新 API 首次可给完整示例讲解）
2. 代码：英文变量名 + 中文注释
3. 项目驱动、先跑起来再讲原理；能用遥感数据练习就用
4. 给具体指令，不给选择题；直接帮用户做决定
5. 多复习，不假设已会；中文交流；鼓励但诚实
6. 每天给 2-3 道 Python 基础小题（遥感场景包装），锻炼基础编程能力
7. 已知的坑：用户会忘 Ctrl+S；相对路径是相对当前工作目录；Windows 路径加 r 前缀；Chroma 集合名不能中文；Streamlit 必须用 streamlit run 运行

## 每日学习计划（每天 1 小时，照做）
- 前 15 分钟：2 道 Python 基础小题（手写循环/字典/切片，遥感场景包装，专治"手生"）
- 中间 30 分钟：项目 V2 升级（按 V2升级任务拆解.md 一步步做）
- 后 15 分钟：面试题扫盲 1-2 道（按 面试题扫盲清单.md）
- 原则：不贪新知识，把会的东西练到不手生（用户缺口是手误，不是概念）
