class CropRatio:

    def __init__(self):
        self._crops = {}
        self._total_weight = 0

    def add(self, name, crop_weight):
        
        # Update the total weight of crops
        self._total_weight += crop_weight

        # Add crop with crop_weight if not in dict(_crops)
        if not name in self._crops:
            self._crops[name] = crop_weight
        else: 
            # Add to crop_weight if crop found in dict(_crops)
            self._crops[name] += crop_weight
        
    def proportion(self, name):
        # If crop not in dict(_crops) return 0
        if (not name in self._crops or 
            self._crops[name] <= 0 or 
            self._total_weight <= 0): 
            return 0

        return self._crops[name]/self._total_weight
    

if __name__ == "__main__":
    crop_ratio = CropRatio()
    crop_ratio.add('Wheat', 1)
    crop_ratio.add('Wheat', 4)
    crop_ratio.add('Rice', 5)
    
    print(crop_ratio.proportion('Wheat'))