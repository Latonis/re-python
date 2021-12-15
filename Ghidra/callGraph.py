import ghidra_bridge
with ghidra_bridge.GhidraBridge(namespace=globals()):
	print(getState().getCurrentAddress().getOffset())
	ghidra.program.model.data.DataUtilities.isUndefinedData(currentProgram, currentAddress)
	
