# add module root path to system path
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

from testing.flower import Flower

class Basket:
    def __init__(self):
        self.color = Flower()

    def describe(self):
        return f"This basket has {self.color.getColor()} flowers"
    

if __name__ == "__main__":
    basket = Basket()
    print(basket.describe())

