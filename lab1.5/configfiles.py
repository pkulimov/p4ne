import glob

folder = "/home/pkulimov/Seafile/p4ne_training/config_files/"
result = set()

for txt_file in glob.iglob("/home/pkulimov/Seafile/p4ne_training/config_files/*.txt"):
    with open(txt_file, "r") as file:
        for line in file:
            if line.find("ip address") > 0:
                result.add(line.replace("ip address", "").strip())

for line in result:
    print(line)
