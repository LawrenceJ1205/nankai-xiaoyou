#!/bin/bash
cd "C:/Users/19301/Desktop/南开小友 知识库"
GIT="/c/Program Files/Git/cmd/git.exe"
for round in 1 2 3; do
  echo "=== ROUND $round ==="
  for i in $(seq 1 15); do
    OUT=$(env -u https_proxy -u http_proxy -u HTTPS_PROXY -u HTTP_PROXY -u all_proxy -u ALL_PROXY GIT_TERMINAL_PROMPT=0 "$GIT" push origin master 2>&1)
    echo "[R$round A$i] $(echo "$OUT" | tail -2 | tr '\n' ' ')"
    if echo "$OUT" | grep -Eq '[0-9a-f]+\.\.[0-9a-f]+ +master -> master' && ! echo "$OUT" | grep -q rejected; then
      echo "PUSH_OK round=$round attempt=$i"
      exit 0
    fi
    sleep 20
  done
  [ $round -lt 3 ] && sleep 60
done
echo "PUSH_FAIL"
exit 1
