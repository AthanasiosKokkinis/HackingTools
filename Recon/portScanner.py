import socket
import threading

def scan_port_range(hostname, port_range, verbose = False, output = None):
    target_ip = socket.gethostbyname(hostname)
    scanning_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(port_range[0],port_range[-1]+1):
        try:
            result = scanning_socket_tcp.connect_ex((target_ip,port))
            if result == 0:
                try:
                    banner = scanning_socket_tcp.recv(1024).decode()
                except:
                    banner = "NO SERVICE"

                if(verbose):
                    print("Port {} is open, running: {}".format(port,banner))
                
                if(output):
                    with open(output,"a") as output_file:
                        output_file.write("Port {} is open, running: {}".format(port,banner))
                scanning_socket_tcp
            else:
                continue
        except:
            pass

def divide_port_range(port_range, num_threads):
    a = [*range(port_range[0],port_range[1]+1,1)]
    k, m = divmod(len(a),num_threads)
    return list((a[i*k+min(i, m):(i+1)*k+min(i+1,m)] for i in range(num_threads)))

def main(target_name, port_range, num_of_threads, verbose = False, output = None):
    port_arrays = divide_port_range(port_range,num_of_threads)
    #print(port_arrays)
    for i in range(0,num_of_threads):
        #print(port_arrays[i])
        thread = threading.Thread(target = scan_port_range, args=[target_name,port_arrays[i],verbose,output])
        thread.start()

target_ip = ""
min_port = 0
max_port = 1000
port_range = [min_port, max_port]
num_threads = 3
verbose = True
output_file = "output.txt"
main(, port_range, num_threads, verbose, output_file)
