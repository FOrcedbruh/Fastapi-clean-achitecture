#! /bin/bash
set -e
sleep 2

alembic upgrade head


exec python main.py