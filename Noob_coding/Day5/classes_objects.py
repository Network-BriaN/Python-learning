class Mobile :
    def __init__(self, name, cost, RAM, storage, processor, camera, color, is_5G):
        self.name = name
        self.cost = cost
        self.RAM = RAM
        self.storage = storage
        self.processor = processor
        self.camera = camera
        self.color = color
        self.is_5G = is_5G

mobile1 = Mobile("POCO_X2", 20000, 6, 64, 730, 48, "black", False)

print(mobile1.is_5G)
