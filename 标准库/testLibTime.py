import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
#
# time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 获取两天前时间
nowTime=time.time()

twoDayAgoTime=nowTime-60*60*24*2
nowTimeTupele=time.localtime(nowTime)

twoDayAgoTimeTuple=time.localtime(twoDayAgoTime)
print(time.strftime("%Y年%m月%d日 %H:%M:%S", nowTimeTupele))
print(time.strftime("%Y年%m月%d日 %H:%M:%S", twoDayAgoTimeTuple))
