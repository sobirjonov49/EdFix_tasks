class SpaceAircraft:
    def __init__(self, model, height, fuel):
        self.model=model
        self.height=height
        self.fuel=fuel
    def launch(self, km):
        print(f"{self.model} raketasi {km} km balanlikda har kmga 100 litr yoqilg'i sarf qiladi")
    def land(self, km): 
        if km/100<=self.fuel:
            print(f"{self.model} raketasi manzilga yetib kelib qo'ndi")
        else:
            print(f"No fuel")
raketa1=SpaceAircraft("sparkle_11", 5000, 420)
raketa1.land(25000)
raketa1.launch(25)
raketa1.land(50000)