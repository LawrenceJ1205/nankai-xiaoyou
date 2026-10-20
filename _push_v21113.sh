#!/bin/bash
cd "C:/Users/19301/Desktop/南开小友 知识库" || exit 1
for round in 1 2 3; do
  for i in $(seq 1 15); do
    out=$(git push origin master 2>&1)
    echo "[r$round a$i] $(echo "$out" | tr '\n' ' ' | cut -c1-160)"
    if echo "$out" | grep -qE 'master -> master' && ! echo "$out" | grep -qi 'rejected'; then
      echo "PUSH_OK round=$round attempt=$i"
      exit 0
    fi
    sleep 6
  done
  echo "[r$round] round exhausted, sleeping 60"
  sleep 60
done
echo "PUSH_FAIL"
exit 1
