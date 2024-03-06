import socket

openFile = input("File to Read: ")
hostsFile = open(openFile, "r")
for line in hostsFile.readlines():
    line = line.strip("\n")
    try:
        ip = socket.gethostbyname(line)
        print("Valid: {0} ({1})".format(ip, line))
    except Exception as e:
        print("Invalid: {0} (N/A)".format(line))
