#-*- coding: utf-8 -*-
import os
import re
import sys


commit_message=input("コミット入力")

os.system("git add . ")
os.system("git commit -m"+""+commit_message)
os.system("git push")
