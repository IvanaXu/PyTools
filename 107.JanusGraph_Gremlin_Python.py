#
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
	
connection = DriverRemoteConnection('ws://yiyin.site:8182/gremlin', 'g')
graph = traversal().withRemote(connection)
# 添加节点
graph.addV('person').property('name', 'test').next()
# 输出为 ['test']
print(graph.V().values('name').toList())	
