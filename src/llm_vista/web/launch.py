import sys
import streamlit as st
from streamlit.web import cli as stcli
from streamlit import runtime
import sys
import os


def main(*args, **kwargs):
    print(f"******* {args} \n*******")
    print(f"******* {kwargs} \n*******")
    if runtime.exists():
        main()
    else:
        print(f"******* {os.getcwd()} \n*******")
        print(f"******* {os.listdir(os.getcwd())} \n*******")
        sys.argv = ["streamlit", "run", "app.py"]
        sys.exit(stcli.main())
