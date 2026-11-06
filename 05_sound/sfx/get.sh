#!/usr/bin/env bash
# usage: get.sh name url [name url ...]
while [ $# -ge 2 ]; do curl -sS -m 60 -o "$1.mp3" -w "$1 %{http_code}\n" "$2"; shift 2; done
