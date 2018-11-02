import csv
import bridge_functions as bf
import unittest
import formatted_data as fb
import copy
import random
BRIDGE_FORMATTED = bf.read_data(open('bridge_data.csv'))
BRIDGE_FORMATTED_BACK_UP = fb.BRIDGE_FORMATTED_BACK_UP
class TestFormatData(unittest.TestCase):
    def test_first_fifty(self):
        expect = fb.first_fifty
        BRIDGE_FORMATTED_COPY = copy.deepcopy(BRIDGE_FORMATTED)
        BRIDGE_FORMATTED_COPY = BRIDGE_FORMATTED[:50]
        bf.format_data(BRIDGE_FORMATTED_COPY)
        actual = BRIDGE_FORMATTED_COPY
        self.assertEqual(expect, actual, "You should format data as described in the handout")
    
    def test_fifty_to_hundred(self):
        expect = fb.fifty_to_hundred_formatted
        BRIDGE_FORMATTED_COPY = copy.deepcopy(BRIDGE_FORMATTED)
        BRIDGE_FORMATTED_COPY = BRIDGE_FORMATTED[50:100]
        bf.format_data(BRIDGE_FORMATTED_COPY)
        actual = BRIDGE_FORMATTED_COPY        
        self.assertEqual(expect, actual, "You should format data as described in the handout")

    def test_middle_fifty(self):
        expect = fb.middle_fifty_formatted
        BRIDGE_FORMATTED_COPY = copy.deepcopy(BRIDGE_FORMATTED)
        BRIDGE_FORMATTED_COPY = BRIDGE_FORMATTED[949:1001]        
        bf.format_data(BRIDGE_FORMATTED_COPY)
        actual = BRIDGE_FORMATTED_COPY        
        self.assertEqual(expect, actual, "You should format data as described in the handout")

    def test_last_fifty(self):
        expect = fb.last_fifty_formatted
        BRIDGE_FORMATTED_COPY = copy.deepcopy(BRIDGE_FORMATTED)
        BRIDGE_FORMATTED_COPY = BRIDGE_FORMATTED[2731:]        
        bf.format_data(BRIDGE_FORMATTED_COPY)
        actual = BRIDGE_FORMATTED_COPY              
        self.assertEqual(expect, actual, "You should format data as described in the handout")
    
    '''def test_all_bridges(self):
        expect = fb.BRIDGE_FORMATTED_BACK_UP
        BRIDGE_FORMATTED_COPY = copy.deepcopy(BRIDGE_FORMATTED)
        bf.format_data(BRIDGE_FORMATTED_COPY)
        actual = BRIDGE_FORMATTED_COPY              
        self.assertEqual(expect, actual, "You should format data as described in the handout")'''        
    

class TestGetBridge(unittest.TestCase):
    def tes_invalid_case_1(self):
        expect = []
        actual = bf.get_bridge(BRIDGE_FORAMTTED_BACK_UP[1:50],0)
        self.assertEqual(expect, actual, "This is an invlaid id you should return an empty list")
    def test_invalid_case_2(self):
        expect = []
        actual = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,2900)
        self.assertEqual(expect, actual, "This gives an id out of bridges you should return an empty list")
    def test_first(self):
        expect = fb.first_fifty[0]
        actual = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,1)
        self.assertEqual(expect, actual, "You should return the bridge of id 1, this is your doctest, if you did not pass please also check the rest of your doctest")
    
    def test_middle_of_first_fifty(self):
        expect = fb.first_fifty[24]
        actual = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,25)
        self.assertEqual(expect, actual, "You should return the bridge of id 25")
    
    def test_first_fifty(self):
        expect = BRIDGE_FORMATTED_BACK_UP[0:50]
        actual = []
        for i in range(1,51):
            actual.append(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i))
        self.assertListEqual(expect, actual, "This test the list of first fifty bridges")
    
    def test_middle_of_last_fifty(self):
        expect = fb.last_fifty[24]
        actual = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, 2756)
        self.assertEqual(expect, actual, "You should return the bridge of id 2756")
        
    def test_last(self):
        expect = fb.last_fifty[-1]
        actual = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,2781)
        self.assertEqual(expect, actual, "You should return the last bridge")
    
    def test_last_fifty(self):
        expect = BRIDGE_FORMATTED_BACK_UP[2732:]
        actual = []
        for i in range(2733, 2782):
            actual.append(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i))
        self.assertListEqual(expect, actual, "This test the list of last fifty bridges")
    
    def test_all_bridges(self):
        expect = BRIDGE_FORMATTED_BACK_UP
        actual = []
        for i in range(1,2782):
            actual.append(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i))
        self.assertListEqual(expect, actual, "This test the list of whole bridges in the given data")


class TestAverageBci(unittest.TestCase):
    def test_invalid_case(self):
        expect = 0.0
        actual = bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP, 0)
        self.assertEqual(expect, actual, "This is an invlaid id, you should return 0.0")

    def test_invalid_case_2(self):
        expect = 0.0
        actual = bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP, 2999)
        self.assertEqual(expect, actual, "This is an invalid id, you should return 0.0")

    def test_id_607(self):
        expect = 0.0
        actual = bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP, 607)
        self.assertEqual(expect, actual, "This is only bridge which has 0.0 bci")

    def test_example_for_doctest(self):
        expect = 70.88571428571429
        actual = bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP,1)
        self.assertAlmostEqual(expect, actual, "This is the example for your doctest, if you did not pass please also check the rest of your doctest")
    
    def test_first_fifty(self):
        expect = fb.first_fifty_average
        actual = []
        for i in range(1,52):
            actual.append(bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP,i))
        self.assertListEqual(expect, actual, "This test the list of average bci you have from id 1 to 50")
    
    def test_middle_fifty(self):
        expect = fb.middle_fifty_average
        actual = []
        for i in range(950,1002):
            actual.append(bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP,i))
        self.assertListEqual(expect, actual, "This test the list of average bci you have from id 950 to id 1001")

    def test_last_fifty(self):
        expect = fb.last_fifty_average
        actual = []
        for i in range(2732,2782):
            actual.append(bf.get_average_bci(BRIDGE_FORMATTED_BACK_UP,i))
        self.assertListEqual(expect, actual, "This test the list of average bci you have from id2732 to id 2781")


class TestTotalLength(unittest.TestCase):
    def test_first_fifty(self):
        expect = 2291.9
        actual = bf.get_total_length_on_highway(fb.first_fifty,'403')
        self.assertAlmostEqual(expect, actual)

    def test_last_fifty_case_0(self):
        expect = 0.0
        actual = bf.get_total_length_on_highway(fb.last_fifty,'403')
        self.assertEqual(expect, actual, "there is no bridge in last fifty belong to 403 so you should return 0")
    
    def test_last_fifty_17(self):
        expect = 159.0
        actual = bf.get_total_length_on_highway(fb.last_fifty,'17')
        self.assertAlmostEqual(expect, actual)
    
    def test_middle_fifty_case_0(self):
        expect = 0.0
        actual = bf.get_total_length_on_highway(fb.middle_fifty,'17')
        self.assertAlmostEqual(expect, actual)
    
    def test_middle_fifty_403(self):
        expect = 1872.2000000000003
        actual = bf.get_total_length_on_highway(fb.middle_fifty,'403')
        self.assertAlmostEqual(expect, actual)    
    
    def test_fifty_to_hundred_417(self):
        expect = 1785.8000000000002
        actual = bf.get_total_length_on_highway(list(fb.fifty_to_hundred),'417')
        self.assertAlmostEqual(expect, actual)
    
    def test_all_bridges_17(self):
        expect = 8367.000000000002
        actual = bf.get_total_length_on_highway(BRIDGE_FORMATTED_BACK_UP,'17')
        self.assertAlmostEqual(expect, actual)
    
    def test_all_bridges_403(self):
        expect = 8964.500000000002
        actual = bf.get_total_length_on_highway(BRIDGE_FORMATTED_BACK_UP,'403')
        self.assertAlmostEqual(expect, actual)
    
    def test_all_bridges_417(self):
        expect = 11281.100000000006
        actual = bf.get_total_length_on_highway(BRIDGE_FORMATTED_BACK_UP,'417')
        self.assertAlmostEqual(expect, actual)


class TestFindClosetBridge(unittest.TestCase):
    def test_bridge3(self):
        expect = 2
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP[1:3],3)
        self.assertEqual(expect, actual, "There are only two bridges in the list no matted how far away you have to return the id beside 3")
    
    def test_bridge_random_two_id(self):
        expect = 917
        first_list = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,917)
        second_list = bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, 3)
        test_list = []
        test_list.append(first_list)
        test_list.append(second_list)
        actual = bf.find_closest_bridge(test_list,3)
        self.assertEqual(expect, actual, "There are randomly two list in the list no matted how far away you have to return the id beside 3")

    def test_bridge_3(self):
        expect = 1
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,3)
        self.assertEqual(expect, actual, "The brige 1 is the closest bridge to bridge 3")
    
    def test_bridge_6(self):
        expect = 8
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,6)
        self.assertEqual(expect, actual, "The brige 8 is the closest bridge to bridge 6")
    
    def test_bridge_7(self):
        expect = 8
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,7)
        self.assertEqual(expect, actual, "The brige 8 is the closest bridge to bridge 7")
    
    def test_bridge_8(self):
        expect = 7
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,8)
        self.assertEqual(expect, actual, "The brige 7 is the closest bridge to bridge 8")
    
    def test_bridge_9(self):
        expect = 7
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,9)
        self.assertEqual(expect, actual, "The brige 7 is the closest bridge to bridge 9")
    
    def test_bridge_10(self):
        expect = 1
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,10)
        self.assertEqual(expect, actual, "The brige 1 is the closest bridge to bridge 10")

    def test_bridge_2212(self):
        expect = 2221
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP[2200:2300], 2212)
        self.assertEqual(expect, actual, "The bridge 2221 is the closest one to 2212 between 2200 and 2300")

    def test_bridge_2212_in_2200_2220(self):
        expect = 2203
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP[2200:2220],2212)
        self.assertEqual(expect, actual, "The bridge 2221 is the closest one to 2212 between 2200 and 2300")

    def test_all_bridge_2212(self):
        expect = 2192
        actual = bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP,2212)
        self.assertEqual(expect, actual, "The bridge 2191 is the closest one to 2212 across all bridges")

    def test_first_fifty(self):
        expect = fb.first_fifty_closest
        actual = []
        for i in range(1,51):
            actual.append(bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP[0:50],i))
        self.assertListEqual(expect, actual,"This test the list of your first fifty bridges")
    
    def test_last_fifty(self):
        expect = fb.last_fifty_closest
        actual = []
        for i in range(2732,2782):
            actual.append(bf.find_closest_bridge(BRIDGE_FORMATTED_BACK_UP[2731:],i))
        self.assertListEqual(expect, actual, "This test the list of your last fifty bridges")

class TestFindBridgesInRadius(unittest.TestCase):
    def test_first_fifty_radius_1(self):
        expect = []
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP[:51],43.10, -80.15, 1)
        self.assertListEqual(expect, actual)

    def test_first_fifty_radius_10(self):
        expect = fb.first_fifty_radius_10
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP[:51],43.10, -80.15, 10)
        self.assertListEqual(expect, actual)

    def test_all_bridges_radius_10(self):
        expect = fb.first_fifty_radius_10
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP,43.10, -80.15, 10)
        self.assertListEqual(expect, actual)

    def test_first_fifty_radius_20(self):
        expect = fb.first_fifty_radius_20
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP[:51],43.10, -80.15, 20)
        self.assertListEqual(expect, actual)
    
    def test_first_fifty_radius_50(self):
        expect = fb.first_fifty_radius_50
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP[:51],43.10, -80.15, 50)
        self.assertListEqual(expect, actual)
    
    def test_middle_fifty_radius_5(self):
        expect = fb.middle_fifty_radius_5
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP[949:1001],43.556729, -79.60997, 5)
        self.assertListEqual(expect, actual)

    def test_middle_fifty_radius_10(self):
        expect = fb.middle_fifty_radius_10
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP[949:1001],43.556729, -79.60997, 10)
        self.assertListEqual(expect, actual)

    def test_all_bridges_radius_5(self):
        expect = [951, 952, 953, 954, 956, 957, 958, 959, 1039, 1040]
        actual = bf.find_bridges_in_radius(BRIDGE_FORMATTED_BACK_UP,43.556729, -79.60997, 5)
        self.assertListEqual(expect, actual)

class TestBridgesContaining(unittest.TestCase):
    def test_invalid_case(self):
        expect = []
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP, "Dinosaur")
        self.assertListEqual(expect, actual, "This is an invalid case and you should return an empty list")

    def test_first_fifty_underpass(self):
        expect = fb.first_fifty_underpass
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP[:51],"UndErPass")
        self.assertListEqual(expect, actual, "This test the list in first 50 contains underpass")

    def test_all_bridges_underpass(self):
        expect = fb.all_bridges_underpass
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP,"UndErPass")
        self.assertListEqual(expect, actual, "This test all of list in the data contain underpass")

    def test_first_fifty_highway(self):
        expect = [1]
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP[:50],"highWaY")
        self.assertListEqual(expect, actual, "This test the list in first 50 bridges contains highway")

    def test_all_bridges_highway(self):
        expect = fb.all_bridges_highway
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP,"highWaY")
        self.assertListEqual(expect, actual, "This test all of list in the data contain highway")
    
    def test_first_fifty_river(self):
        expect = fb.first_fifty_river
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP[:51],"river")
        self.assertListEqual(expect, actual, "This test first fifty bridges cotain river")

    def test_middle_fifty_river(self):
        expect = fb.middle_fifty_river
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP[949:1000],"river")
        self.assertListEqual(expect, actual)

    def test_last_fifty_river(self):
        expect = fb.last_fifty_river
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP[2731:2782],"river")
        self.assertListEqual(expect, actual)
    
    def test_all_bridges_river(self):
        expect = fb.all_bridges_river
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP,"river")
        self.assertListEqual(expect, actual) 
    
    def test_all_bridges_at(self):
        expect = fb.all_bridges_at
        actual = bf.get_bridges_containing(BRIDGE_FORMATTED_BACK_UP, "@")
        self.assertListEqual(expect, actual)
        

class TestAssignInspector(unittest.TestCase):
    def test_doctest_1(self):
        expect = [[45,55,56]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP,[[43.10, -80.15]], 3)
        self.assertListEqual(expect, actual)

    def test_doctest1_first_fifty(self):
        expect = [[45, 7, 12],[]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP[:50], [[43.10, -80.15],[38.691, -80.85]],3)
        self.assertListEqual(expect, actual)

    def test_doctest1_last_fifty(self):
        expect = [[2774, 2781],[]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP[2730:], [[43.10, -80.15],[38.691, -80.85]],3)
        self.assertListEqual(expect, actual)

    def test_doctest_2(self):
        expect = [[45, 55], [56, 64]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP,[[43.20, -80.35], [43.10, -80.15]], 2)
        self.assertListEqual(expect, actual)
    
    def test_doctest_3(self):
        expect = [[45, 55], [56, 64]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP, [[43.20, -80.35], [45.0368, -81.34]], 2)
        self.assertListEqual(expect, actual)
    
    def test_doctest_4(self):
        expect = [[919, 1420], [45, 55]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP, [[38.691, -80.85], [43.20, -80.35]], 2)
        self.assertListEqual(expect, actual)
    
    def test_doctest4_first_fifty(self):
        expect = [[]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP[:50], [[38.691, -80.85]],3)
        self.assertListEqual(expect, actual)
    
    def test_doctest4_last_fifty(self):
        expect = [[]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP[2730:], [[38.691, -80.85]],3)
        self.assertListEqual(expect, actual)

    def test_case_5(self):
        expect = [[919,1420]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP, [[38.691, -80.85]],3)
        self.assertListEqual(expect, actual, "There are only two bridges across all bridges are qualified")        

    def test_case_6(self):
        expect = [[919, 1420], [45, 55, 56], [64, 101, 113]]
        actual = bf.assign_inspectors(BRIDGE_FORMATTED_BACK_UP, [[38.691, -80.85], [43.556729, -79.60997],[43.20, -80.35]], 3)
        self.assertListEqual(expect, actual)

class TestGetDistanceBetween(unittest.TestCase):
    def test_first_fifty(self):
        expect = fb.first_fifty_distance
        actual = []
        for i in range(1,50):
            actual.append(bf.get_distance_between(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i),bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, i+1)))
        self.assertListEqual(expect, actual)

    def test_first_fifty_to_2212(self):
        expect = fb.first_fifty_2212
        actual = []
        for i in range(1,51):
            actual.append(bf.get_distance_between(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i),bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,2212)))
        self.assertListEqual(expect, actual)

    def test_last_fifty(self):
        expect = fb.last_fifty_distance
        actual = []
        for i in range(2731, 2781):
            actual.append(bf.get_distance_between(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i),bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, i+1)))
        self.assertListEqual(expect, actual)
    
    def test_last_fifty_2212(self):
        expect = fb.last_fifty_2212
        actual = []
        for i in range(2731, 2782):
            actual.append(bf.get_distance_between(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i),bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, 2212)))
        self.assertListEqual(expect, actual)

    def test_all_bridges(self):
        expect = fb.all_distance
        actual = []
        for i in range(1,2781):
            actual.append(bf.get_distance_between(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i),bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, i+1)))
        self.assertListEqual(expect, actual)
    
    def test_all_bridges_2212(self):
        expect = fb.all_bridges_2212
        actual = []
        for i in range(1,2782):
            actual.append(bf.get_distance_between(bf.get_bridge(BRIDGE_FORMATTED_BACK_UP,i),bf.get_bridge(BRIDGE_FORMATTED_BACK_UP, 2212)))
        self.assertListEqual(expect, actual)        

class TestGetAverageBciBelow(unittest.TestCase):
    def test_empty_list(self):
        expect = []
        actual = bf.get_bridges_with_bci_below(BRIDGE_FORMATTED_BACK_UP, [1,2781],10)
        self.assertListEqual(expect, actual)

    def test_bci_10(self):      
        expect = [607,1282,1528,1625,2715]
        ids = []
        for i in range(1,2781):
            ids.append(i)
        actual = bf.get_bridges_with_bci_below(BRIDGE_FORMATTED_BACK_UP,ids,10)
        self.assertListEqual(expect, actual, "This test the list of all bridges have bci under 10")
    
    def test_bci_first_fifty_65(self):
        expect = [32,45]
        actual = bf.get_bridges_with_bci_below(BRIDGE_FORMATTED_BACK_UP, [1,32,33,44,45,60],65)
        self.assertListEqual(expect, actual, "This test test a sample that may contain the bci lower than 65")

    def test_bci_first_fifty_72(self):
        ids = []
        for i in range(1,51):
            ids.append(i)
        expect = [2, 3, 5, 7, 8, 9, 11, 12, 13, 32, 39, 45, 48, 49]
        actual = bf.get_bridges_with_bci_below(BRIDGE_FORMATTED_BACK_UP,ids,72)
        self.assertListEqual(expect, actual, "This test bridges have bci under 72 between id40 and id50")

    def test_bci_forty_fifty_72(self):
        ids = []
        for i in range(40,51):
            ids.append(i)
        expect = [45,48,49]
        actual = bf.get_bridges_with_bci_below(BRIDGE_FORMATTED_BACK_UP,ids,72)
        self.assertListEqual(expect, actual, "This test bridges have bci under 72 between id40 and id50")
    
    def test_bcis_all_45(self):
        ids = []
        for i in range(1,2782):
            ids.append(i)
        expect = [607, 898, 1277, 1282, 1528, 1625, 2177, 2193, 2643, 2685, 2687, 2715]
        actual = bf.get_bridges_with_bci_below(BRIDGE_FORMATTED_BACK_UP,ids,45)
        self.assertListEqual(expect, actual, "This test bridges have bci under 45 across all bridges")        

class TestInspectBridges(unittest.TestCase):
    def test_first_bridge(self):
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,[1],"10/23/2018",12.20)
        expect = True
        actual = bf.get_bridge(bridge_copy,1)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,1)[bf.BCIS_INDEX][0] == 12.20
        self.assertEqual(expect, actual)

    def test_last_bridge(self):
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,[2781],"10/23/2018",12.20)
        expect = True
        actual = bf.get_bridge(bridge_copy,2781)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,2781)[bf.BCIS_INDEX][0] == 12.20
        self.assertEqual(expect, actual)

    def test_first_and_last(self):
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,[2781,1],"10/23/2018",12.20)
        expect = True
        actual = bf.get_bridge(bridge_copy,1)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,1)[bf.BCIS_INDEX][0] == 12.20 and  bf.get_bridge(bridge_copy,2781)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,2781)[bf.BCIS_INDEX][0] == 12.20
        self.assertEqual(expect, actual)
    
    def test_first_fifty_random_three(self):
        ids = random.sample(range(1,51),3)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,ids,"10/23/2018",12.20)
        expect = 3
        acc = 0
        for bridge_id in range(1,51):
            if(bf.get_bridge(bridge_copy,bridge_id)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,bridge_id)[bf.BCIS_INDEX][0] == 12.20 and bridge_id in ids):
                acc += 1
        self.assertEqual(expect, acc)
    
    def test_last_fifty_random_three(self):
        ids = random.sample(range(2732,2781),3)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,ids,"10/23/2018",12.20)
        expect = 3
        acc = 0
        for bridge_id in range(2732,2781):
            if(bf.get_bridge(bridge_copy,bridge_id)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,bridge_id)[bf.BCIS_INDEX][0] == 12.20 and bridge_id in ids):
                acc += 1
        self.assertEqual(expect, acc)        
    
    def test_all_odd_bridges(self):
        ids = []
        for i in range(1,2782,2):
            ids.append(i)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,ids,"10/23/2018",12.20)
        expect = 1391
        acc = 0
        for bridge_id in range(1,2782):
            if(bf.get_bridge(bridge_copy,bridge_id)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,bridge_id)[bf.BCIS_INDEX][0] == 12.20 and bridge_id % 2 == 1):
                acc += 1
        self.assertEqual(expect, acc)
    
    def test_all_even_bridges(self):
        ids = []
        for i in range(2,2782,2):
            ids.append(i)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,ids,"10/23/2018",12.20)
        expect = 1390
        acc = 0
        for bridge_id in range(1,2782):
            if(bf.get_bridge(bridge_copy,bridge_id)[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bf.get_bridge(bridge_copy,bridge_id)[bf.BCIS_INDEX][0] == 12.20 and bridge_id % 2 == 0):
                acc += 1
        self.assertEqual(expect, acc)
    
    def test_all_bridges(self):
        ids = []
        for i in range(1,2782):
            ids.append(i)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,ids,"10/23/2018",12.20)
        expect = 2781
        acc = 0
        for bridge in bridge_copy:
            if bridge[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bridge[bf.BCIS_INDEX][0] == 12.20:
                acc += 1
        self.assertEqual(expect, acc)
    
    def test_all_bridges_random_three(self):
        ids = random.sample(range(1,2781),3)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        bf.inspect_bridges(bridge_copy,ids,"10/23/2018",12.20)
        expect = 3
        acc = 0
        for bridge in bridge_copy:
            if bridge[bf.LAST_INSPECTED_INDEX] == "10/23/2018" and bridge[bf.BCIS_INDEX][0] == 12.20:
                acc += 1
        self.assertEqual(expect, acc)        

class TestAddRehab(unittest.TestCase):
    def test_first_fifty_random_three(self):
        ids = random.sample(range(1,51),3)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        for bridge_id in ids:
            bf.add_rehab(bridge_copy, bridge_id,"12/20/2018",True)
        expect = 3
        acc = 0
        for i in range(1,51):
            bridge = bf.get_bridge(bridge_copy,i)
            if bridge[bf.LAST_MAJOR_INDEX] == "12/20/2018" and i in ids:
                acc += 1
        self.assertEqual(expect, acc) 

    def test_last_fifty_random_three(self):
        ids = random.sample(range(2732,2782),3)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        for bridge_id in ids:
            bf.add_rehab(bridge_copy, bridge_id,"12/20/2018",False)
        expect = 3
        acc = 0
        for i in range(2732,2782):
            bridge = bf.get_bridge(bridge_copy,i)
            if bridge[bf.LAST_MINOR_INDEX] == "12/20/2018" and i in ids:
                acc += 1
        self.assertEqual(expect, acc)

    def test_all_bridges_random_three(self):
        ids = random.sample(range(1,2782),3)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        for bridge_id in ids:
            bf.add_rehab(bridge_copy, bridge_id,"12/20/2018",True)
        expect = 3
        acc = 0
        for bridge in bridge_copy:
            if bridge[bf.LAST_MAJOR_INDEX] == "12/20/2018":
                acc += 1
        self.assertEqual(expect, acc)

    def test_all_bridges_true(self):
        ids = []
        for i in range(1,2782):
            ids.append(i)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        for bridge_id in ids:
            bf.add_rehab(bridge_copy, bridge_id,"12/20/2018",True)
        expect = 2781
        acc = 0
        for bridge in bridge_copy:
            if bridge[bf.LAST_MAJOR_INDEX] == "12/20/2018":
                acc += 1
        self.assertEqual(expect, acc)

    def test_all_bridges_false(self):
        ids = []
        for i in range(1,2782):
            ids.append(i)
        bridge_copy = copy.deepcopy(BRIDGE_FORMATTED_BACK_UP)
        for bridge_id in ids:
            bf.add_rehab(bridge_copy, bridge_id,"12/20/2018",False)
        expect = 2781
        acc = 0
        for bridge in bridge_copy:
            if bridge[bf.LAST_MINOR_INDEX] == "12/20/2018":
                acc += 1
        self.assertEqual(expect, acc)    
if __name__ == "__main__":
    unittest.main(exit = False)