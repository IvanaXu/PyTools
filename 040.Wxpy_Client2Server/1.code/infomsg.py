import MySQLdb

ing=''
state=0


"""
    try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='xuyifan',db='infologin',port=3306)
	cur=conn.cursor()
	strout=cur.execute('select * from LoginTable Where User ='+'"'+checkusr+'"'+'and Password ='+'"'+checkpaw+'"')
	if(strout!=0):
	    return 'Y'
	else:
	    return 'Warning'
	cur.close()
	conn.close()
    except MySQLdb.Error,e:
	err='Mysql Error '+str(e.args[0])+':'+e.args[1]
	return err
	#___Sql_________
"""

def sqlmatch(checkusr,checkpaw):
    return 'Y'
