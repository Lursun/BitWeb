
class Block :
    def mining():
        diff=1208125050997691315695083670915326931193237982586303531011003759538765426933086993686190125157774847635054139742454124580793690027707505268472099701
        while True:
            start=time()
            s=str(random())
            print ("strat",s)
            while stop:
                time1m=(s+str(random()))
                out=int(hashlib.sha512(time1m).hexdigest(),16)
                if out < p:
                    break
            end=time()
            print("end",end-start)
            return end-start
        