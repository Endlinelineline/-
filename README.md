年会抽奖
科技有限公司有300员工，开年会抽奖，奖项如下:
一等奖3名:泰国5日游+手术费报销
二等奖6名:	iPhone14手机	
三等奖30名:	三斤苹果	
规则:
1.共抽3次，第一次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
2.每个员工限中奖一次，不能重复

解题思路:
1.生成一个员工列表，用random模块从里面取随机值
2.取完值之后，立刻从员工大列表里把中奖人删掉，即可防止其再次中奖
