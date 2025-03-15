import pprint
import pickle

def read_data_info():
    with open("/tmp/data_info.pkl", "rb") as file:
        data = pickle.load(file)
        for each_data in data:
            print("Presence Condition: " + each_data[1], end=" ")
            print("Associated: " + str(len(each_data[0])))
            print("--------------------------------------------")

            

def read_pq():
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        print("Size: " + str(len(pqeue)))
        for each in pqeue:
            print("--------------------------------------------")
            print("Energy: " + str(each[0]) + " PC: " + each[1])
            trace = each[2]
            for idx, bit in enumerate(trace):
                if bit != 0:
                    # print("Bit: " + str(idx), end=" ")
                    pass
            print("\n")


def main():
    read_data_info()
    # read_pq()
    
if __name__ == "__main__":
    main()