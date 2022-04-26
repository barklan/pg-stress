#!/usr/bin/env bash

for _ in {1..100000}; do
    for _ in {1..100}; do
        xh get :8000 &
    done
    echo "sent requests"
    sleep 1
done
