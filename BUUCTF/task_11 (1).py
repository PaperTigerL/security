from Crypto.Util.number import *
import gmpy2
from flag import flag
def gen_prime(number):
    p = getPrime(number//2)
    q = getPrime(number//2)
    return p,q

m = bytes_to_long(flag.encode())
p,q = gen_prime(1024)
print(p*q)
e = 65537
d = gmpy2.invert(e,(p-1)*(q-1))
print(d%(p-1))
print(pow(m,e,p*q))
# 93172788492926438327710592564562854206438712390394636149385608321800134934361353794206624031396988124455847768883785503795521389178814791213054124361007887496351504099772757164211666778414800698976335767027868761735533195880182982358937211282541379697714874313863354097646233575265223978310932841461535936931
# 307467153394842898333761625034462907680907310539113349710634557900919735848784017007186630645110812431448648273172817619775466967145608769260573615221635
# 52777705692327501332528487168340175436832109866218597778822262268417075157567880409483079452903528883040715097136293765188858187142103081639134055997552543213589467751037524482578093572244313928030341356359989531451789166815462417484822009937089058352982739611755717666799278271494933382716633553199739292089
