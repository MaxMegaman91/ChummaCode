class Database():
    def __init__(self,conditionlist,*existingdata):
        self.databoard = [conditionlist]
        importData = existingdata
        self.databoard.append(importData)
    
    def query(self,*queryFor):
        return