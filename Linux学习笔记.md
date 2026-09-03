# Linux 学习笔记（部署方向）

> 学习目标：不追求全面，只学「把 AI 应用部署上线」够用的部分。
> 练习环境：Ubuntu 那台电脑（本机 Windows 不装 WSL）。

## 一、为什么要学 Linux

- Linux = 服务器操作系统（免费、开源、稳定）。
- 你部署 AI 应用，就是让它跑在一台 **Linux 服务器**上。
- 分工：Windows 写代码 → 服务器 Linux 跑代码。所以必须会 Linux。

## 二、三个核心概念

1. **Shell**：命令行界面。Windows 用 cmd/PowerShell，Linux 用 **bash**（就是你敲命令的黑框）。
   - Windows 敲 `python xxx.py`，Linux 里是 `python3 xxx.py`。
2. **一切皆文件**：Linux 里几乎所有东西都抽象成「文件」（配置文件、日志、甚至设备）。看懂目录 + 会查文件 = 会一半 Linux。
3. **权限**：每个文件有「拥有者 / 所属组 / 其他人」三组权限（读/写/执行），后面部署 Nginx 时必用。

## 三、文件系统结构（记这几个就够部署用）

| 路径 | 放什么 |
|---|---|
| `/` | 根目录，一切从这里开始 |
| `/home/你的用户名` | 你的家目录，记作 `~`，你的代码放这 |
| `/etc` | 配置文件（Nginx 配置就在这） |
| `/var` | 日志、运行中变化的数据（Nginx 日志在这） |
| `/usr` | 装的软件 |
| `/tmp` | 临时文件 |

## 四、8 个核心命令

| 命令 | 作用 | 例子 |
|---|---|---|
| `pwd` | 显示当前目录 | `pwd` |
| `ls` | 列出文件 | `ls -l`（带详细信息/权限）|
| `cd` | 切换目录 | `cd ~` 回家目录 |
| `mkdir` | 建目录 | `mkdir myapp` |
| `touch` | 建空文件 | `touch app.py` |
| `cat` | 看文件内容 | `cat app.py` |
| `cp` / `mv` / `rm` | 复制 / 移动 / 删除 | `mv app.py demo.py` |
| `man` | 查命令帮助（万能手册）| `man ls` |

补充小技巧：
- 按 `Tab` 自动补全文件名/命令；按 `↑` 调出上一条命令。
- `ls -la` 连隐藏文件一起列（`.` 开头的都是隐藏文件）。

## 五、作业（进 Ubuntu 后照做）

1. `cd ~` 回家目录，`pwd` 看看自己在哪
2. `mkdir linux_practice` 建练习目录，`cd linux_practice` 进去
3. `touch hello.txt` 建空文件，`ls -l` 看它的权限
4. `cat hello.txt`（空文件没输出，正常）
5. 用 `man ls` 看看 ls 的帮助，按 `q` 退出

## 六、下一步预告

- 文件权限（chmod / chown）
- 软件安装（apt 包管理器）
- SSH 远程连接服务器
- 进程管理（ps / top / systemctl）
- vim 文本编辑器（在服务器上改配置文件要用）

---

进度记录：本文件由 AI 整理，配合「第二台电脑 AI 交接」使用。学完一节更新 AGENTS.md 并 git push。
