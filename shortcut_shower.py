#!/bin/python3

is_alt_down = False
is_shift_down = False
is_win_down = False
is_altgr_down = False
is_ctrl_down = False

path = "/home/user/.scripts/"

import gi
import sched, time

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


tooltips = {}

cps = 0
old_cps = 0
count = 0

searching = False

from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def measure_cp():
    global cps, old_cps
    old_cps = round((cps + old_cps) / 2)
    cps = 0
    charspersecond.set_text("chars/minute = " + str(old_cps * 60))


# rt = RepeatedTimer(1, measure_cp)  # it auto-starts, no need of rt.start()


def update_tooltips():
    search_string = search.get_text()
    for key in keys:
        # key.get_style_context().add_class("destructive-action")
        tooltip = get_tooltip(key.name)
        if tooltip is not "" and search_string in tooltip:
            key.get_style_context().add_class("suggested-action")
        else:
            key.get_style_context().remove_class("suggested-action")


def capitalize(s):
    if is_altgr_down:
        return alternative(s)
    if s in [x.name for x in alphabet]:
        return s.upper()
    elif s == "1":
        return "!"
    elif s == "2":
        return '"'
    elif s == "3":
        return "§"
    elif s == "4":
        return "$"
    elif s == "5":
        return "%"
    elif s == "6":
        return "&"
    elif s == "7":
        return "/"
    elif s == "8":
        return "("
    elif s == "9":
        return ")"
    elif s == "0":
        return "="
    elif s == "ß":
        return "?"
    elif s == "^":
        return "°"
    elif s == ",":
        return ";"
    elif s == ".":
        return ":"
    elif s == "-":
        return "_"
    elif s == "<":
        return ">"
    elif s == "´":
        return "`"
    elif s == "+":
        return "*"
    elif s == "#":
        return "'"
    else:
        return s


def shift_up():
    global is_shift_down
    is_shift_down = False
    update_tooltips()
    rshift.get_style_context().remove_class("destructive-action")
    update_labels()


def shift_down():
    global is_shift_down
    is_shift_down = True
    update_tooltips()
    update_labels()


def altgr_up():
    global is_altgr_down
    is_altgr_down = False
    update_tooltips()
    update_labels()


def alternative(name):
    if is_shift_down:
        if name == "ß":
            return "¿"
        elif name == "1":
            return "¡"
        elif name == "2":
            return "⅛"
        elif name == "3":
            return "£"
        elif name == "4":
            return "¤"
        elif name == "5":
            return "⅜"
        elif name == "6":
            return "⅝"
        elif name == "7":
            return "⅞"
        elif name == "8":
            return "™"
        elif name == "9":
            return "±"
        elif name == "0":
            return "°"
        elif name == "^":
            return "″"
        elif name == ",":
            return "×"
        elif name == ".":
            return "÷"
        elif name == "a":
            return "Æ"
        elif name == "b":
            return "‘"
        elif name == "c":
            return "Ĉ"
        elif name == "d":
            return "Ð"
        elif name == "f":
            return "ª"
        elif name == "g":
            return "Ĝ"
        elif name == "h":
            return "Ĥ"
        elif name == "i":
            return "ı"
        elif name == "j":
            return "Ĵ"
        elif name == "k":
            return "&"
        elif name == "l":
            return "Ł"
        elif name == "m":
            return "º"
        elif name == "n":
            return "’"
        elif name == "o":
            return "Ø"
        elif name == "p":
            return "Þ"
        elif name == "q":
            return "Ω"
        elif name == "r":
            return "®"
        elif name == "s":
            return "Ŝ"
        elif name == "t":
            return "Ŧ"
        elif name == "u":
            return "Ŭ"
        elif name == "v":
            return "‚"
        elif name == "w":
            return "Ł"
        elif name == "x":
            return "‹"
        elif name == "y":
            return "›"
        elif name == "z":
            return "¥"
        elif name == "ö":
            return "Ö"
        elif name == "ä":
            return "Ä"
        elif name == "ü":
            return "Ü"

    if name == "ß":
        return "\\"
    elif name == "q":
        return "@"
    elif name == "1":
        return "¹"
    elif name == "2":
        return "²"
    elif name == "3":
        return "³"
    elif name == "4":
        return "₹"
    elif name == "5":
        return "½"
    elif name == "6":
        return "¬"
    elif name == "7":
        return "{"
    elif name == "8":
        return "["
    elif name == "9":
        return "]"
    elif name == "0":
        return "}"
    elif name == "+":
        return "~"
    elif name == "<":
        return "|"
    elif name == "a":
        return "æ"
    elif name == "b":
        return "“"
    elif name == "c":
        return "ĉ"
    elif name == "d":
        return "ð"
    elif name == "e":
        return "€"
    elif name == "f":
        return "đ"
    elif name == "g":
        return "ĝ"
    elif name == "h":
        return "ĥ"
    elif name == "i":
        return "→"
    elif name == "j":
        return "ĵ"
    elif name == "k":
        return "ĸ"
    elif name == "l":
        return "ł"
    elif name == "m":
        return "µ"
    elif name == "n":
        return "”"
    elif name == "o":
        return "ø"
    elif name == "p":
        return "þ"
    elif name == "r":
        return "¶"
    elif name == "s":
        return "ŝ"
    elif name == "t":
        return "ŧ"
    elif name == "u":
        return "ŭ"
    elif name == "v":
        return "„"
    elif name == "w":
        return "ł"
    elif name == "x":
        return "«"
    elif name == "y":
        return "»"
    elif name == "z":
        return "←"
    elif name == "#":
        return "’"
    elif name == ",":
        return "·"
    elif name == ".":
        return "…"
    elif name == "-":
        return "–"
    elif name == "^":
        return "′"
    elif name == "<":
        return "|"
    else:
        return name


def altgr_down():
    global is_altgr_down
    is_altgr_down = True
    update_tooltips()
    update_labels()


def update_modifiers():
    mods = ""
    if is_shift_down:
        mods += "Shift "
    if is_win_down:
        mods += "Win "
    if is_altgr_down:
        mods += "AltGr "
    if is_ctrl_down:
        mods += "Ctrl "
    if is_alt_down:
        mods += "Alt "
    modifiers.set_text(mods)


def update_labels():
    if is_shift_down:
        for c in capitalizable_chars:
            c.set_label(capitalize(c.name))
    elif is_altgr_down:
        for a in altgrable_chars:
            a.set_label(alternative(a.name))
    elif not is_shift_down:
        for c in capitalizable_chars:
            c.set_label((c.name))



class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, a):
        update_tooltips()
        info.set_text(get_tooltip(a.name))
        print(get_tooltip(a.name))

    def key_press_handler(self, window, key):
        global is_ctrl_down, is_altgr_down, is_alt_down
        k = key.keyval
        text.set_text(str(k))
        btn = number_to_button(k)
        if btn is None:
            name.set_text("Unknown")
            print("Button " + str(k) + " not supported")
            return
        info.set_text(get_tooltip(btn.name))
        if btn.get_label()[1:].lower() == "shift":
            shift_down()
        elif btn.get_label()[1:].lower() == "ctrl":
            is_ctrl_down = True
        elif btn.get_label()[1:].lower() == "alt":
            is_alt_down = True
        elif btn.get_label().lower() == "alt gr":
            altgr_down()
        elif btn.get_label()[1:].lower() == "win":
            global is_win_down
            is_win_down = True
            update_tooltips()
        btn.get_style_context().add_class("destructive-action")
        name.set_text(btn.get_label().replace("\n", " "))
        update_modifiers()

    def key_release_handler(self, window, key):
        k = key.keyval
        btn = number_to_button(k)
        if btn is None:
            print("Button " + str(k) + " not supported")
            return
        if btn.get_label()[1:].lower() == "shift":
            shift_up()
        elif btn.get_label()[1:].lower() == "alt":
            global is_alt_down
            is_alt_down = False
        elif btn.get_label()[1:].lower() == "ctrl":
            global is_ctrl_down
            is_ctrl_down = False
        elif btn.get_label().lower() == "alt gr":
            altgr_up()
        elif btn.get_label()[1:].lower() == "win":
            global is_win_down
            is_win_down = False
            update_tooltips()
        btn.get_style_context().remove_class("destructive-action")
        global cps, searching

        if not searching and btn.get_label() == "/":
            searching = True
            search.grab_focus()
            search.set_text("")
        elif searching and btn.get_label() == "ESC":
            searching = False
            space.grab_focus()
        update_modifiers()

    def search(self, a):
        update_tooltips()


def number_to_button(key):
    if 64 < key < 91 or key == 214 or key == 220 or key == 196:
        return number_to_button(key + 32)
    elif key == 65307:  # Esc
        return esc
    elif key == 65469 + 1:  # F1
        return f1
    elif key == 65469 + 2:  # F2
        return f2
    elif key == 65469 + 3:  # F3
        return f3
    elif key == 65469 + 4:  # F4
        return f4
    elif key == 65469 + 5 or key == 269025046:  # F5 or media rewind
        return f5
    elif key == 65469 + 6 or key == 269025044:  # F6 or media play pause
        return f6
    elif key == 65469 + 7 or key == 269025047:  # F7 or media faster
        return f7
    elif key == 65469 + 8:  # F8
        return f8
    elif key == 65469 + 9:  # F9
        return f9
    elif key == 65469 + 10:  # F10
        return f10
    elif key == 65469 + 11:  # F11
        return f11
    elif key == 65469 + 12:  # F12
        return f12
    elif key == 65407:
        return num_lock
    elif key == 65455:
        return num_div
    elif key == 65450:
        return num_times
    elif key == 65453:
        return num_minus
    elif key == 65451:
        return num_plus
    elif key == 65421:
        return num_enter
    elif key == 65438:
        return num_0
    elif key == 65436:
        return num_1
    elif key == 65433:
        return num_2
    elif key == 65435:
        return num_3
    elif key == 65430:
        return num_4
    elif key == 65437:
        return num_5
    elif key == 65432:
        return num_6
    elif key == 65429:
        return num_7
    elif key == 65431:
        return num_8
    elif key == 65434:
        return num_9
    elif key == 65439:
        return num_comma
    elif key == 32:  # Space
        return space
    elif key == 97 or key == 230 or key == 198:
        return a
    elif key == 98 or key == 2770 or key == 2768:
        return b
    elif key == 99 or key == 742 or key == 710:
        return c
    elif key == 100 or key == 240 or key == 208:
        return d
    elif key == 101 or key == 8364 or key == 170:
        return e
    elif key == 102 or key == 496 or key == 170:
        return f
    elif key == 103 or key == 71 or key == 760 or key == 728:
        return g
    elif key == 104 or key == 694 or key == 678:
        return h
    elif key == 105 or key == 2301 or key == 697:
        return i
    elif key == 106 or key == 700 or key == 684:
        return j
    elif key == 107 or key == 930 or key == 38:
        return k
    elif key == 108 or key == 435 or key == 419:
        return l
    elif key == 109 or key == 181 or key == 186:
        return m
    elif key == 110 or key == 2771 or key == 2769:
        return n
    elif key == 111 or key == 248 or key == 216:
        return o
    elif key == 112 or key == 254 or key == 222:
        return p
    elif key == 113 or key == 64 or key == 2009:
        return q
    elif key == 114 or key == 182 or key == 174:
        return r
    elif key == 115 or key == 766 or key == 734:
        return s
    elif key == 116 or key == 956 or key == 940:
        return t
    elif key == 117 or key == 765 or key == 733:
        return u
    elif key == 118 or key == 2814 or key == 2813:
        return v
    elif key == 119 or key == 2814 or key == 2813:
        return w
    elif key == 120 or key == 171 or key == 16785465:
        return x
    elif key == 121 or key == 187 or key == 16785466:
        return y
    elif key == 122 or key == 2299 or key == 165:
        return z
    elif key == 228 or key == 65114:
        return ae
    elif key == 246 or key == 65113 or key == 65120:
        return oe
    elif key == 252 or key == 65111 or key == 65112:
        return ue
    elif key == 65106 or key == 176 or key == 16785458 or key == 16785459:
        return caret
    elif key == 65289 or key == 65056:
        return tab
    elif key == -1:
        return caps
    elif key == 65505 or key == 65509:
        return lshift
    elif key == 65507:
        return lctrl
    elif key == 65515:
        return lwin
    elif key == 65513 or key == 65511:
        return lalt
    elif key == 48 + 0 or key == 61 or key == 125:
        return n0
    elif key == 48 + 1 or key == 33 or key == 185 or key == 161:
        return n1
    elif key == 48 + 2 or key == 34 or key == 178 or key == 2755:
        return n2
    elif key == 48 + 3 or key == 167 or key == 179 or key == 163:
        return n3
    elif key == 48 + 4 or key == 36 or key == 16785593 or key == 164:
        return n4
    elif key == 48 + 5 or key == 37 or key == 189 or key == 2756:
        return n5
    elif key == 48 + 6 or key == 172 or key == 2757:
        return n6
    elif key == 48 + 7 or key == 47 or key == 123 or key == 2758:
        return n7
    elif key == 48 + 8 or key == 40 or key == 91 or key == 2761:
        return n8
    elif key == 48 + 9 or key == 41 or key == 93 or key == 177:
        return n9
    elif key == 65361:
        return left
    elif key == 65362:
        return up
    elif key == 65363:
        return right
    elif key == 65364:
        return down
    elif key == 44 or key == 59 or key == 183 or key == 215:
        return comma
    elif key == 45 or key == 95 or key == 2729 or key == 2730:
        return minus
    elif key == 46 or key == 58 or key == 16785446 or key == 247:
        return period
    elif key == 60 or key == 62 or key == 65128:
        return less_than
    elif key == 65027:
        return altgr
    elif key == 65383:
        return menu
    elif key == 65508:
        return rctrl
    elif key == 65506:
        return rshift
    elif key == 65293:
        return enter
    elif key == 65288:
        return back
    elif key == 223 or key == 63 or key == 92 or key == 191:
        return ss
    elif key == 65105 or key == 65104 or key == 65115 or key == 65116:
        return accent
    elif key == 43 or key == 42 or key == 126 or key == 175:
        return plus
    elif key == 35 or key == 39 or key == 2769 or key == 65109:
        return pound
    elif key == 65299:
        return pause
    elif key == 65379:
        return insert
    elif key == 65365:
        return pageup
    elif key == 65366:
        return pagedown
    elif key == 65535:
        return delete
    elif key == 65367:
        return end


builder = Gtk.Builder()
builder.add_from_file(path + "Keyboard.glade")
builder.connect_signals(Handler())

esc = builder.get_object("esc")
esc.name = "esc"
caret = builder.get_object("caret")
caret.name = "^"
tab = builder.get_object("tab")
tab.name = "tab"
caps = builder.get_object("caps")
caps.name = "caps"
lshift = builder.get_object("lshift")
lshift.name = "lshift"
lctrl = builder.get_object("lctrl")
lctrl.name = "lctrl"
lwin = builder.get_object("lwin")
lwin.name = "lwin"
lalt = builder.get_object("lalt")
lalt.name = "lalt"

f1 = builder.get_object("f1")
f1.name = "f1"
f2 = builder.get_object("f2")
f2.name = "f2"
f3 = builder.get_object("f3")
f3.name = "f3"
f4 = builder.get_object("f4")
f4.name = "f4"
f5 = builder.get_object("f5")
f5.name = "f5"
f6 = builder.get_object("f6")
f6.name = "f6"
f7 = builder.get_object("f7")
f7.name = "f7"
f8 = builder.get_object("f8")
f8.name = "f8"
f9 = builder.get_object("f9")
f9.name = "f9"
f10 = builder.get_object("f10")
f10.name = "f10"
f11 = builder.get_object("f11")
f11.name = "f11"
f12 = builder.get_object("f12")
f12.name = "f12"
space = builder.get_object("space")
space.name = "space"

num_lock = builder.get_object("num_lock")
num_lock.name = "num_lock"
num_div = builder.get_object("num_div")
num_div.name = "num_div"
num_times = builder.get_object("num_times")
num_times.name = "num_times"
num_minus = builder.get_object("num_minus")
num_minus.name = "num_minus"
num_plus = builder.get_object("num_plus")
num_plus.name = "num_plus"
num_enter = builder.get_object("num_enter")
num_enter.name = "num_enter"
num_0 = builder.get_object("num_0")
num_0.name = "num_0"
num_1 = builder.get_object("num_1")
num_1.name = "num_1"
num_2 = builder.get_object("num_2")
num_2.name = "num_2"
num_3 = builder.get_object("num_3")
num_3.name = "num_3"
num_4 = builder.get_object("num_4")
num_4.name = "num_4"
num_5 = builder.get_object("num_5")
num_5.name = "num_5"
num_6 = builder.get_object("num_6")
num_6.name = "num_6"
num_7 = builder.get_object("num_7")
num_7.name = "num_7"
num_8 = builder.get_object("num_8")
num_8.name = "num_8"
num_9 = builder.get_object("num_9")
num_9.name = "num_9"
num_comma = builder.get_object("num_comma")
num_comma.name = "num_comma"

a = builder.get_object("a")
a.name = "a"
b = builder.get_object("b")
b.name = "b"
c = builder.get_object("c")
c.name = "c"
d = builder.get_object("d")
d.name = "d"
e = builder.get_object("e")
e.name = "e"
f = builder.get_object("f")
f.name = "f"
g = builder.get_object("g")
g.name = "g"
h = builder.get_object("h")
h.name = "h"
i = builder.get_object("i")
i.name = "i"
j = builder.get_object("j")
j.name = "j"
k = builder.get_object("k")
k.name = "k"
l = builder.get_object("l")
l.name = "l"
m = builder.get_object("m")
m.name = "m"
n = builder.get_object("n")
n.name = "n"
o = builder.get_object("o")
o.name = "o"
p = builder.get_object("p")
p.name = "p"
q = builder.get_object("q")
q.name = "q"
r = builder.get_object("r")
r.name = "r"
s = builder.get_object("s")
s.name = "s"
t = builder.get_object("t")
t.name = "t"
u = builder.get_object("u")
u.name = "u"
v = builder.get_object("v")
v.name = "v"
w = builder.get_object("w")
w.name = "w"
x = builder.get_object("x")
x.name = "x"
y = builder.get_object("y")
y.name = "y"
z = builder.get_object("z")
z.name = "z"
ae = builder.get_object("ae")
ae.name = "ä"
oe = builder.get_object("oe")
oe.name = "ö"
ue = builder.get_object("ue")
ue.name = "ü"
comma = builder.get_object("comma")
comma.name = ","
period = builder.get_object("period")
period.name = "."
minus = builder.get_object("minus")
minus.name = "-"

alphabet = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, ae, oe, ue]

n0 = builder.get_object("n0")
n0.name = "0"
n1 = builder.get_object("n1")
n1.name = "1"
n2 = builder.get_object("n2")
n2.name = "2"
n3 = builder.get_object("n3")
n3.name = "3"
n4 = builder.get_object("n4")
n4.name = "4"
n5 = builder.get_object("n5")
n5.name = "5"
n6 = builder.get_object("n6")
n6.name = "6"
n7 = builder.get_object("n7")
n7.name = "7"
n8 = builder.get_object("n8")
n8.name = "8"
n9 = builder.get_object("n9")
n9.name = "9"
less_than = builder.get_object("less_than")
less_than.name = "<"

altgr = builder.get_object("altgr")
altgr.name = "ALT GR"
fn = builder.get_object("fn")
fn.name = "FN"
menu = builder.get_object("menu")
menu.name = "Menu"
rctrl = builder.get_object("rctrl")
rctrl.name = "RCTRL"
rshift = builder.get_object("rshift")
rshift.name = "RShift"
enter = builder.get_object("enter")
enter.name = "Enter"
back = builder.get_object("back")
back.name = "◀️"
ss = builder.get_object("ss")
ss.name = "ß"
accent = builder.get_object("accent")
accent.name = "´"
plus = builder.get_object("plus")
plus.name = "+"
pound = builder.get_object("pound")
pound.name = "#"

b_print = builder.get_object("print")
b_print.name = "Print"
scrolllock = builder.get_object("scrolllock")
scrolllock.name = "Scroll\nLock"
pause = builder.get_object("pause")
pause.name = "Pause"
insert = builder.get_object("insert")
insert.name = "Insert"
home = builder.get_object("home")
home.name = "Home"
pageup = builder.get_object("pageup")
pageup.name = "Page\nUp"
pagedown = builder.get_object("pagedown")
pagedown.name = "Page\nDown"
delete = builder.get_object("delete")
delete.name = "Delete"
end = builder.get_object("end")
end.name = "End"

numbers = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
capitalizable_chars = alphabet + numbers + [caret, period, comma, minus, less_than, less_than, ss, accent, plus, pound]
altgrable_chars = numbers + [ss, plus, q, e, less_than, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o,
                   p, q, r, s, t, u, v, w, x, y, z, pound, comma, period, minus, caret]

up = builder.get_object("up")
up.name = "up"
left = builder.get_object("left")
left.name = "left"
right = builder.get_object("right")
right.name = "right"
down = builder.get_object("down")
down.name = "down"

keys = [
           esc, caret, tab, caps, lshift, lctrl, lwin, lalt, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, space,
           num_lock, num_div, num_times, num_minus, num_plus, num_enter, num_0, num_1, num_2, num_3, num_4, num_5,
           num_6, num_7, num_8, num_9, num_comma, comma, period, minus, up, down, left, right, less_than, altgr, fn,
           menu, rctrl, rshift, enter, back, ss, accent, plus, pound, b_print, scrolllock, pause, insert, home, pageup,
           delete, end, pagedown
       ] + alphabet + numbers


def parse_tips(file):
    content = ""
    with open(file) as f:
        content = f.read()
    for line in content.splitlines():
        if not (line.strip().startswith("#") or line.isspace() or line is ""):
            l = line.split(":")
            tooltips[l[0].strip().lower()] = l[1].strip()


    unsup_shortcuts = ""
    for t in tooltips:
        if t.split(" ")[-1].lower() not in [x.name.lower() for x in keys]:
            unsup_shortcuts += t + "\n"
    if unsup_shortcuts != "":
        print("Unsupported shortcuts:")
        print(unsup_shortcuts)


parse_tips("/tmp/testkeys")


def translate(ka):
    if ka == "ö":
        return "oe"
    if ka == "ä":
        return "ae"
    if ka == "ü":
        return "ue"
    if ka == "ß":
        return "ss"
    return ka


def get_tooltip(ka):
    global is_win_down, is_shift_down
    ka = ka.lower()
    tooltip = ""
    for kb in tooltips:
        kb = kb.lower()
        if translate(ka) in kb.split(" "):
            if "shift" in kb and "win" not in kb:
                if is_shift_down and not is_win_down:
                    tooltip += tooltips[kb] + "\n"
                elif not is_shift_down and not is_win_down:
                    tooltip += "+Shift: " + tooltips[kb] + "\n"
            elif "win" in kb and "shift" not in kb:
                if is_win_down and not is_shift_down:
                    tooltip += tooltips[kb] + "\n"
                elif not is_win_down and not is_shift_down:
                    tooltip += "+Win: " + tooltips[kb] + "\n"
            elif "shift" in kb and "win" in kb:
                if is_shift_down and is_win_down:
                    tooltip += "f" + tooltips[kb] + "\n"
                elif is_win_down:
                    tooltip += "+Shift: " + tooltips[kb] + "\n"
                elif is_shift_down:
                    tooltip += "+Win: " + tooltips[kb] + "\n"
                else:
                    tooltip += "+Shift+Win: " + tooltips[kb] + "\n"
            else:
                #tooltip += tooltips[kb] + "\n"
                pass
    return tooltip[:-1] if tooltip.endswith("\n") else tooltip


text = builder.get_object("text")
name = builder.get_object("name")
search = builder.get_object("search")
info = builder.get_object("textbuffer")
charspersecond = None
modifiers = builder.get_object("modifiers")

update_tooltips()
space.grab_focus()

window = builder.get_object("window")
window.set_title("f")
window.show_all()

Gtk.main()
