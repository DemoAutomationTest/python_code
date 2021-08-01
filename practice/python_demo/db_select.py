import os,sys
o_path = os.getcwd()
sys.path.append(o_path)
from Module.AUTO_HELP import DB_Link

result=DB_Link("select * from esun_account")
print(result[0])