#! /usr/bin/python2.7

input_path = "../benchmark/"

bench = ["compress95", "go"]
argu = ["ialu", "imult", "memport", "fpalu", "fpmult"]
value = ["1", "2", "4", "8", "16"]
out = ["ipc", "time"]
s = set()

def empty_file(filename):
    fp = open(filename, 'w')
    fp.close()

def deal(input_file, output_suffix):
    fp = open(input_file, 'r')
    for line in fp.readlines():
        array = line.split()
        if len(array) > 1:
            if array[0] == 'sim_IPC':
                output_ipc = input_path + "ipc." + output_suffix
                if output_ipc not in s:
                    s.add(output_ipc)
                    empty_file(output_ipc)
                fp_out_ipc = open(output_ipc, 'a')
                fp_out_ipc.write("1"+"\t"+array[1]+"\n")
                fp_out_ipc.close()
            if array[0] == 'sim_elapsed_time':
                output_time = input_path + "time." + output_suffix
                if output_time not in s:
                    s.add(output_time)
                    empty_file(output_time)
                fp_out_time = open(output_time, 'a')
                fp_out_time.write("1"+"\t"+array[1]+"\n")
                fp_out_time.close()


if __name__ == "__main__":
    for ben in bench:
        for arg in argu:
            for val in value:
                file_in = input_path+ben+"."+arg+"."+val
                file_out = arg+"."+ben
                deal(file_in, file_out)
