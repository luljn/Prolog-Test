import pyswip

prolog = pyswip.Prolog()
prolog.consult("main.pl")

result = prolog.query("programmeur(X)")

for sol in result :
    print(sol['X'])