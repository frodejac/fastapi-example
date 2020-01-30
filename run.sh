#!/usr/bin/env bash

exec uvicorn --reload --host 0.0.0.0 --port 8090 --log-level debug app.app:app
