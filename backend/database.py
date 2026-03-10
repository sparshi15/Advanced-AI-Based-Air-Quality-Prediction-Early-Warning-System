import psycopg2
import os

DATABASE_URL = os.getenv("postgresql://postgres:OYGCdleLhOiEVoqdZguneyUkUmAfDQQZ@turntable.proxy.rlwy.net:39588/railway")

conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()
