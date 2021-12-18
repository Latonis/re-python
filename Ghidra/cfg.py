import ghidra_bridge

with ghidra_bridge.GhidraBridge(namespace=globals(), hook_import=True):

   from ghidra.program.model.block import SimpleBlockModel
   from ghidra.util.task import TaskMonitor

   model = SimpleBlockModel(currentProgram)
   blocks = model.getCodeBlocks(TaskMonitor.DUMMY)

   for block in blocks:
       print(block)
