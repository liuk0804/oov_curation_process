import re

# todo:catch repeating parenthesis
emoticons = {
':*':':* <emoji>', 
':-*':':-* <emoji>', 
':x':':x <emoji>', 
':-)':':-) <emoji>', 
':-))':':-)) <emoji>', 
':-)))':':-))) <emoji>', 
':-))))':':-)))) <emoji>', 
':-)))))':':-))))) <emoji>', 
':-))))))':':-)))))) <emoji>', 
':)':':) <emoji>', 
':))':':)) <emoji>', 
':)))':':))) <emoji>', 
':))))':':)))) <emoji>', 
':)))))':':))))) <emoji>', 
':))))))':':)))))) <emoji>', 
':)))))))':':))))))) <emoji>', 
':o)':':o) <emoji>', 
':]':':] <emoji>', 
':3':':3 <emoji>', 
':c)':':c) <emoji>', 
':>':':> <emoji>', 
'=]':'=] <emoji>', 
'8)':'8) <emoji>', 
'=)':'=) <emoji>', 
':}':':} <emoji>', 
':^)':':^) <emoji>', 
'|;-)':'|;-) <emoji>', 
":'-)": ":'-) <emoji>",
":')": ":') <emoji>",
'\o/':'\o/ <emoji>', 
'*\\0/*':'*\\0/* <emoji>', 
':-D':':-D <emoji>', 
':D':':D <emoji>', 
# '(\':':'(\': <emoji>', 
'8-D':'8-D <emoji>', 
'8D':'8D <emoji>', 
'x-D':'x-D <emoji>', 
'xD':'xD <emoji>', 
'X-D':'X-D <emoji>', 
'XD':'XD <emoji>', 
'=-D':'=-D <emoji>', 
'=D':'=D <emoji>', 
'=-3':'=-3 <emoji>', 
'=3':'=3 <emoji>', 
'B^D':'B^D <emoji>', 
'>:[':'>:[ <emoji>', 
':-(':':-( <emoji>', 
':-((':':-(( <emoji>', 
':-(((':':-((( <emoji>', 
':-((((':':-(((( <emoji>', 
':-(((((':':-((((( <emoji>', 
':-((((((':':-(((((( <emoji>', 
':-(((((((':':-((((((( <emoji>', 
':(':':( <emoji>', 
':((':':(( <emoji>', 
':(((':':((( <emoji>', 
':((((':':(((( <emoji>', 
':(((((':':((((( <emoji>', 
':((((((':':(((((( <emoji>', 
':(((((((':':((((((( <emoji>', 
':((((((((':':(((((((( <emoji>', 
':-c':':-c <emoji>', 
':c':':c <emoji>', 
':-<':':-< <emoji>', 
':<':':< <emoji>', 
':-[':':-[ <emoji>', 
':[':':[ <emoji>', 
':{':':{ <emoji>', 
':-||':':-|| <emoji>', 
':@':':@ <emoji>', 
":'-(": ":'-( <emoji>",
":'(": ":'( <emoji>",
'D:<':'D:< <emoji>', 
'D:':'D: <emoji>', 
'D8':'D8 <emoji>', 
'D;':'D; <emoji>', 
'D=':'D= <emoji>', 
'DX':'DX <emoji>', 
'v.v':'v.v <emoji>', 
"D-':": "D-': <emoji>",
'(>_<)':'(>_<) <emoji>', 
':|':':| <emoji>', 
'>:O':'>:O <emoji>', 
':-O':':-O <emoji>', 
':-o':':-o <emoji>', 
':O':':O <emoji>', 
'°o°':'°o° <emoji>', 
'o_O':'o_O <emoji>', 
'o_0':'o_0 <emoji>', 
'o.O':'o.O <emoji>', 
'o-o':'o-o <emoji>', 
'8-0':'8-0 <emoji>', 
'|-O':'|-O <emoji>', 
';-)':';-) <emoji>', 
';)':';) <emoji>', 
'*-)':'*-) <emoji>', 
'*)':'*) <emoji>', 
';-]':';-] <emoji>', 
';]':';] <emoji>', 
';D':';D <emoji>', 
';^)':';^) <emoji>', 
':-,':':-, <emoji>', 
'>:P':'>:P <emoji>', 
':-P':':-P <emoji>', 
':P':':P <emoji>', 
'X-P':'X-P <emoji>', 
'x-p':'x-p <emoji>', 
'xp':'xp <emoji>', 
'XP':'XP <emoji>', 
':-p':':-p <emoji>', 
':p':':p <emoji>', 
'=p':'=p <emoji>', 
':-Þ':':-Þ <emoji>', 
':Þ':':Þ <emoji>', 
':-b':':-b <emoji>', 
':b':':b <emoji>', 
':-&':':-& <emoji>', 
'>:\\':'>:\\ <emoji>', 
'>:/':'>:/ <emoji>', 
':-/':':-/ <emoji>', 
':-.':':-. <emoji>', 
':/':':/ <emoji>', 
':\\':':\\ <emoji>', 
'=/':'=/ <emoji>', 
'=\\':'=\\ <emoji>', 
':L':':L <emoji>', 
'=L':'=L <emoji>', 
':S':':S <emoji>', 
'>.<':'>.< <emoji>', 
':-|':':-| <emoji>', 
'<:-|':'<:-| <emoji>', 
':-X':':-X <emoji>', 
':X':':X <emoji>', 
':-#':':-# <emoji>', 
':#':':# <emoji>', 
'O:-)':'O:-) <emoji>', 
'0:-3':'0:-3 <emoji>', 
'0:3':'0:3 <emoji>', 
'0:-)':'0:-) <emoji>', 
'0:)':'0:) <emoji>', 
'0;^)':'0;^) <emoji>', 
'>:)':'>:) <emoji>', 
'>:D':'>:D <emoji>', 
'>:-D':'>:-D <emoji>', 
'>;)':'>;) <emoji>', 
'>:-)':'>:-) <emoji>', 
'}:-)':'}:-) <emoji>', 
'}:)':'}:) <emoji>', 
'3:-)':'3:-) <emoji>', 
'3:)':'3:) <emoji>', 
'o/\o':'o/\o <emoji>', 
'^5':'^5 <emoji>', 
'>_>^':'>_>^ <emoji>', 
'<3':'<3 <emoji>', 
'(-;':'(-; <emoji>',
'(-_-)':'(-_-) <emoji>',
'(8':'(8 <emoji>',
'(;':'(; <emoji>',
'(^_^':'(^_^ <emoji>',
'(^_^)':'(^_^) <emoji>',
'-.-':'-.- <emoji>',
'-_-':'-_- <emoji>',
'-__-':'-__- <emoji>',
'-______-':'-______- <emoji>',
'.(^_^)':'.(^_^) <emoji>',
'._.':'._. <emoji>',
'.__.':'.__. <emoji>',
'/=':'/= <emoji>',
'0_0':'0_0 <emoji>',
'8-)':'8-) <emoji>',
'8-/':'8-/ <emoji>',
'8-O':'8-O <emoji>',
'8/':'8/ <emoji>',
'8=D':'8=D <emoji>',
'8P':'8P <emoji>',
'8|':'8| <emoji>',
':-3':':-3 <emoji>',
':-]':':-] <emoji>',
':-}':':-} <emoji>',
':0':':0 <emoji>',
':=P':':=P <emoji>',
';-':';- <emoji>',
';-D':';-D <emoji>',
';-P':';-P <emoji>',
';/':';/ <emoji>',
';P':';P <emoji>',
'=(':'=( <emoji>',
'=P':'=P <emoji>',
'=_=':'=_= <emoji>',
'=x':'=x <emoji>',
'=|':'=| <emoji>',
'>:(':'>:( <emoji>',
'@.@':'@.@ <emoji>',
'@8':'@8 <emoji>',
'@_@':'@_@ <emoji>',
'O.o':'O.o <emoji>',
'O=':'O= <emoji>',
'P.S':'P.S <emoji>',
'P.s':'P.s <emoji>',
'T.T':'T.T <emoji>',
'T_T':'T_T <emoji>',
'\\(^_^)/':'\\(^_^)/ <emoji>',
'\\^_^/':'\\^_^/ <emoji>',
'\\m/':'\\m/ <emoji>',
'^-^':'^-^ <emoji>',
'^.^':'^.^ <emoji>',
'^^':'^^ <emoji>',
'^^.':'^^. <emoji>',
'^_-':'^_- <emoji>',
'^_^':'^_^ <emoji>',
'^_^)b':'^_^)b <emoji>',
'^_^.':'^_^. <emoji>',
'^__^':'^__^ <emoji>',
'^o^':'^o^ <emoji>',
'^v^':'^v^ <emoji>',
'o3o':'o3o <emoji>',
'p.s':'p.s <emoji>',
'u.u':'u.u <emoji>',
'x.x':'x.x <emoji>',
'xD.':'xD. <emoji>',
'xP':'xP <emoji>',
'x_x':'x_x <emoji>',
'|8':'|8 <emoji>',
'~_~':'~_~ <emoji>',

}

# todo: clear this mess
pattern = re.compile("^[:=\*\-\(\)\[\]x0oO\#\<\>8\\.\'|\{\}\@\^\_T3\?\!]+$")
mirror_emoticons = {}
for exp, tag in emoticons.items():
    if pattern.match(exp) \
            and any(ext in exp for ext in [";", ":", "="]) \
            and not any(ext in exp for ext in ["L", "D", "p", "P", "3"]):
        mirror = exp[::-1]

        if "{" in mirror:
            mirror = mirror.replace("{", "}")
        elif "}" in mirror:
            mirror = mirror.replace("}", "{")

        if "(" in mirror:
            mirror = mirror.replace("(", ")")
        elif ")" in mirror:
            mirror = mirror.replace(")", "(")

        if "<" in mirror:
            mirror = mirror.replace("<", ">")
        elif ">" in mirror:
            mirror = mirror.replace(">", "<")

        if "[" in mirror:
            mirror = mirror.replace("[", "]")
        elif "]" in mirror:
            mirror = mirror.replace("]", "[")

        if "\\" in mirror:
            mirror = mirror.replace("\\", "/")
        elif "/" in mirror:
            mirror = mirror.replace("/", "\\")

        # print(exp + "\t\t" + mirror)
        mirror_emoticons[mirror] = tag
emoticons.update(mirror_emoticons)

for exp, tag in list(emoticons.items()):
    if exp.lower() not in emoticons:
        emoticons[exp.lower()] = tag

# emoticon_groups = {
#     "positive": {'<emoji>', '<emoji>', '<emoji>', '<emoji>', '<emoji>'},
#     "negative": {'<emoji>', '<emoji>', }
# }


def print_positive(sentiment):
    for e, tag in emoticons.items():
        if tag in emoticon_groups[sentiment]:
            print(e)

# print_positive("negative")
# print(" ".join(list(emoticons.keys())))
# [print(e) for e in list(emoticons.keys())]
