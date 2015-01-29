
import copy
import Path
from graphics import *

def main():    
    
    
    loc_map = Path.Locations_Map(200,2,50)
    route = loc_map.get_random_route()
    print(route.get_distance())
    
    
    
main()