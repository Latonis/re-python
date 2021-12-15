import ghidra_bridge

def getAddress(indx):
	return currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(indx)

with ghidra_bridge.GhidraBridge(namespace=globals()):
	print(getState().getCurrentAddress().getOffset())
	ghidra.program.model.data.DataUtilities.isUndefinedData(currentProgram, currentAddress)

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
		if (name == "entry"):
			count = 0
			for instr in instructions:
				address = instr.getAddress()
				opcode = instr.getMnemonicString()
				if opcode == "CALL" and count < 10:
					count += 1
					print(f"\t 0x{address}: {instr}")
					flows = instr.getFlows()
					if (len(flows)) == 1:
						targetAddress = f"0x{flows[0]}"
						graph.add_edge(name, targetAddress)
				elif (count == 10):
					break
		print(f"Function: {name}, Entry Point: {entryPoint}")
	nx.draw(graph, with_labels=True)
	plt.show()

