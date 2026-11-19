# Karl 19.11.26

# Ülesanne 3.6: Python Turtle ruut
import turtle

kylje_pikkus = 100
nurk = 90
varv = "red"
edasi = kylje_pikkus

turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)

edasi = edasi * 1.5
turtle.up()
turtle.goto(edasi, 0)
turtle.down()

turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)

edasi = edasi * 2
turtle.up()
turtle.goto(edasi, 0)
turtle.down()

turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)


turtle.done()



# Ülesanne 3.4: Lemmikraamat
raamatu_pealkiri  = "Suvi"
raamatu_autor = "Oskar Meri"
raamat = raamatu_pealkiri+" "+raamatu_autor
lk = 300
skoor = 10.0

print("Minu lemmikraamat on "+raamat+" Eno Raud , mis on "+str(lk)+" lehekülge pikk ja mille ma hindan "+str(skoor)+" punktiga.")


# Ülesanne 3.2: Ostunimekiri
toode = "juust"
kogus = 50
hind = 15.50

print("Soovin "+toode+" "+str(kogus)+", mille tüki hind on "+str(hind)+" eurot.")


