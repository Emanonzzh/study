# 学习者情况（每次会话必读）

## 最近一次会话（2026-09-09 夜 · 本机 AI 已记录，先看这节）

### 本次推送了什么（GitHub，均已 pull 到即可用）
- `4452f9c` fix：day21.py 的 `risk_assessment` docstring 加**触发边界**——只在用户问"某区域形变风险/等级/是否需防范"时调用；概念题（什么是 InSAR/PS-InSAR/SBAS）、数据集查询、法规问答不得误调。**本地已编译通过**
- `112a560` docs：README 首屏加了 mermaid 架构图 + ✨亮点 + 4 条"核心面试技术点"；**新增 `deploy.sh`**（服务器一条命令部署，自动从旧容器恢复 `DASHSCOPE_API_KEY`）
- 今天更早：`e5fbe17` 面试题库入库 / `cda4676` V2-A3/A4 完成 / `5a39ef9` 每日练习

### 求职分析结论（重要，白天参考）
- **身份定性**：26 届已毕业 → 2026.9 秋招面向 27 届**不适用**，走**社招/往届通道**；目标城市深圳、行业不限
- **双轨**：主攻 AI 应用开发（遥感+AI 差异化，简历=上线项目+毕设）；GIS 内业仅作保底（两版简历分开投）
- 可行性结论：项目够格当敲门砖；真正卡点=无工作经验+非科班+算法白板，靠"公网 Demo + 投递量 + 面试准备"补

### 求职材料产出（在**本机** `C:\Users\123\Desktop\WORK\`，不在仓库，白天需要的话拷过去）
- `钟英浩_AI应用开发_简历_深圳版.md`：AI 应用岗简历（主打 day21 三工具 Agent + 毕设=项目二）
- `求职打招呼话术.md`：BOSS 直聘 3 版话术 + 投递节奏
- 毕设（云贵高原湖泊 2013-2022 动态分析）已整理成"简历可讲 + 面试衔接话术"，见简历文件

### ⏳ 待办（白天，按序）
1. **服务器部署新版**：登录 ECS `root@47.76.101.97` → 进项目目录 → `git pull` → `bash deploy.sh`（deploy.sh 会自动取回 API Key、重建、重启、健康检查；找不到目录用 `find / -maxdepth 4 -name day21.py`）
2. **README 补演示截图**：占位注释已在 README "🖼 演示截图"处
3. **开始投递**：按话术每天 30-50 家（AI 应用 / 遥感+AI / GIS 内业保底轮流），回复后发 简历PDF + Demo + GitHub
4. **学习主线**（1 小时/天）：每日基础小题 2-3 道 → **V2 阶段 C（RAG 评估，面试性价比最高，做完简历加"检索命中率对比实验"）** → 面试扫盲 1-7/9 → 有余力再推 V2-B/D

---

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
  1. ✅ **项目反刍完成**（2026-09-04，day21remake.py 从空白重搭，3 轮 bug 修复 + 全文逐行讲解，教学要点：独立 if 打分 vs if/elif 分级）
  2. ⏳ **V2 阶段 A 进行中**：
     - A1 ✅ day22_seed_data.py（monitoring_series 表 + 18 条川西示范区示例数据，幂等验证过；UPDATE 练习做完后已把练习代码从脚本删除并复位数据）
     - A2 ✅ day23_risk.py risk_assessment 完成（规则打分：速率+40/加速+30/异常+30；分级 ≤30低/≤60中/>60较高；验收 100 分三项全中，空数据返回"数据不足"）
     - A3 ✅ risk_assessment 已集成进 day21.py（@tool+docstring+create_agent 三工具），验收三问全过：法规等级→query_regulation、青藏数据集→query_dataset、川西风险→risk_assessment(100分/较高风险)
     - A4 ✅ 结构化报告+免责声明已生效（prompt 注入 user_message，分节输出+末尾免责声明）
      - ⚠️ 待办：① risk_assessment docstring 边界模糊导致概念题误调用（问"什么是SBAS-InSAR"被调了风险评估），需改成"用户询问某区域形变风险等级时调用，不要用于数据集查询或概念解释" ② 青藏数据集回答中出现元数据里没有的速率数字=幻觉案例，已存档当面试素材 ③ 服务器重新部署（docker）未做
   3. ⏭️ **V2 阶段 C（RAG 评估）**（2026-09-10 完成）：
      - C1 ✅ rag_eval_questions.py：12 题测试集（问题+期望命中关键词），全部校验：关键词在原文出现≥1次且有辨识度（修正"发展趋向预测→发展趋势预测"、"危险性评估"22次无区分度改选"可行性研究阶段"）
      - C2 ✅ rag_eval.py：评估脚本（建库→检索→关键词命中判断→计数）
      - C3 ✅ 四组实验：chunk_size∈{100,400}×k∈{2,4}，结果 10/12、11/12、10/12、**12/12**，最优 400+4（100 命中率 83%）
      - 结论（面试可讲版）：小切片造成语义碎片，适度加大切片+提高 k 显著提升命中率；但 k 越大 token 越贵、噪音越多，k 是"最小够用"权衡，评测价值=用数据找最小够用参数
      - C4 ✅ 最优参数已落地 day21.py（400/k=4），验证通过；⚠️ 注意：splitter 的 chunk_size 与 embedding 的 chunk_size=10 是两回事（后者是每批条数）
      - 实验中学习者踩坑：build_store 参数未接收（TypeError）、f-string 变量写在引号外（SyntaxError）、`if hits in material` 选错变量、没导入 st 却用装饰器、F:\Python3.14 反复误用——全部独立修复或当场纠正
   4. 写简历（1 主打项目 + 2 支撑项目 + GitHub + 公网地址）；**C 完成可加一句："构建法规问答测试集，对比切片策略与检索参数（chunk_size/k 四组实验），检索命中率 83%→100%"**
   5. 投递 AI 应用开发 / 大模型应用 / AI Agent 岗
     - 今日新踩坑：脚本必须先 cd 到仓库目录再跑（monitoring.db 曾被建进 F:\VScode 目录）；AUTOINCREMENT 永不复用 ID，删了重插 ID 会跳；UPDATE 定位要用业务字段（date）而非 id；cursor.rowcount 检查影响行数防静默失败
  3. 写简历（1 主打项目 + 2 支撑项目 + GitHub + 公网地址）
  4. 投递 AI 应用开发 / 大模型应用 / AI Agent 岗
- 每日基础练习：practice_day1（列表循环/if边界/字典查询）✅、practice_two_sum ✅（持续进行）

## 面试扫盲资料（已入库）
- `面试题库_AI_Interview/`：GitHub 开源题库（kingaimaster/AI_Interview，200+ 题，已拷入仓库）
- **只学 4 个目录**：`0.AI应用开发工程师`、`1.Python`、`5.Agent`（LangChain/LangGraph/MCP）、`8.HR初筛`
- **跳过**：PyTorch/Transformer/多模态（校招 AI 应用岗考得浅，秋招后再说）
- 用法：每天 15 分钟扫 1-2 题，只读"参考口语化回答"，结合自己的 day21 项目举一反三
- 高频必考补充：MCP vs Function Calling 区别（FC=模型侧调用机制，MCP=应用侧工具接入协议/治理层；见 `5.Agent/MCP/A.md` Q2）

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
