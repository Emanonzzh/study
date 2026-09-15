"""agent_lab.db —— 统一数据库连接（从仓库根 .env 读凭据）。

为什么单独抽一层：tools / anomaly / inject / evaluate 四个模块都要连库，
连接参数散落各处时，改一次端口就要改四处（DRY）。
"""
from __future__ import annotations

import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(str(PROJECT_ROOT / ".env"))


def connect(database: str | None = None) -> pymysql.connections.Connection:
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=database or os.getenv("DB_NAME"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def query(sql: str, args: tuple = ()) -> list[dict]:
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, args)
            return cur.fetchall()
    finally:
        conn.close()


def execute(sql: str, args: tuple = ()) -> int:
    """执行写操作（仅注入脚本使用；生产分析路径必须只读）。"""
    conn = connect()
    try:
        with conn.cursor() as cur:
            rows = cur.execute(sql, args)
        conn.commit()
        return rows
    finally:
        conn.close()


def table_exists(name: str) -> bool:
    rows = query(
        "SELECT COUNT(*) AS c FROM information_schema.tables "
        "WHERE table_schema = DATABASE() AND table_name = %s",
        (name,),
    )
    return bool(rows and rows[0]["c"])
