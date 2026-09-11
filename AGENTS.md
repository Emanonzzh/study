# 学习者情况（每次会话必读）

## 最近一次会话（2026-09-10 夜 · 先看这节）

### 本次推送（GitHub，pull 即可用）
- `b1071f1` **V2-C 完成：RAG 评估** —— `rag_eval_questions.py`（12 题测试集）+ `rag_eval.py`（评估脚本）+ 四组实验（chunk_size 100/400 × k 2/4）：命中 10/12、11/12、10/12、**12/12**，最优 **400/k=4** 已落地 `day21.py`
- `ed0193d` 每日练习：`my_max` 擂台模式 + `average_step` 相邻增量（阶段 B 零件）
- 更早：`4452f9c` risk_assessment docstring 触发边界已修 / `112a560` README 架构图+deploy.sh / `fd91eb7` 交接更新

### 求职材料（在**本机** `C:\Users\123\Desktop\WORK\`，不在仓库，另一台电脑要用请拷）
- `钟英浩_AI应用开发_简历_深圳版.md` —— 已加入 V2-C 成果（**检索命中率 83%→100%**）
- `求职打招呼话术.md`（BOSS 3 版）、`深圳投递公司清单.md`（含初级检索法与筛选）
- `4周计划_手写基础与求职并行.md`（**手写代码是当前最大短板**，按此计划每天练）
- `项目口述稿_遥感监测智能助手.md` —— 面试口述稿（1 分钟版/3 分钟版/追问 Q&A/踩坑故事/证据索引）；**仓库内同步版：`docs/项目口述稿.md`**（2026-09-11 已按 A5 部署完成 + V2-B 进展同步更新：线上已是最新三工具版；第四个工具 `deformation_analysis` 标注为"待集成"）

### 📌 文档同步规则（每轮会话必须遵守）
项目每有一次新进展（新增工具/评测结果/部署变更/功能改动），**必须同步更新三处**，否则面试时会前后矛盾：
1. `AGENTS.md`（本文件）—— 进度 + 待办
2. **简历** `WORK\钟英浩_AI应用开发_简历_深圳版.md` —— 数字、功能描述要和新进展一致
3. **项目口述稿** `docs/项目口述稿.md`（仓库内，便于两台电脑同步）—— 新增功能要补进"三个工具/架构/评测/踩坑/Q&A"对应小节；本机 `WORK\项目口述稿_遥感监测智能助手.md` 保持同版本

### 求职结论（2026-09-12 更新：转向开发）
- **目标岗位改为两个**：① **Agent 开发工程师（初级/社招往届）** ② **AI 运维 / AI 应用部署运维（初级）**；遥感/GIS 内业降为**兜底**
- 身份：26 届已毕业 → 社招/往届通道；目标城市深圳（简历另有"广东东莞"住址说法，待本人统一）
- **不新开项目**：把现有项目升级成工程化项目（CRUD + 日志留痕 + health + docker compose + GitHub Actions + 监控 + pytest），同时喂饱两个岗位
- 6 周计划（每天 2h：手写 30min / 主线 60min / 读代码 20min / 笔记 10min）：
  本机 `WORK\开发转型计划_Agent开发与AI运维_6周.md`
- **硬短板优先级**：① 手写 Python（面试手写不过=淘汰） ② CRUD/后端 ③ code review ④ 运维（Docker compose/CI-CD/监控）
- ⚠️ 诚实红线：简历里"OBIA 92.3%""YOLOv8-OBB mAP 87.6%"等**未做过的项目/课程不得保留**（成绩单与面试追问都会穿帮）；只保留真实可辩护的：喀斯特石漠化大赛（待核实细节）、毕设、AI 应用项目

### ⏳ 待办（白天，按序）
1. ✅ **服务器部署新版完成（2026-09-11）**：ECS `root@47.76.101.97` → `cd /root/study` → `git pull && bash deploy.sh`，健康检查 http_code=200，公网验收通过（三工具新版已上线，含形变风险分析）。学习者踩坑：cd 进了文件而文件夹（Not a directory）——find 找到的是文件名，cd 它的目录
2. **README 补演示截图**（占位注释在"🖼 演示截图"处）
3. **开始投递**：按话术每天 30-50 家（AI 应用 / 遥感+AI / 保底轮流），AI 版与 GIS 版简历分开投
4. **学习主线**：每日 2-3 道手写小题 → 面试扫盲 1-7、9 → 有余力再推 V2-B（数据分析工具）/ V2-D（HITL 人工审批）

---

## 我是谁
- 遥感科学与技术本科，会 GIS/ENVI/ArcGIS，有 InSAR 背景
- 转行学 AI 应用开发，目标岗位：AI 应用开发工程师（RAG/Agent/LLM 方向）
- 26 届已毕业，目标城市深圳；主攻 AI 应用开发，遥感+AI 是长期差异化方向

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
  - 第三步：day21.py 整合成品（一个 Agent 三工具：query_regulation 向量查条例 + query_dataset SQL 查数据集 + risk_assessment 风险打分）
  - 踩坑记录：① embedding 必带 chunk_size=10（阿里云每批最多10条）② SQL LIKE 是连续子串匹配 ③ conn.close 必须在函数内 return 前 ④ 真实 API key 禁止硬编码 push（泄漏过一次，已吊销；代码用环境变量 DASHSCOPE_API_KEY）
- ✅ 部署上线：Docker 容器化部署于阿里云 ECS（Ubuntu 22.04，公网 IP 47.76.101.97），Streamlit 服务跑在 8501 端口，**公网可访问：http://47.76.101.97:8501**
  - 服务器操作：SSH 登录（root 用户）、git clone 拉项目、docker build/run、安全组已开 22 和 8501
  - Linux 基础已学：核心命令/权限/文件系统（见 Linux学习笔记.md）
- ⏭️ 下一阶段（求职冲刺）：
  1. ✅ **项目反刍完成**（2026-09-04，day21remake.py 从空白重搭，3 轮 bug 修复 + 全文逐行讲解，教学要点：独立 if 打分 vs if/elif 分级）
  2. ✅ **V2 阶段 A 全部完成**：
     - A1 ✅ day22_seed_data.py（monitoring_series 表 + 18 条川西示范区示例数据，幂等验证过）
     - A2 ✅ day23_risk.py risk_assessment（规则打分：速率+40/加速+30/异常+30；分级 ≤30低/≤60中/>60较高；空数据返回"数据不足"）
     - A3 ✅ risk_assessment 集成进 day21.py（@tool+docstring+create_agent 三工具），验收三问全过
     - A4 ✅ 结构化报告+免责声明已生效（prompt 注入 user_message，分节输出+末尾免责声明）
     - ✅ risk_assessment docstring 触发边界已修（`4452f9c`：仅区域形变风险查询时调用，概念题/数据集查询/法规问答不得误调）
     - ⚠️ 遗留：青藏数据集回答中出现元数据里没有的速率数字 = 幻觉案例，已存档当面试素材；服务器重新部署未做
  3. ✅ **V2 阶段 C（RAG 评估）完成（2026-09-10）**：
     - C1 ✅ rag_eval_questions.py：12 题测试集（问题+期望命中关键词），全部校验关键词区分度
     - C2 ✅ rag_eval.py：评估脚本（建库→检索→关键词命中判断→计数）
     - C3 ✅ 四组实验：chunk_size∈{100,400}×k∈{2,4} → 10/12、11/12、10/12、**12/12**，最优 400+4（100 时命中率 83%）
     - 结论（面试可讲版）：小切片造成语义碎片，适度加大切片 + 提高 k 显著提升命中率；但 k 越大 token 越贵、噪音越多，k 是"最小够用"权衡，评测价值 = 用数据找最小够用参数
     - C4 ✅ 最优参数已落地 day21.py（400/k=4）；⚠️ splitter 的 chunk_size 与 embedding 的 chunk_size=10 是两回事（后者是每批条数）
     - 实验中踩坑（全部独立修复）：build_store 参数未接收、f-string 变量写在引号外、`if hits in material` 选错变量、没导入 st 却用装饰器、Python 路径反复误用
  4. ✅ 简历：AI 应用版已完成（主打 day21 + 毕设项目二 + V2-C 评测成果）
  5. ⏳ 投递 AI 应用开发 / 大模型应用 / AI Agent 岗（进行中）
     - 其他踩坑：脚本必须先 cd 到仓库目录再跑（monitoring.db 曾被建进 F:\VScode 目录）；AUTOINCREMENT 永不复用 ID；UPDATE 定位要用业务字段（date）而非 id；cursor.rowcount 检查影响行数防静默失败
- 每日基础练习：practice_day1（列表循环/if边界/字典查询）✅、practice_two_sum ✅、recent_average ✅、my_max/average_step ✅（持续进行，**手写能力仍需强化**）

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
- API key：禁止硬编码上传 GitHub；代码统一用环境变量 DASHSCOPE_API_KEY 读取（os.getenv）
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
- 前 15 分钟：2 道 Python 基础小题（**手写、不看 AI**——这是当前最大短板，专治"代码都是 AI 写的"）
- 中间 30 分钟：项目推进（V2-B 数据分析工具 / V2-D HITL）或凭记忆重写自己项目的核心函数
- 后 15 分钟：面试题扫盲 1-2 道（按 面试题扫盲清单.md）
- 原则：不贪新知识，把会的东西练到不手生（用户缺口是手误，不是概念）
