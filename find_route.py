########################################################################################
#Author: Avinash Shanker
#UTA ID: 1001668570
#Date: 30-Jan-2019
########################################################################################
#Usage Information
#For Uninformed Search
#python find_route.py input1.txt Bremen Kassel
#For Informed Search with heuristic Data
#python find_route.py input1.txt Bremen Kassel h_kassel.txt
########################################################################################

#Import Libraries
from collections import deque
import sys

#Configuration and Initializations
File_End = 'END OF INPUT'
Pathes = []
Expanded = []
Heuristic = []

#This Function is used to read the user input file and store it as list of array
#Storing each path as both forward and reverse paths so that they have same distance
def Setup_Map():
	input_file = sys.argv[1]
	Data_File = open(input_file)
	for Row in Data_File:
		if File_End not in Row:
			City = Row.split()
			Origin = City[0]
			Dest = City[1]
			Dist = City[2]
			F_Path = [Origin, Dest, Dist]
			Pathes.append(F_Path)
			R_Path = [Dest, Origin, Dist]
			Pathes.append(R_Path)
			
		else:
			break
	return Pathes		

#This function parses and stores heuristic file given by user
#Heuristic value is added to Total cost of the city location
def Setup_Heuristic():
	heuristicfile = sys.argv[4]
	Heu_File = open(heuristicfile)
	for Row in Heu_File:
	    if File_End not in Row:
	    	heuristic = Row.split()
	    	hcity = heuristic[0]
	    	hvalue = heuristic[1]
	    	Heuristic.append([hcity, hvalue])
	    else:
	    	break
	return Heuristic  
	
#Class is invoked to perform uninformed search
#I am using only f(n) value to complete the path
class USearch:
    def Parse_Node(self, Start_City, Goal_City):
        Pathes = Setup_Map()
        Fringe = deque()
        Fringe.append(Create_Nd(Start_City, 0, 0))
        ExpNode = 0
        NotInRange = 0

        while 1:
            if len(Fringe) != 0:
                Nd_Expd = Fringe.popleft()
                ExpNode = ExpNode + 1
                if Nd_Expd.name == Goal_City:
                    break
                else:
                    if Nd_Expd.name not in Expanded:
                        Expanded.append(Nd_Expd.name)
                        for Data in Pathes:
                            if Data[0] == Nd_Expd.name:
                                cost = Nd_Expd.Total_Cost+int(Data[2])
                                us = Create_Nd(Data[1], cost, Nd_Expd.d+1)
                                us.parents= Nd_Expd
                                Fringe.append(us)
                                US_Sorted=sorted(Fringe, key=lambda Create_Nd:Create_Nd.Total_Cost)
                                Fringe=deque(US_Sorted)
            else:
                NotInRange = 1
                break
        if(NotInRange == 1):
        	Print_Infinity(ExpNode)

        else:
            print ("nodes expanded: " , str(ExpNode))
            print ("distance: " , str(Nd_Expd.Total_Cost))
            print ("route: ")
            path = []
            path.append(Goal_City)
            while Nd_Expd.parents != None:
                path.append(Nd_Expd.parents.name)
                Nd_Expd = Nd_Expd.parents
            path.reverse()
            Loc=0
            while Loc < len(path)-1:
                for Trace in Pathes:
                    if path[Loc] == Trace[0] and path[Loc + 1] == Trace[1]:
                        print (Trace[0], "to", Trace[1] + ",", Trace[2] + "km")
                Loc = Loc + 1


#Function is invoked to print when the distance between two path is infinity
def Print_Infinity(ExpNode):
	print ("nodes expanded:", str(ExpNode))
	print ("distance: infinity")
	print ("route:\nnone")

#Informed search class calls Setup_Heuristic function inside parse node
#All the pathes are setup by Setup_Map() funtion
#When compared to Uniformed search heuristic value is also added while i.e. f(n)+g(n)
class ISearch:
    def Parse_Node(self, Start_City, Goal_City):
        Fringe = deque()
        Pathes = Setup_Map()
        Heuristic = Setup_Heuristic()
        Fringe.append(Create_Nd(Start_City, 0, 0))
        ExpNode=0
        NotInRange = 0
        while 1:
            if len(Fringe) != 0:
                Nd_Expd = Fringe.popleft()
                ExpNode += 1
                if Nd_Expd.name == Goal_City:
                    break
                else:
                    if Nd_Expd.name not in Expanded:
                        Expanded.append(Nd_Expd.name)
                        for Data in Pathes:
                            if Data[0] == Nd_Expd.name:
                                for huer in Heuristic:
                                    if huer[0] == Data[1]:
                                        heuristicvalue=huer[1]

                                Add_Hue = Nd_Expd.Total_Cost + int(Data[2]) + int(heuristicvalue)
                                Cost = Nd_Expd.Total_Cost + int(Data[2])
                                Is_Cost = Create_Nd(Data[1], Cost , Add_Hue)
                                Is_Cost.parents= Nd_Expd
                                Fringe.append(Is_Cost)
                                IS_Sorted=sorted(Fringe, key=lambda Create_Nd:Create_Nd.d)
                                Fringe=deque(IS_Sorted)
            else:
                NotInRange = 1
                break
        if(NotInRange == 1):
        	Print_Infinity(ExpNode)
        	
        else:
            print ("nodes expanded: " , str(ExpNode))
            print ("distance: " , str(Nd_Expd.Total_Cost))
            print ("route: ")
            path = []
            path.append(Goal_City)
            while Nd_Expd.parents != None:
                path.append(Nd_Expd.parents.name)
                Nd_Expd = Nd_Expd.parents
            path.reverse()
            Loc=0
            while Loc < len(path) - 1:
                for Trace in Pathes:
                    if path[Loc] == Trace[0] and path[Loc + 1] == Trace[1]:
                        print (Trace[0], "to", Trace[1] + ",", Trace[2] + "km")
                Loc = Loc + 1

#Function to create node and keep track of parents and cost
class Create_Nd:
    def __init__(self, name, Total_Cost, d):
        self.name = name
        self.parents = None
        self.Total_Cost = Total_Cost
        self.d = d

#Main function where based on the number of arguments USearch or ISearch is perfomed
def main():
	source = sys.argv[2]
	destination = sys.argv[3]
	if len(sys.argv) > 4:
		setter = ISearch()
	else:
		setter = USearch()
	setter.Parse_Node(source,destination)

if __name__ == "__main__":
    main()



    
