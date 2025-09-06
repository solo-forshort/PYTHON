class SecureScan:
    def show_report(self):
        print("Generic security scan report")

class VirusScan(SecureScan):
    def show_report(self):
        print("Virus scan report: No threats found")

class FirewallRules(SecureScan):
    def show_report(self):
        print("Firewall rules report: All rules are active")

class IntrusionDetection(SecureScan):
    def show_report(self):
        print("Intrusion detection report: No intrusions detected")

def perform_scan(tool):
    tool.show_report()

    ### Creating Objects
# virus = VirusScan()
# firewall = FirewallRules()
# intrusion = IntrusionDetection()

# perform_scan(virus)
# perform_scan(firewall)
# perform_scan(intrusion)

#creating all tool objects in a list
tools = [VirusScan(), FirewallRules(), IntrusionDetection()]

#Loop through each tool and run the scan
for tool in tools:
    perform_scan(tool)
