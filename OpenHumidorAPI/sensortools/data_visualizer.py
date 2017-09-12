#!/usr/bin/python
import pylab as plt
import sys

def safe_select(start, end):
    entry = start-1
    while entry<start or entry>end:
        try:
            entry = int(raw_input("{}-{}?".format(start, end)))
        except ValueError:
            pass
    return entry

class DataVisualizer(object):
    def __init__(self, fn):
        self.fn = fn

    def load_data(self, xind, yind):
        x_data, y_data = [], []
        with open(self.fn) as f:
            for line in f.readlines():
                x_data.append(line.split(",")[xind])
                y_data.append(line.split(",")[yind])
        return x_data, y_data

    def visualize(self):
        with open(self.fn) as f:
            hintline = f.readline().split(",")
        print("The selected file has {} fields"
              "in the following format:".format(len(hintline)))
        print "\n".join(["{}: {}".format(num, hint) for (num, hint) in zip(range(len(hintline)), hintline)])
        print "Please select the data row for the x-axis:"
        ind_x = safe_select(0, len(hintline))
        print "Please select the data row for the y-axis:"
        ind_y = safe_select(0, len(hintline))
        _x, _y = self.load_data(ind_x, ind_y)
        label = raw_input("Type a label for the data: ")
        if label:
            plt.plot(_x, _y, label=label)
            plt.legend()
        else:
            plt.plot(_x, _y)

    def run(self):
        plt.ion()
        while raw_input("Plot another field? (y/n)") == "y":
            self.visualize()

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print "Please provide a filename !"
    else:
        vis = DataVisualizer(sys.argv[1])
        vis.run()
