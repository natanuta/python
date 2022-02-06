
def dbg(txt):
    print(txt)

def read_file (filename):
    with open(filename) as f:
        #lines = f.readlines()
        lines = [x.rstrip() for x in f]  # remove line breaks
    return lines

class WorkingDay():

    def __init__(self, start,  end):
        self.start = start
        self.end = end
        self.totalmins = self.calculate_working_hours (self.start,self.end)

    @classmethod
    def calculate_working_hours(self, start, end):
         hourmin1 = start.split(":")
         start_mins = int(hourmin1[0])*60 + int(hourmin1[1])

         hourmin2 = end.split(":")
         end_mins = int(hourmin2[0]) * 60 + int(hourmin2[1])

         return (end_mins - start_mins)


class WorkingMonth():
    def __init__(self):
        self.dayCnt = 1
        self.isHolyday = false

def add_day_to_month(day):
    pass

if __name__ == '__main__':

    l1 = read_file("hours1.txt")

    for item in l1:
        x = item.split (",")
        day = WorkingDay((x[0]), (x[1]))
        add_day_to_month (day)
        print (day.start)
        print(day.end)
        print ("Total work in minutes: ", day.totalmins)








