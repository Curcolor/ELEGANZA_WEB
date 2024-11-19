#!/bin/bash
python -m venv venv

source venv/Scripts/activate
pip install -r requirements.txt

net start MySQL80
python run.py