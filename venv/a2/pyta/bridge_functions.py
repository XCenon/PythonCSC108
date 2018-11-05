""" 
Assignment 2: Bridges

The data used for this assignment is a subset of the data found in:
https://www.ontario.ca/data/bridge-conditions
"""

import csv
import math
from typing import List, TextIO

ID_INDEX = 0
NAME_INDEX = 1
HIGHWAY_INDEX = 2
LAT_INDEX = 3
LON_INDEX = 4
YEAR_INDEX = 5
LAST_MAJOR_INDEX = 6
LAST_MINOR_INDEX = 7
NUM_SPANS_INDEX = 8
SPAN_LENGTH_INDEX = 9
LENGTH_INDEX = 10
LAST_INSPECTED_INDEX = 11
BCIS_INDEX = 12

HIGH_PRIORITY_BCI = 60   
MEDIUM_PRIORITY_BCI = 70
LOW_PRIORITY_BCI = 100

HIGH_PRIORITY_RADIUS = 500  
MEDIUM_PRIORITY_RADIUS = 250
LOW_PRIORITY_RADIUS = 100

EARTH_RADIUS = 6371

####### BEGIN HELPER FUNCTIONS ####################


def read_data(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on csv_file.
    """ 

    lines = csv.reader(csv_file)
    data = list(lines)[2:]
    return data


def calculate_distance(lat1: float, lon1: float,
                       lat2: float, lon2: float) -> float:
    """Return the distance in kilometers between the two locations defined by   
    (lat1, lon1) and (lat2, lon2), rounded to the nearest meter.
    
    >>> calculate_distance(43.659777, -79.397383, 43.657129, -79.399439)
    0.338
    >>> calculate_distance(43.42, -79.24, 53.32, -113.30)
    2713.226
    """

    # This function uses the haversine function to find the
    # distance between two locations. You do NOT need to understand why it
    # works. You will just need to call on the function and work with what it
    # returns.
    # Based on code at goo.gl/JrPG4j

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = (math.radians(lon1), math.radians(lat1), 
                              math.radians(lon2), math.radians(lat2))

    # haversine formula t
    lon_diff = lon2 - lon1 
    lat_diff = lat2 - lat1 
    a = (math.sin(lat_diff / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    return round(c * EARTH_RADIUS, 3)


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

THREE_BRIDGES_UNCLEANED = [
    ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403', '43.167233',
     '-80.275567', '1965', '2014', '2009', '4',
     'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012', '72.3', '',
     '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5', '', '70.7', '72.9',
     ''],
    ['1 -  43/', 'WEST STREET UNDERPASS', '403', '43.164531', '-80.251582',
     '1963', '2014', '2007', '4',
     'Total=60.4  (1)=12.2;(2)=18;(3)=18;(4)=12.2;', '61', '04/13/2012',
     '71.5', '', '71.5', '', '68.1', '', '69', '', '69.4', '', '69.4', '',
     '70.3', '73.3', ''],
    ['2 -   4/', 'STOKES RIVER BRIDGE', '6', '45.036739', '-81.33579', '1958',
     '2013', '', '1', 'Total=16  (1)=16;', '18.4', '08/28/2013', '85.1',
     '85.1', '', '67.8', '', '67.4', '', '69.2', '70', '70.5', '', '75.1', '',
     '90.1', '']
    ]

THREE_BRIDGES = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,
                  -80.275567, '1965', '2014', '2009', 4,
                  [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, 
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,
                                 73.3]],
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958',
                  '2013', '', 1, [16.0], 18.4, '08/28/2013',
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]
                ]

#################################################


def format_until_span(items: List[str], new_data: List[object], count: int):
    # ID
    new_data.append(count)
    # name
    new_data.append(items[NAME_INDEX])
    # Highway
    new_data.append(items[HIGHWAY_INDEX])
    # LAT LON
    new_data.append(float(items[LAT_INDEX]))
    new_data.append(float(items[LON_INDEX]))
    # build year
    new_data.append(items[YEAR_INDEX])
    # last MAJOR rebuild
    new_data.append(items[LAST_MAJOR_INDEX])
    # last MINOR rebuild
    new_data.append(items[LAST_MINOR_INDEX])


def append_span(items: List[str], new_data: List[object]) -> int:
    spanNum = int(items[NUM_SPANS_INDEX])
    new_data.append(spanNum)
    # at this point the index dont follow the CONST
    readingPos = SPAN_LENGTH_INDEX
    spanDetail = []
    for spanIndex in range(spanNum):
        # print(spanIndex)
        # push by spilt
        span = items[readingPos]
        indexOfEqual = span.index("(")
        semicolSplit = span[indexOfEqual:].split("=")
        # push the val into detail
        spanDetail.append(float(semicolSplit[1]))
        # increament position
        readingPos += 1

    readingPos += 1
    new_data.append(spanDetail)
    return readingPos


def fomat_rest(items: List[str], new_data: List[object], readingPos: int) -> None:
    # bridge length
    if len(items[readingPos]):
        new_data.append(float(items[readingPos]))
    else:
        new_data.append(0.0)
    # increament position
    readingPos += 1

    new_data.append(items[readingPos])
    # increament position to skip repeate one
    readingPos += 2

    # BCI detail
    BCIDetail = []
    for x in items[readingPos:]:
        if len(x):
            BCIDetail.append(float(x))

    new_data.append(BCIDetail)


def format_data(data: List[List[str]]) -> None:
    # get the data inside
    count = 1
    newDatas = []
    for items in data:
        # ggive temp
        newData = []

        # format before span
        format_until_span(items, newData, count)
        # tackle the span
        readingPos = append_span(items, newData)
        # reset of all
        fomat_rest(items, newData, readingPos)

        newDatas.append(newData)
        count += 1

    data[:] = newDatas[:]
    # print(data)

# Return the data for the bridge with id bridge_id from bridge_data. If
# there is no bridge with the given id, return an empty list.


def get_bridge(bridge_data: List[list], bridge_id: int) -> list:
    for item in bridge_data:
        if item[0] == bridge_id:
            return item

    return []

# Return the average BCI for the bridge with bridge_id from bridge_data.
# If there is no bridge with the id bridge_id, return 0.0. If there are no
# BCIs for the bridge with id bridge_id, return 0.0.


def get_average_bci(bridge_data: List[list], bridge_id: int) -> float:
    for item in bridge_data:
        # get the target item
        if item[0] == bridge_id:
            # average through BCIs
            return sum(item[12]) / len(item[12])

    return 0.0

# Return the total length of bridges in bridge_data on highway.
# Use zero for the length of bridges that do not have a length provided.
# If there are no bridges on highway, return 0.0.


def get_total_length_on_highway(bridge_data: List[list], highway: str) -> float:

    sum = 0.0
    for item in bridge_data:
        if item[HIGHWAY_INDEX] == highway:
            sum += item[LENGTH_INDEX]

    return sum


# Return the distance in kilometres, rounded to the nearest metre
# (i.e., 3 decimal places), between the two bridges bridge1 and bridge2.


def get_distance_between(bridge1: list, bridge2: list) -> float:
    return calculate_distance(bridge1[LAT_INDEX], bridge1[LON_INDEX], bridge2[LAT_INDEX], bridge2[LON_INDEX])
    
# Return the id of the bridge in bridge_data that has the shortest
# distance to the bridge with id bridge_id.


def find_closest_bridge(bridge_data: List[list], bridge_id: int) -> int:
    minin_dis = 999999999
    closest_index = 0
    target = get_bridge(bridge_data, bridge_id)
    for bridge in bridge_data:
        cur_dis = get_distance_between(target, bridge)
        if cur_dis < minin_dis and target[0] != bridge[0]:
            minin_dis = cur_dis
            closest_index = bridge[ID_INDEX]

    return closest_index

# Return the IDs of the bridges that are within radius distance
# from (lat, long).


def find_bridges_in_radius(bridge_data: List[list], lat: float, long: float,
                           distance: float) -> List[int]:
    targetlist = []
    for bridge in bridge_data:
        curDis = calculate_distance(bridge[LAT_INDEX], bridge[LON_INDEX], lat, long)
        if curDis < distance:
            targetlist.append(bridge[0])

    return targetlist

# Return the IDs of the bridges with ids in bridge_ids whose most
# recent BCIs are less than or equal to bci_limit.


def get_bridges_with_bci_below(bridge_data: List[list], bridge_ids: List[int],
                               bci_limit: float) -> List[int]:
    list = []
    for id in bridge_ids:
        # map the index if test case slice it
        indexInArr = index_in_arr_given_id(bridge_data, id)
        curBCI = bridge_data[indexInArr][BCIS_INDEX]
        if curBCI[0] < bci_limit:
            list.append(id)

    return list

# function for finding array index for given ID
# NOTE: I am not sure this situation happens cos when we slice the data the
# id would not match the array index


def index_in_arr_given_id(bridge_data: List[list], id: int) -> int:
    index = 0
    for item in bridge_data:
        if item[0] == id: return index
        index += 1

    return index

# Return a list of IDs of bridges whose names contain search (case insensitive).


def get_bridges_containing(bridge_data: List[list], search: str) -> List[int]:
    list = []
    for bridge in bridge_data:
        bridgeName = bridge[1].upper()
        index = bridgeName.find(search.upper(), 0, len(bridgeName))
        if index != - 1:
            list.append(bridge[0])

    return list


def assign_SPB(bridge_data: List[list], checked: List[int],
               lat: float, lon: float, curList: List[object], priority: int):
    # check which priority
    priority_radius = HIGH_PRIORITY_RADIUS
    priority_BCI = HIGH_PRIORITY_BCI
    if priority == 2:
        priority_radius = MEDIUM_PRIORITY_RADIUS
        priority_BCI = MEDIUM_PRIORITY_BCI
    elif priority == 3:
        priority_radius = LOW_PRIORITY_RADIUS
        priority_BCI = LOW_PRIORITY_BCI

    # find high priority first
    temp = find_bridges_in_radius(bridge_data, lat, lon, priority_radius)
    temp = get_bridges_with_bci_below(bridge_data, temp, priority_BCI)

    for id in temp:
        # map the index if test case slice it
        indexInArr = index_in_arr_given_id(bridge_data, id)
        if checked[indexInArr] == 0:
            curList.append(id)


def filter_right_num(bridge_data: List[list], checked: List[int],
           newList: List[object], max_bridges: int, curList: List[object]):
    index = 0
    curNumberInNewList = 0

    # now push into new List
    while index < len(curList) and curNumberInNewList < max_bridges:
        # map the index if test case slice it
        indexInArr = index_in_arr_given_id(bridge_data, curList[index])
        # not checked by others
        if checked[indexInArr] == 0:
            newList.append(curList[index])
            curNumberInNewList += 1
            checked[indexInArr] = 1

        index += 1

# Return a list of bridge IDs to be assigned to each inspector in
# inspectors. inspectors is a list containing (latitude, longitude) pairs
# representing each inspector's location.


def assign_inspectors(bridge_data: List[list], inspectors: List[List[float]],
                      max_bridges: int) -> List[List[int]]:
    inspectList = []
    checked = [0] * len(bridge_data)

    for inspector in inspectors:
        curList = []
        # get High Priority First
        assign_SPB(bridge_data, checked, inspector[0], inspector[1], curList, 1)
        # if it is not enough
        if len(curList) < max_bridges:
            assign_SPB(bridge_data, checked, inspector[0], inspector[1], curList, 2)
        # if it is not enough
        if len(curList) < max_bridges:
            assign_SPB(bridge_data, checked, inspector[0], inspector[1], curList, 3)

        # get the right number for each inspectors
        newList = []
        filter_right_num(bridge_data, checked, newList, max_bridges, curList)
        inspectList.append(newList)
    return inspectList

# Update the bridges in bridge_data with id in bridge_ids with the new
# date and BCI score for a new inspection.


def inspect_bridges(bridge_data: List[list], bridge_ids: List[int], date: str, 
                    bci: float) -> None:

    for id in bridge_ids:
        bridge_data[id - 1][LAST_INSPECTED_INDEX] = date
        bridge_data[id - 1][BCIS_INDEX].insert(0, bci)

# Update the bridge with the id bridge_id to have its last rehab set to
# new_date. If is_major is True, update the major rehab date. Otherwise,
# update the minor rehab date.


def add_rehab(bridge_data: List[list], bridge_id: int, new_date: str, 
              is_major: bool) -> None:

    if is_major:
        bridge_data[bridge_id - 1][LAST_MAJOR_INDEX] = new_date
    else:
        bridge_data[bridge_id - 1][LAST_MINOR_INDEX] = new_date


if __name__ == '__main__':
    # pass
    import doctest
    doctest.testmod()

    import python_ta

    python_ta.check_all("bridge_functions.py")

    # add_rehab(bridges, test_Index, "99999", 1)
    # print(get_bridge(bridges, test_Index))
    # inspect_bridges(bridges, [test_Index, test_Index + 1], "777", 999)
    # print(get_bridge(bridges, test_Index))
    # print(get_bridge(bridges, test_Index + 1))
