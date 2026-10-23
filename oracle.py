import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def rolls(n, b):
    k = -(-n//b)
    return f"The {pl(n,' banner',' banners')} at {pl(b,' banner',' banners')} a roll {v(n,'takes','take')} {pl(k,' roll',' rolls')}, the last roll holding {pl(n-(k-1)*b,' banner',' banners')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' banner',' banners')} at {pl(w,' banner',' banners')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' banner',' banners')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' roll',' rolls')} at ${m(pc)} a roll {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a banner."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' banner',' banners')} at {pl(pm,' banner',' banners')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(781)
R = random.randint
cases = [
 dict(fn="rolls", args=["260","12"], expect=rolls(260,12)),
 dict(fn="weeks", args=["260","30"], expect=weeks(260,30)),
 dict(fn="cost", args=["22","41.25","260"], expect=cost(22,4125,260)),
 dict(fn="time", args=["260","5"], expect=time_(260,5)),
 dict(fn="rolls", args=["1","1"], expect=rolls(1,1)),
 dict(fn="rolls", args=["252","12"], expect=rolls(252,12)),
 dict(fn="rolls", args=["1000000","1000"], expect=rolls(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["240","30"], expect=weeks(240,30)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="rolls", args=[str(n),str(b)], expect=rolls(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["rolls",["0","12"]],["rolls",["1000001","12"]],["rolls",["2.5","12"]],["rolls",["260","0"]],["rolls",["260","1001"]],
 ["weeks",["0","30"]],["weeks",["260","0"]],["weeks",["260","100001"]],["weeks",["260","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","41.25","260"]],["cost",["100001","41.25","260"]],["cost",["22","0","260"]],["cost",["22","41.255","260"]],["cost",["22","41.25","0"]],
 ["time",["0","5"]],["time",["260","0"]],["time",["260","101"]],["time",["260","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
