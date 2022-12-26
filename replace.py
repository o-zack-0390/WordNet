from copy import copy

def read_file(path):
    f     = open(path, 'r', encoding="utf-8", newline="")
    line  = f.readline()
    list  = []
    
    while line:
        line       = line_replace(line)
        line       = line.split(':')
        list.append(line)
        line       = f.readline()
        
    f.close()
    return list
    
    
def line_replace(line):
    line = line\
    .replace("\n", '')\
    .replace("\r", '')\
    .replace(' ','')
    
    return line
    
    
def write_file(path):
    global list
    
    f    = open(path, 'w', encoding="utf-8", newline="")
    prev = list[0]
    size = len(list)
    
    for i in range(1,size):
        this = list[i]
        
        if prev[0] != this[0]:
            f.write(prev[0]+':'+prev[1]+"\n")
            
        prev = this
    
    f.close()
    
    
path1 = "data2/topic-news/up_entity.txt"
path2 = "data2/topic-news/up_entity_2.txt"
list  = copy(read_file(path1))
write_file(path2)

'''
cd reserch\AI\AI_models\knn\wordnet
python p.py

path1 = "data/dokujo-tsushin/up_entity.txt"
path2 = "data/dokujo-tsushin/up_entity_2.txt"

path1 = "data/it-life-hack/up_entity.txt"
path2 = "data/it-life-hack/up_entity_2.txt"

path1 = "data/kaden-channel/up_entity.txt"
path2 = "data/kaden-channel/up_entity_2.txt"

path1 = "data/livedoor-homme/up_entity.txt"
path2 = "data/livedoor-homme/up_entity_2.txt"

path1 = "data/movie-enter/up_entity.txt"
path2 = "data/movie-enter/up_entity_2.txt"

path1 = "data/peachy/up_entity.txt"
path2 = "data/peachy/up_entity_2.txt"

path1 = "data/smax/up_entity.txt"
path2 = "data/smax/up_entity_2.txt"

path1 = "data/sports-watch/up_entity.txt"
path2 = "data/sports-watch/up_entity_2.txt"

path1 = "data/topic-news/up_entity.txt"
path2 = "data/topic-news/up_entity_2.txt"
'''
