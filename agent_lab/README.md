# agent_lab —— 手写 Agent 与分析内核代码（快照）

这是我**不依赖任何 Agent 框架**手写的实验代码，属于销售经营分析项目的一部分。

## 一、Agent 实验线（手写 ReAct）

| 文件 | 内容 |
|---|---|
| `tools.py` | 4 个纯函数工具：指标查询 / 月度趋势 / 维度排名 / **量价三因子分解**（含精确加总断言） |
| `p1_react.py` | 手写 ReAct 循环：步数上限 / token 预算 / 重复动作检测 / observation 截断 / 错误回传 / 全轨迹 |
| `p1_stress.py` | 6 场景故障注入压测（超纲 / 非法参数 / DB 超时 / 模糊提问 / 跨维度 / 重度取数） |
| `db.py` | 统一数据库连接 |

## 二、分析内核：异常检测与评测（D3/D4）

| 文件 | 内容 |
|---|---|
| `anomaly.py` | 异常检测：**周内效应校正** + 日历校正 + **MAD 稳健统计** + 脉冲/漂移两类异常 |
| `inject_anomalies.py` | 注入 6 个已知异常到副本表 `orders_injected`，产出 ground truth |
| `evaluate_anomaly.py` | **差分口径 + 事件化后处理**的 P/R/F1 评测 |
| `eval/anomaly_report.md` | 评测报告（含门槛取舍实验与误报归因） |

## 三、接口层（D6）：FastAPI

| 文件 | 内容 |
|---|---|
| `api.py` | 6 个接口：`/health` `/metrics` `/anomalies` `/report/{period}` `/reconciliation/{period}` `/analyze` |
| `api_smoke_test.py` | Python 客户端冒烟测试（7 项：含边界校验 422、404、中文 UTF-8） |
| `streamlit_app.py` | **销售经营分析看板**（Streamlit + Plotly） |
| `ui_smoke_test.py` | 用官方 `AppTest` 无头跑一遍看板（UI 层冒烟测试） |
| `FastAPI入门.md` | 给没写过 FastAPI 的人：四个核心概念 / 状态码 / **`def` vs `async def`** / 练习 / 上生产缺什么 |

看板五个页签：**量价归因（瀑布图）· 维度下钻 · 异常发现 · 报告与对账 · 自然语言问数**。

启动与验证：

```bash
python agent_lab/api.py                          # 起 API 服务
# 浏览器打开 http://127.0.0.1:8000/docs        ← 可直接点着测
streamlit run agent_lab/streamlit_app.py --server.port 8502
# 浏览器打开 http://127.0.0.1:8502             ← 看板
python agent_lab/api_smoke_test.py               # 7 项接口冒烟（不花钱）
python agent_lab/ui_smoke_test.py                # UI 冒烟（AppTest 无头执行）
python agent_lab/api_smoke_test.py --with-llm    # 额外测 /analyze（调 LLM）
```

**为什么接口一律用 `def` 而不是 `async def`**：分析是同步阻塞的（pymysql + 报告渲染 1~8 秒）。
FastAPI 对 `def` 会自动丢线程池、不占事件循环；写成 `async def` 里跑同步阻塞代码会**卡死整个服务**。

## 四、两份文档

| 文件 | 用途 |
|---|---|
| `代码导读.md` | 读码顺序 / 每个文件的关键代码片段与解释 / 面试"讲代码"路线 / 9 个追问 |
| `FastAPI入门.md` | FastAPI 零基础入门（结合本项目真实代码） |

## ⚠️ 运行前提

- 需要 **MySQL**（`orders` 表 102,287 行）+ **DeepSeek key**（`.env`）
- **低配机 / 无 MySQL 时只读代码，不要运行** —— 读代码 + 写注释同样能学会

## 本目录定位

- 这是**可读快照**，方便在别的电脑上 `git pull` 后阅读学习
- **活的版本**在 `ai-commerce-intelligence-platform/agent_lab/`（另一个仓库），会继续迭代
- 两处如有差异，以那边为准

## 学习重点（面试要能讲）

1. **量价三因子分解**为什么能精确加总（`ΔR = 量效应 + 价效应 + 交互项`，断言闭合 0.0）
2. **ReAct 循环**的停止条件有哪几个、为什么"重复动作检测"不能只看参数相同
3. **错误回传**：工具报错为什么当 observation 回传给模型，而不是直接抛异常
4. **异常检测第一版为什么错**：175 个误报的根因是**周内效应**（拿周六比周一）
5. **评测方法也会错**：P 只有 35% 时先逐条归因，发现"误报"全是同一事件的多次检出 →
   加**事件化后处理**而不是调阈值；并用**差分口径**剔除真实业务事件（元旦暴涨）的噪声地板
