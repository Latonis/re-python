# This directory holds all of my Ghidra automation scripts.

## Directions for Ghidra Bridge
1. `pip3 install ghidra_bridge`
2. `python3 -m ghidra_bridge.install_server ~/ghidra_scripts`
3. Use in Python3 script:
	```
	import ghidra_bridge
	with ghidra_bridge.GhidraBridge(namespace=globals()):
    	print(getState().getCurrentAddress().getOffset())
    	ghidra.program.model.data.DataUtilities.isUndefinedData(currentProgram, currentAddress)
	```
## Sources
- https://www.sentinelone.com/labs/a-guide-to-ghidra-scripting-development-for-malware-researchers/
- https://class.malware.re/2021/03/08/ghidra-scripting.html
