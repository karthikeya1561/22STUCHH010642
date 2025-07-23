from utils.log import log
import sqlite3
from . import schemas

DB_PATH = "./test.db"

def create_url(url: schemas.UrlCreate):
    log(stack="backend", level="info", pkg="repository", message="create_url called")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute(
        "INSERT INTO url_mappings (original_url, short_url) VALUES (?, ?)",
        (url.original_url, url.short_url)
    )
    conn.commit()
    url_id = cursor.lastrowid
    cursor.execute("SELECT id, original_url, short_url FROM url_mappings WHERE id = ?", (url_id,))
    row = cursor.fetchone()
    conn.close()
    return {"id": row[0], "original_url": row[1], "short_url": row[2]}

def get_url(url_id: int):
    log(stack="backend", level="info", pkg="repository", message="get_url called")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("SELECT id, original_url, short_url FROM url_mappings WHERE id = ?", (url_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "original_url": row[1], "short_url": row[2]}
    return None

def get_url_by_shortened(shortened_url: str):
    log(stack="backend", level="info", pkg="repository", message="get_url_by_shortened called")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("SELECT id, original_url, short_url FROM url_mappings WHERE short_url = ?", (shortened_url,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "original_url": row[1], "short_url": row[2]}
    return None

def get_urls(skip: int = 0, limit: int = 10):
    log(stack="backend", level="info", pkg="repository", message="get_urls called")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("SELECT id, original_url, short_url FROM url_mappings LIMIT ? OFFSET ?", (limit, skip))
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "original_url": row[1], "short_url": row[2]} for row in rows]

def delete_url(url_id: int):
    log(stack="backend", level="info", pkg="repository", message="delete_url called")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("SELECT id, original_url, short_url FROM url_mappings WHERE id = ?", (url_id,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM url_mappings WHERE id = ?", (url_id,))
        conn.commit()
    conn.close()
    if row:
        return {"id": row[0], "original_url": row[1], "short_url": row[2]}
    return None