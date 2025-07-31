@echo off
title Astraeus Quick Start

echo Starting Astraeus Trading System...
echo ===================================

REM Check virtual environment
if not exist "venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found
    echo Please run setup first
    pause
    exit /b 1
)

REM Check .env file
if not exist ".env" (
    echo ERROR: .env file not found
    echo Please configure API keys first
    pause
    exit /b 1
)

echo Starting system...
venv\Scripts\python.exe main.py

echo.
echo System stopped. Press any key to exit...
pause >nul