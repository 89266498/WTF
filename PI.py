import clr
import System
if is_netcoreapp:
    clr.AddReference("System.Diagnostics.Process")
process = System.Diagnostics.Process()
process.StartInfo.FileName = cmd
process.StartInfo.Arguments = args
process.StartInfo.CreateNoWindow = True
process.StartInfo.UseShellExecute = False
process.StartInfo.RedirectStandardInput = False
process.StartInfo.RedirectStandardOutput = False
process.StartInfo.RedirectStandardError = False
process.Start()
process.WaitForExit()