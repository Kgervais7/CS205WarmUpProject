"""
Author: Ian Foertsch
Date:12/30/14
Project: Graph Traversal
"""
import copy
import math
import random


class Location:
    
    def __init__(self, ident, coordinatesList):
        self.identifier = ident
        self.coordinates = []
        for coordinate in coordinatesList:
            self.coordinates.append(coordinate)
        
    def get_coordinates(self):
        return copy.deepcopy(self.coordinates)  
    
    def get_ident(self):
        return self.identifier  
        
    
class Route:
    
    def __init__(self, LocationList, locationsMap):
        self.locations = LocationList
        self.map = locationsMap
    
    def get_locations(self):
        return copy.deepcopy(self.locations)
    
    def get_location_at_index(self, index):
        self.locations
        return copy.deepcopy(self.locations[index])
    
    def get_length(self):
        return len(self.locations)
    
    def status(self):
        for location in self.locations:
            print(self.map.get_location_at_index(location).get_coordinates())
    
    
    """The get_distance method returns the total distance traveled along the route.
    """
    def get_distance(self):
        # First, initialize the index and distance variables to 0, where length
        # is equal to the total number of locations in the Route object's location list
        index = 0
        distance = 0
        length = len(self.locations)
        for loc in self.locations:
            
            first = self.map.get_location_at_index(loc)
            next = self.map.get_location_at_index()
            # handle the special case if the location we're attempting to access is the 
            # last item in the list. This is the case if the index == total list length - 1
            if index == length - 1:
                distance += self.map.get_location_at_index(location).calc_distance(location, self.locations[0])
                return distance
            else:
                distance += calc_distance(location, self.locations[index + 1])
                index += 1
            
    
    
""" the map class is analogous to the "problem" interface for AIMA java: it contains 
the problem state specific information for an instance of the travelling salesman problem.
The dictionary of location objects is generated randomly.
"""
class Locations_Map:
    
    def __init__(self, num_locations, dimensionality, coordinate_boundary):
        #initialize a new, empty dictionary
        self.locationsMap = {}
        #create a number of new, random locations within the specified coordinate boundary
        n = 0
        while n < num_locations:
            #first initialize a specified number of coordinates randomly within the specified coordinate boundary
            coordinates = []
            dimension = 0
            while dimension < dimensionality:
                coordinates.append(random.randint(-coordinate_boundary, coordinate_boundary))
                dimension += 1
            self.locationsMap[n] = Location(n, coordinates)
            n += 1
            
            
    """Get_location returns a deep copy of the location specified by the integer arguement."""
    def get_location(self, loc_num):
        return copy.deepcopy(self.locationsMap[loc_num])
    
    """get_random_route retreives all of the locations stored in the locations hashmap,
    loads deep copies of the locations to a list, shuffles the list and uses that shuffled list
    to return a new route object containing the randomized list."""
    def get_random_route(self):
        locations = list(self.locationsMap.keys())
        """ the shuffle method is located below instead of withing the Route
        constructor due to the fact that the shuffle method modifies the 
        locations list "in Place" that is, it modifies the starting list and 
        returns 'none' ie. something of type 'none' This was the source of 
        frustrating none-type errors' """
        random.shuffle(locations)
        return Route(locations)
    
    def status(self):
        for key in self.locationsMap:
            print(key)
            print(self.locationsMap[key].get_coordinates())
    
    
"""#get_distance accepts 2 location objects, known as 
loc_A and loc_B. if the dimension coordinates of the two
location objects differ, such as if one location is in 3-space
and the second is in 2-space, the object in 2 space is assumed
to be located on the origin for the missing dimensions"""
def prep_coordinates(loc_A, loc_B):
    coordinates_A = loc_A.get_coordinates()
    coordinates_B = loc_B.get_coordinates()
    # If the dimensionality of the two points is identical, then we can return a simple 
    # absolute difference between the two coordinate lists
    if len(coordinates_A) == len(coordinates_B):
        return (coordinates_A, coordinates_B)
    else:
        return fill_coordinates(coordinates_A, coordinates_B)
        
    
    
def calc_distance(loc_A, loc_B):
    coordinates_A, coordinates_B = prep_coordinates(loc_A, loc_B) 
    total = 0
    counter = 0
    for coordinate in coordinates_A:
        total += (coordinate - coordinates_B[counter]) ** 2
        counter += 1
    return math.sqrt(total) 
 

"""fill coordinates calculates the maximum value of two coordinate lists
and fills in the smaller list with 0s until the two lists are of equal size.
This is to allow the comparison of two coordinate lists of unequal size by assuming 
that the smaller coordinate list "lies on the origin" for each dimension for which it 
lacks a coordinate. For example, when comparing [1,2] and [7,8,3,2], the distance computation would
be performed on [1,2,0,0] and [7,8,3,2].
"""
def fill_coordinates(A, B):
    A, B = get_min(A, B)
    while(len(A) < len(B)):
        A.append(0)
    return(A, B)
    

def get_min(A, B):
    if len(A) <= len(B):
        return (A, B)
    else:
        return (B, A)
    

    
