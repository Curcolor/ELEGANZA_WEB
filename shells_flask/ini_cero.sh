#!/bin/bash
python -m venv venv

pip install -r requirements.txt

source venv/Scripts/activate

net start MySQL80
python run.py