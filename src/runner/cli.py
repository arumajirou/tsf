import argparse
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    print("PyYAML が未インストールです。`pip install -r requirements.txt` を実行してください。", file=sys.stderr)
    raise

from src.core.run import resolve_config, validate_config


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tsf", description="Time Series Forecasting runner")
    sub = p.add_subparsers(dest="command", required=True)

    for name in ("run", "train"):  # train を run のエイリアスとして実装
        sp = sub.add_parser(name, help="設定を読み込み、（dry-run時は）解析のみ実施")
        sp.add_argument("--config", "-c", type=str, default="conf/config.yaml", help="メイン設定ファイル（YAML）")
        sp.add_argument("--dry-run", action="store_true", help="設定解決と検証のみ（学習/推論は実行しない）")
    return p


def cmd_run(args: argparse.Namespace) -> int:
    cfg_path = Path(args.config)
    if not cfg_path.exists():
        print(f"[ERR] config が見つかりません: {cfg_path}", file=sys.stderr)
        return 2

    resolved = resolve_config(cfg_path)
    validate_config(resolved)

    if args.dry_run:
        print("=== DRY RUN: 設定の解決結果（抜粋） ===")
        important = {}
        for k in ("name", "data", "model", "training", "tracking"):
            if k in resolved:
                important[k] = resolved[k]
        print(yaml.safe_dump(important, sort_keys=False, allow_unicode=True))
        print("OK: 設定は有効です（学習/推論は実行していません）")
        return 0

    print("TODO: 学習/推論/バックテストの実処理をこの先に実装します。")
    return 0


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command in ("run", "train"):
        return cmd_run(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
