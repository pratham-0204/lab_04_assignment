class flight:
    def __init__(self):
        self.fli = []
    def addflight(self , location , team1 , team2 , time):
        self.fli.append(
            {
                "match location":location,
                "team 01" : team1,
                "team 02": team2,
                "time" : time 
            }
        )
    def showteam(self , name):
        steam = []
        for i in self.fli:
            if(name in i["team 01"] or ["team 02"]):
                steam.append(i)
            
        return steam
    def showlocation(self , locat):
        slocat = []
        for i in self.fli:
            if(locat in i["match location"]):
                slocat.append(i)
        return slocat
    def showtime(self , tim):
        stime = []
        for i in self.fli:
            if(tim in i["time"]):
                stime.append(i)
        return stime
    def display(self , match):
        for i in match:
            print("------------------------------------------------------------------------")
            print( "Match location :", i["match location"])
            print("team 01 :",i["team 01"]  )
            print("team 02 :",i["team 02"]  )
            print("time :",i["time"])

fli = flight()

fli.addflight("Mumbai", "India", "Sri Lanka", "DAY")
fli.addflight("Delhi", "England", "Australia", "DAY-NIGHT")
fli.addflight("Chennai", "India", "South Africa", "DAY")
fli.addflight("Indore", "England", "Sri Lanka", "DAY-NIGHT")
fli.addflight("Mohali", "Australia", "South Africa", "DAY-NIGHT")
fli.addflight("Delhi", "India", "Australia", "DAY")

while True:
    print("Search Options:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        t = input("Enter the team name : ")
        m = fli.showteam(t)
        fli.display(m)
    if(choice == 2):
        t = input("Enter the location : ")
        m = fli.showlocation(t)
        fli.display(m)
    if(choice == 3):
        t = input("Enter the timing : ")
        m = fli.showtime(t)
        fli.display(m)
    else:
        break

