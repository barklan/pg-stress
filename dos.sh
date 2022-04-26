#!/usr/bin/env bash

for _ in {1..100000}; do
    for _ in {1..30}; do
        xh get :8000 &
    done
    sleep 3
    echo "sent requests"
done
