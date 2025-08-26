from abc import ABC, abstractmethod

class ScanTool(ABC):
    @property
    @abstractmethod
    def scan_device(self):
        pass
class VirusScan(ScanTool):
    @property
    def scan_device(self):
        return "Scanning for viruses..."

class FwScan(ScanTool):
    @property
    def scan_device(self):
        return "Scanning for firewall threats..."

#### Usage ####
tools = [VirusScan(), FwScan()]
for tool in tools:
    print(tool.scan_device)

