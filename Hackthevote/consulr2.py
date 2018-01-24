#run as  :   python consulr2.py 2>/dev/null


import r2pipe
import json

r2 = r2pipe.open("./consul.dcdcdac48cdb5ca5bc1ec29ddc53fb554d814d12094ba0e82f84e0abef065711")
r2.cmd('ood')
r2.cmd('aaa')
r2.cmd('db 0x00400b45')
r2.cmd('dc')
r2.cmd('db 0x00400a76')
r2.cmd('dr rip=0x00400a6a')
r2.cmd('dc')
r2.cmd('db 0x00400a38')
r2.cmd('db 0x00400a2e')
for i in range(0,63):
	r2.cmd('dr rip=0x00400a0d')
	r2.cmd('dc')
	r2.cmd('dc')
r2.cmd('dr rip=0x00400a0d')
r2.cmd('dc')
print(r2.cmd('ps @ rsi'))



