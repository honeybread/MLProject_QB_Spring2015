from csv import DictReader
import math

# given two coordinates, this function returns a speed 
speed = lambda (x1,y1),(x2,y2): math.sqrt(((x2-x1)**2+(y2-y1)**2))
# given a list of coordinates, this function returns the total length of a trip
trip_length = lambda x_y: sum([speed(x_y[e],x_y[e+1]) for e in xrange(len(x_y)) if e < len(x_y)-1])

class DataManipulation(object):
    def __init__(self, filepath):
        self.filepath = filepath    
        
    def data_import(self):
        # input: the location of .csv file as a string. E.g."drivers/1/1.csv"
        # output: a list of tuple, [(x1,y1),(x2,y2),....]
        for driver in drivers:
            for trip in driver:
                data = list(DictReader(open(self.filepath,"r")))
                x_y = [(float(e["x"]),float(e["y"])) for e in data]
        return x_y

    def data_dump(self):
        
        
    def main():
        filename = "drivers/1/1.csv" # change this as you need to
        x_y = data_import(filename)
        print speed(x_y[0],x_y[1])
        print trip_length(x_y)
     
    def data_plot():
        # output: a list of tuple, [(x1,y1),(x2,y2),....]
        data = list(DictReader(open(filename,"r")))
        x = [(float(e["x"])) for e in data]
        y = [(float(e["y"])) for e in data]
        return x,y
        	


if __name__ == "__main__":
	main()