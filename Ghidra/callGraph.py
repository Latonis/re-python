import ghidra_bridge

def getAddress(indx):
	return currentProgram.getAddressFactory().getAddress(indx)

with ghidra_bridge.GhidraBridge(namespace=globals()):
	print(getState().getCurrentAddress().getOffset())

	listing = currentProgram.getListing()
	functionManager = currentProgram.getFunctionManager()
	print(listing, functionManager)

	functions = functionManager.getFunctions(True)
	print(functions)
	
		
	import networkx as nx
	import matplotlib.pyplot as plt

	graph = nx.DiGraph()
	for func in functions:
		entryPoint = func.getEntryPoint()
		name = func.getName()
		instructions = listing.getInstructions(entryPoint, True)
		print(f"Function: {name}, Entry Point: {entryPoint}")

		for instr in instructions:
			address = instr.getAddress()
			opcode = instr.getMnemonicString()
			if opcode == "CALL":
				print(f"\t 0x{address}: {instr}")
				flows = instr.getFlows()
				if (len(flows)) == 1:
					targetAddress = f"{flows[0]}" if "EXTERNAL" in str(flows[0]) else f"0x{flows[0]}"
					targetFunc =  targetAddress if "EXTERNAL" in targetAddress else functionManager.getFunctionAt(getAddress(targetAddress)).getName()
					graph.add_edge(name, targetFunc)
	nx.draw(graph, with_labels=True)
	plt.show()

