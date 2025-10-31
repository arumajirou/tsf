
from __future__ import annotations
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# このファイルは Alembic の環境スクリプトです。
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# モデルメタデータ（必要なら import して metadata を参照）
# 例: from db.models import Base; target_metadata = Base.metadata
target_metadata = None

def get_url() -> str:
    # 環境変数が優先。なければ alembic.ini の sqlalchemy.url
    env = os.getenv("DATABASE_URL")
    if env:
        return env
    # alembic.iniで設定されていれば使う
    return config.get_main_option("sqlalchemy.url")

def run_migrations_offline() -> None:
    # --sql（オフライン）時のみ literal_binds=True を使う
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    # 通常実行。literal_binds=False（指定しない）でOK
    cfg_dict = config.get_section(config.config_ini_section) or {}
    url = get_url()
    if url:
        cfg_dict["sqlalchemy.url"] = url
    connectable = engine_from_config(
        cfg_dict,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
