delimiters = [' ', '*', '/', ',', ';', '(', ')', '[', ']', '{', '}', '=', '<', '>', '+', '-', '&', '|', '!','?',':']


def sashimi_char(st, c):
    tab = []
    it = 0
    a = 0
    if st == '':
        return []
    while a < len(st) and st[a] == c:
        it += 1
        tab.append(c)
        a += 1
    if a < len(st):
        tab.append(st[a])
    a += 1
    for i in st[a:]:
        if i == c:
            it += 2
            tab.append(c)
            if a != len(st) - 1:
                tab.append('')
        else:
            tab[it] = tab[it] + i
        a += 1
    return tab


def sashimi_lines(tab):
    t = []
    it = 0
    it2 = 0
    for word in tab:
        if it2 == 0 :
            t.append([])
        if word == '{' or word == ';':
            t[it].append(word)
            it += 1
            it2 = 0
        else:
            if word == '}':
                it += 1
                it2 = 0
                t.append([word])
                it += 2
                t.append([])
            else:
                t[it].append(word)
                it2 += 1
    return t


def remove_char(st, c):
    return "".join([i for i in st if i != c])


def remove_c_comments(st):
    while st.find('/*') != -1:
        if st.find('/*') != -1 and st.find('*/') != -1:
            a = st.find('/*')
            b = st.find('*/')
            if a < b:
                st = st[:a] + st[b + 2:]
            else:
                return "Erreur"
    return st


def remove_preprocess(st):
    while st.find('#') != -1:
        deb = st.find('#')
        fin = st[deb:].find('\n') + deb
        if fin != -1:
            st = st[:deb] + st[fin:]
        else:
            st = st[:deb]
    return st


def remove_cpp_comment(st):
    while st.find('//') != -1:
        deb = st.find('//')
        fin = st[deb:].find('\n') + deb
        if fin != -1:
            st = st[:deb] + st[fin:]
        else:
            st = st[:deb]
    return st


def remove_space(t):
    tab = []
    it = 0
    for line in t:
        tab.append([])
        for word in line:
            if word != ' ':
                tab[it].append(word)
        it += 1
    return tab

def remove_blank_table(t) :
    ta = []
    for it in t :
        if len(it) != 0 :
            ta.append(it)
    return ta

def sashimi_file(link):
    content = "".join(open(link).readlines())
    # removing all the comments
    content = remove_c_comments(remove_preprocess(content))
    content = remove_cpp_comment(content)
    content = remove_char(content, '\t')
    content = remove_char(content, '\n')

    # sashimi caracteres de separation !

    lines = [content]
    for deli in delimiters:
        t = []
        for line in lines:
            if line != deli:
                t += sashimi_char(line, deli)
            else:
                t += deli
        lines = t
    # sashimi lignes
    li = sashimi_lines(lines)
    lines = remove_space(li)
    lines = remove_blank_table(lines)
    return lines


print(sashimi_file("gtk-hotkey-registry.c"))
