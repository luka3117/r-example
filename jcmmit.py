#-*- coding: utf-8 -*-
import os
import re
import sys
from datetime import datetime

commit_message=input("コミット入力")
# commit_message=str(datetime.now())
# commit_message=re.sub("\.|:", "-", commit_message)


os.system("git add . ")
os.system("git commit -m"+""+commit_message)
os.system("git push")
