@echo off
cd /d "d:\rbu_honors_assessment-main\rbu_honors_assessment-main"
python -m uvicorn server:app --host 0.0.0.0 --port 8000