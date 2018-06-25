from collections import *
from random import *
import time

def train_char_lm(fname, order=4):
    data = file(fname).read()
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in xrange(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char]+=1
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.iteritems()]
    outlm = {hist:normalize(chars) for hist, chars in lm.iteritems()}
    return outlm
def generate_letter(lm, history, order):
        history = history[-order:]
        dist = lm[history]
        x = random()
        for c,v in dist:
            x = x - v
            if x <= 0: return c
def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = []
    for i in xrange(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)


def post(stri="trainPoems2.txt"):
    if stri == "trainPoems2.txt":
        print "espanol"
    else:
        print "ingles"
    order =4
    lm = train_char_lm(stri,order)
    print "esta iniciando"
    for i in xrange(1,1000):
        lm =dict(Counter(lm)+Counter(train_char_lm(stri,order)))
    print "termino de aprender"
    for j in xrange(0,50):
        print "esta imprimiendo"
        opnF = open("poems.txt", 'a')
        opnF.writelines(generate_text(lm, order,249)+" #poems #bot #MachineLearning"+"\n")
        print "posteo en poems.txt"
    print "listo"

if raw_input() is 'e':
    post()
else:
    post("trainPoems.txt")
