import sys
import unidecode

def is_valid(k):
    for c in k:
        if ord(c) < ord("a") or ord(c) > ord("z"):
            return False
    return True

def anagram_key(w):
    w_clean = w.replace("\u00b7", "").replace("-", "")
    return ''.join(sorted(unidecode.unidecode(w_clean).lower()))

def dumpsql(fname):
    d = {}

    with open(fname, "r") as f:
        l = f.readline()
        i = 1
        while l:
            w = l.strip()
            
            if not w:
                break
                
            k = anagram_key(w)
            
            if is_valid(k):
                try:
                    d[k].append(w)
                except KeyError:
                    d[k] = [w]

            l = f.readline()
            i += 1
    #print("Total keys: %d" % (len(d)))
    
    #print("LOCK TABLES `words` WRITE;")
    for k, ws in d.items():
        for w in ws:
            print("INSERT INTO `words` VALUES (NULL,'%s','%s');" % (k, w));
    #print("UNLOCK TABLES;")

dumpsql(sys.argv[1])

