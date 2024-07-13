class Mobile:
    countryCodes = {
        "880": "Bangladesh",
        "966": "India",
        "455": "USA"
    }

    def __init__(self, model, simCardStatus, balance=0):
        self.model = model
        self.simCardStatus = simCardStatus
        self.balance = balance
        self.call_history = []
        print(f"Model {self.model} is manufactured.")

    def setSimCardStatus(self, status):
        self.simCardStatus = status
        print("SIM card status updated successfully.")
    
    def __str__(self):
        return f"Mobile Phone Detail:\nModel: {self.model}\nSIM Card Status: {self.simCardStatus}\nBalance: {self.balance} TK"
    
    
class Nokia(Mobile):
    def __init__(self, model, simCardStatus, balance=0):
        super().__init__(model, simCardStatus, balance)
        
    

    def rechargeSIMCard(self, amount):
        self.balance += amount
        print(f"Recharge successful! Current balance {self.balance} TK.")

    def dialCall(self, number):
        if not self.simCardStatus:
            return "No SIM card available!"
        
        if self.balance <= 0:
            return "Insufficient balance!"

        country_code = number[:3]
        if country_code not in Mobile.countryCodes:
            return "Dialing is not allowed in this region."

        self.balance -= 10  
        self.call_history.append(number)
        return f"Dialing the number {number} to {Mobile.countryCodes[country_code]} region."

    def dialCallHistory(self):
        return '\n'.join(self.call_history)



N1100 = Nokia("N1100", True, 100)
print(N1100)

N3110 = Nokia("N3110", False)
print(N3110)

N3110.setSimCardStatus(True)
print(N3110)

N3110.rechargeSIMCard(200)
print(N3110)

print(N3110.dialCall("88017196xxxx"))
print(N3110.dialCall("96617196xxxx"))
print(N3110.dialCall("45517196xxxx"))

print(N1100.dialCall("88017196xxxx"))
print(N1100.dialCall("45517196xxxx"))
print(N1100.dialCall("96617196xxxx"))

print(f"Dial call history for {N1100.model}:\n{N1100.dialCallHistory()}")
print(f"Dial call history for {N3110.model}:\n{N3110.dialCallHistory()}")
        
        
           