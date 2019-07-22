import pickle

source = open("../../links.txt", "r")
dest = open("DATA/LINKS/init_links_dt=2019-07-21.pkl", 'wb')

links = set()
for line in source:
    links.add(line)
pickle.dump(links, dest)
