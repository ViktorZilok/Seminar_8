import model as md
import view as v

def button():
    x = v.get()
    md.init()
    result = md.calc(x)
    v.view(result)

