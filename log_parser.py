import re
print("WARNINGS:")
with open("./data/rsvp_agent_log.dat", "r+")as dat_file:
    for line in dat_file:
        match = re.search('WARNING', line)
        if match is None:
            pass
        else:
            print(str(line[0:14]) + " -- " + str(line[45:]))
