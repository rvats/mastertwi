from typing import List, Any


def nearestXsteakHouses(totalSteakhouses, allLocations, numSteakhouses):
    # WRITE YOUR CODE HERE
    if (numSteakhouses == totalSteakhouses):
        return allLocations

    nearestXsteakHousesLocation = []
    nearestXsteakHousesDistance = []

    for location in allLocations:
        currentLocationDistance = (location[0] ** 2) + (location[1] ** 2)
        if (len(nearestXsteakHousesLocation) < numSteakhouses):
            nearestXsteakHousesLocation.append(location)
            nearestXsteakHousesDistance.append(currentLocationDistance)
        else:
            farthestLocationDistance = max(nearestXsteakHousesDistance)
            if (currentLocationDistance < farthestLocationDistance):
                farthestLocationIndex = nearestXsteakHousesDistance.index(farthestLocationDistance)
                nearestXsteakHousesLocation[farthestLocationIndex] = location

    return nearestXsteakHousesLocation

print(nearestXsteakHouses(3,[[1,2],[3,4],[1,-1]],2))