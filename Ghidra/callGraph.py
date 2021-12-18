import ghidra_bridge

def getAddress(indx):
	return currentProgram.getAddressFactory().getAddress(indx)

with ghidra_bridge.GhidraBridge(namespace=globals(), hook_import=True):
	print(getState().getCurrentAddress().getOffset())

	listing = currentProgram.getListing()
	functionManager = currentProgram.getFunctionManager()
	print(listing, functionManager)

	functions = functionManager.getFunctions(True)
	print(functions)
	
		
	import networkx as nx
	import matplotlib.pyplot as plt
	import numpy as np
	from ghidra.util.task import TaskMonitor

	graph = nx.Graph()
	for func in functions:
		print(f"Function Name: {func.getName()}")
		print(f"Function Body: {func.getBody()}")
		print(f"Function Entry Point: {func.getEntryPoint()} ")

		print(f"Function Called by: {func.getCalledFunctions(TaskMonitor.DUMMY)}")
		graph.add_edges_from([(func.getName(), x.getName()) for x in func.getCalledFunctions(TaskMonitor.DUMMY)])
		# print(f"Function Calling: {func.getCallingFunctions(TaskMonitor.DUMMY)}")
		# entryPoint = func.getEntryPoint()
		# name = func.getName()
		# instructions = listing.getInstructions(entryPoint, True)
		# print(f"Function: {name}, Entry Point: {entryPoint}")
		# graph.add_edge(name, targetFunc)
	pos = nx.spring_layout(graph, k=0.3*1/np.sqrt(len(graph.nodes())), iterations=20)
	nx.draw_planar(graph, with_labels=True, verticalalignment='top')
	# nx.draw(graph, pos=pos, )
	# nx.draw_networkx_nodes(graph, pos=pos, node_size=600, node_color='w', alpha=0.4, node_shape='d')
	# nx.draw_networkx_labels(graph, pos=pos)
	plt.show()

