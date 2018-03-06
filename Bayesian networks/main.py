from tkinter.filedialog import askopenfilename
import re
import bayesianNetwork as bn

filename = askopenfilename()
rules = open(filename).readlines()
patron = re.compile('[P|p]\(([a-zA-Z](["|",","][a-zA-Z])*)\)\=[0-1]\.[0-9]*')
validation = [patron.match(line) for line in rules]
if(validation):
    t = bn.bayesianNetwork(rules)
    t.factors(rules)