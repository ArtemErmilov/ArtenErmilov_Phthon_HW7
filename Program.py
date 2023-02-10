


from os import system

from View import View

from CalcRN import CalcRN

from Presenter import Presenter


system ('cls')



v= View

c=CalcRN()

d = Presenter(c,v)

d.buttonClic()
