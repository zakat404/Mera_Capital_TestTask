#!/usr/bin/env bash
# wait-for-it.sh

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z "$host" "$port"; do
  >&2 echo "Сервис $host:$port недоступен - ожидаем..."
  sleep 1
done

>&2 echo "Сервис $host:$port доступен - продолжаем..."
exec $cmd
