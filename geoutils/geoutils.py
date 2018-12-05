import math
from sympy import Point, Polygon, pi


def take_angle(element):
    return element['angle']


def sort_coordinates(corner_list):
    midpoint = get_midpoint(corner_list)

    corner_metadata = []

    for corner in corner_list:
        angle = get_angle(corner, midpoint)
        corner_metadata.append({'corner': corner, 'angle': angle})


    #print(corner_metadata)
    corner_metadata = sorted(corner_metadata, key = lambda x: x['angle']) #sort by angle
    #print('test list:', test_list)

    sorted_corner_list = []

    for meta in corner_metadata:
        sorted_corner_list.append(meta['corner'])

    return sorted_corner_list

def get_angle(point, midpoint):
    dX = point[0] - midpoint[0]
    dY = point[1] - midpoint[1]
    rads = math.atan2 (-dY, dX)
    rads = rads - (math.pi / 2)
    return rads

def get_midpoint(corner_list):

    lat_list = []
    long_list = []

    for corner in corner_list:
        lat_list.append(corner[1])
        long_list.append(corner[0])

    return (sum(long_list)/len(long_list), sum(lat_list)/len(lat_list))



def bounding_box_within_swath(swath_box, select_box):

    match_1 = False
    match_2 = False
    match_3 = False
    match_4 = False

    if point_east_of_bound(swath_box.corners[0]['long'], select_box.corners[0]['long']):
        if point_south_of_bound(swath_box.corners[0]['lat'], select_box.corners[0]['lat']):
            match_1 = True


    if point_west_of_bound(swath_box.corners[1]['long'], select_box.corners[1]['long']):
        if point_south_of_bound(swath_box.corners[1]['lat'], select_box.corners[1]['lat']):
            match_2 = True

    if point_west_of_bound(swath_box.corners[2]['long'], select_box.corners[2]['long']):
        if point_north_of_bound(swath_box.corners[2]['lat'], select_box.corners[2]['lat']):
            match_3 = True

    if point_east_of_bound(swath_box.corners[3]['long'], select_box.corners[3]['long']):
        if point_north_of_bound(swath_box.corners[3]['lat'], select_box.corners[3]['lat']):
            match_4 = True

    #print(match_1)
    #print(match_2)
    #print(match_3)
    #print(match_4)

    if int(swath_box.corners[0]['long']) == -166:
        print('box found!!!')

        swath_box.print_geometries()

        print(point_east_of_bound(swath_box.corners[0]['long'], select_box.corners[0]['long']))
        print(point_south_of_bound(swath_box.corners[0]['lat'], select_box.corners[0]['lat']))


        print(point_west_of_bound(swath_box.corners[1]['long'], select_box.corners[1]['long']))
        print(point_south_of_bound(swath_box.corners[1]['lat'], select_box.corners[1]['lat']))

        print(point_east_of_bound(swath_box.corners[2]['long'], select_box.corners[2]['long']))
        print(point_north_of_bound(swath_box.corners[2]['lat'], select_box.corners[2]['lat']))

        print(point_west_of_bound(swath_box.corners[3]['long'], select_box.corners[3]['long']))
        print(point_north_of_bound(swath_box.corners[3]['lat'], select_box.corners[3]['lat']))


        #print( swath_box.corners[0]['long'])
        #print(select_box.corners[0]['long'])


    if match_1 and match_2 and match_3 and match_4:

        print(point_east_of_bound(swath_box.corners[0]['long'], select_box.corners[0]['long']))
        print( swath_box.corners[0]['long'])
        print(select_box.corners[0]['long'])

        return True


    return False

def polygon_contain(swath_box, select_box):
    sw1, sw2, sw3, sw4 = [(swath_box.corners[0]['lat'], swath_box.corners[0]['long']), (swath_box.corners[1]['lat'], swath_box.corners[1]['long']), (swath_box.corners[2]['lat'], swath_box.corners[2]['long']), (swath_box.corners[3]['lat'], swath_box.corners[3]['long'])]
    se1, se2, se3, se4 = [(select_box.corners[0]['lat'], select_box.corners[0]['long']), (select_box.corners[1]['lat'], select_box.corners[1]['long']), (select_box.corners[2]['lat'], select_box.corners[2]['long']), (select_box.corners[3]['lat'], select_box.corners[3]['long'])]

    swath_poly = Polygon(sw1, sw2, sw3, sw4)
    select_poly = Polygon(se1, se2, se3, se4)

    print(swath_poly.encloses(select_poly))
    return swath_poly.encloses(select_poly)

def point_east_of_bound(swath_long, select_long):
    if select_long > 90 and swath_long < -90:
        swath_long = swath_long + 180
        select_long = select_long - 180
        if swath_long < select_long:
            return True
    else:
        if swath_long < select_long:
            return True

    return False

def point_west_of_bound(swath_long, select_long):
    if select_long > 90 and swath_long < -90:
        swath_long = swath_long + 180
        select_long = select_long - 180
        if swath_long > select_long:
            return True
    else:
        if swath_long > select_long:
            return True

    return False


def point_north_of_bound(swath_lat, select_lat):
    if swath_lat < select_lat:
        return True
    return False

def point_south_of_bound(swath_lat, select_lat):
     if swath_lat > select_lat:
        return True
     return False