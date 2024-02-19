import sys
import subprocess

from llm_vista.services import DefaultVectoStore

def test_output():
    dsv = DefaultVectoStore()
    assert dsv.url == "BASE_URL_VECTOR"