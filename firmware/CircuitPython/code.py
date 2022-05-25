print("Starting setup...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

from kmk.scanners.keypad import MatrixScanner

print("Initializing keyboard...")

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

# keyboard.debug_enabled = True

keyboard.matrix = [
                    MatrixScanner(column_pins=(board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0),
                                  row_pins=(board.GP6,board.GP7,board.GP8,board.GP9)),
                    MatrixScanner(column_pins=(board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15),
                                  row_pins=(board.GP16,board.GP17,board.GP18,board.GP19))
                  ]

keyboard.coord_mapping = [ 
    0,  1,  2,  3,  4,  5,                  24, 25, 26, 27, 28, 29,
    6,  7,  8,  9,  10, 11,                 30, 31, 32, 33, 34, 35,
    12, 13, 14, 15, 16, 17,                 36, 37, 38, 39, 40, 41,
                           21,           44,
            20,    22, 23, 19, 18,   47, 46, 42, 43,    45,
    ]

# KMK Layer Mods
# --------------
# KC.DF(layer)	    Switches the default layer until the next time the keyboard powers off
# KC.MO(layer)	    Momentarily activates layer, switches off when you let go
# KC.LM(layer, mod)	As MO(layer) but with mod active
# KC.LT(layer, kc)	Momentarily activates layer if held, sends kc if tapped
# KC.TG(layer)	    Toggles the layer (enables it if no active, and vise versa)
# KC.TO(layer)	    Activates layer and deactivates all other layers
# KC.TT(layer)	    Momentarily activates layer if held, toggles it if tapped repeatedly

Num = KC.MO(1)
Nav = KC.MO(2)
Sym = KC.MO(3) 

WordL = KC.LALT(KC.LEFT)
WordR = KC.LALT(KC.RIGHT)

Undo = KC.LGUI(KC.Z)
Cut = KC.LGUI(KC.X)
Copy = KC.LGUI(KC.C)
Paste = KC.LGUI(KC.V)
Redo = KC.LGUI(KC.Y)

vsNavB = KC.LCTL(KC.MINS)
vsNavF = KC.LCTL(KC.LSFT(KC.MINS))
    
keyboard.keymap = [
    # Base layer
    #-------+-------+-------+-------+-------+-------+                                      +-------+-------+-------+-------+-------+-------+
    #  TAB  |   Q   |   W   |   F   |   P   |   G   |                                      |   J   |   L   |   U   |   Y   |   ;   |   '   |
    #-------+-------+-------+-------+-------+-------|                                      |-------+-------+-------+-------+-------+-------|
    #  CRTL |   A   |   R   |   S   |   T   |   D   |                                      |   H   |   N   |   E   |   I   |   O   | ENTER |
    #-------+-------+-------+-------+-------+-------+-------+                      +-------+-------+-------+-------+-------+-------+-------|
    # SHIFT |   Z   |   X   |   C   |   V   |   B   |       |                      |   -   |   K   |   M   |   ,   |   .   |   /   | SHIFT |
    #-------+-------+-------+-------+-------+-------+-------+-------+      +-------+-------+-------+-------+-------+-------+-------+-------+
    #               |       |       |  GUI  |  ALT  | SPACE |  Nav  |      |  Sym  | BKSPC |  Num  |  Nav  |       |       |
    #               +-------+       +-------+-------+-------+-------+      +-------+-------+-------+-------+       +-------+
    [
        KC.TAB,  KC.Q, KC.W, KC.F, KC.P,  KC.G,                                      KC.J, KC.L, KC.U,    KC.Y,   KC.SCLN, KC.QUOT,
        KC.LCTL, KC.A, KC.R, KC.S, KC.T,  KC.D,                                      KC.H, KC.N, KC.E,    KC.I,   KC.O,    KC.ENTER,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V,  KC.B,                                      KC.K, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, 
                                                  KC.NO,                  KC.MINS,
                       KC.NO,    KC.LGUI,KC.LALT, KC.SPC,  Nav,         Sym, KC.BKSP, Num, Nav,             KC.NO,
    ],

    # Number layer
    #-------+-------+-------+-------+-------+-------+                                      +-------+-------+-------+-------+-------+-------+
    #       |       |       |       |       |       |                                      |       |   7   |   8   |   9   |   =   |       |
    #-------+-------+-------+-------+-------+-------|                                      |-------+-------+-------+-------+-------+-------|
    #       |       |       |       |       |       |                                      |       |   4   |   5   |   6   |   -   |   /   |
    #-------+-------+-------+-------+-------+-------+-------+                      +-------+-------+-------+-------+-------+-------+-------|
    #       |       |       |       |       |       |       |                      |       |   0   |   1   |   2   |   3   |   +   |   *   |
    #-------+-------+-------+-------+-------+-------+-------+-------+      +-------+-------+-------+-------+-------+-------+-------+-------+
    #               |       |       |       |       | SPACE |       |      |       | BKSPC |       |   ,   |       |   .   |
    #               +-------+       +-------+-------+-------+-------+      +-------+-------+-------+-------+       +-------+
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,                                      KC.NO, KC.N7, KC.N8, KC.N9, KC.EQL, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,                                      KC.NO, KC.N4, KC.N5, KC.N6, KC.PMNS, KC.LPRN,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,                                      KC.N0, KC.N1, KC.N2, KC.N3, KC.PPLS, KC.ASTR, 
                                                  KC.NO,                      KC.NO,
                      KC.NO,        KC.NO, KC.NO, KC.SPC, KC.NO,        KC.NO, KC.BKSP, KC.NO, KC.COMM,     KC.PDOT,
    ],

    # Navigation layer
    #-------+-------+-------+-------+-------+-------+                                      +-------+-------+-------+-------+-------+-------+
    #  ESC  |       |       |       |       | VOL+  |                                      |       | HOME  |   ↑   |  END  | PGUP  |       |
    #-------+-------+-------+-------+-------+-------|                                      |-------+-------+-------+-------+-------+-------|
    #       |       |  ALT  | CTRL  | SHIFT | VOL-  |                                      |       |   ←   |   ↓   |   →   |PGDOWN |       |
    #-------+-------+-------+-------+-------+-------+-------+                      +-------+-------+-------+-------+-------+-------+-------|
    # SHIFT | Undo  |  Cut  | Copy  | Paste | Redo  | MPLAY |                      |       |       | WordL |       | WordR |vsNavB |vsNavF |
    #-------+-------+-------+-------+-------+-------+-------+-------+      +-------+-------+-------+-------+-------+-------+-------+-------+
    #               |       |       |       |       |       |       |      |       | BKSPC |       |       |       |       |
    #               +-------+       +-------+-------+-------+-------+      +-------+-------+-------+-------+       +-------+
    [
        KC.ESC,  KC.NO, KC.NO,    KC.NO,   KC.NO,  KC.VOLU,                                    KC.NO, KC.HOME,  KC.UP,   KC.END,   KC.PGUP,  KC.NO,
        KC.NO,   KC.NO, KC.LALT, KC.LCTL, KC.LSFT, KC.VOLD,                                    KC.NO, KC.LEFT, KC.DOWN, KC.RIGHT, KC.PGDOWN, KC.NO,
        KC.LSFT, Undo,   Cut,     Copy,    Paste,   Redo,                                      KC.NO,  WordL,   KC.NO,   WordR,    vsNavB,   vsNavF, 
                                                           KC.MPLY,                    KC.NO,
                        KC.NO,             KC.NO,   KC.NO,  KC.NO, KC.NO,      KC.NO, KC.BKSP, KC.NO, KC.NO,             KC.NO,
    ],

    # Symbol layer
    #-------+-------+-------+-------+-------+-------+                                      +-------+-------+-------+-------+-------+-------+
    #   `   |   !   |   @   |   #   |   $   |   %   |                                      |   ^   |   &   |   *   |   (   |   )   |   _   |
    #-------+-------+-------+-------+-------+-------|                                      |-------+-------+-------+-------+-------+-------|
    #   F1  |  F2   |  F3   |  F4   |  F5   |  F6   |                                      |   |   |   [   |   ]   |   {   |   }   |       |
    #-------+-------+-------+-------+-------+-------+-------+                      +-------+-------+-------+-------+-------+-------+-------|
    #   F7  |  F8   |  F9   |  F10  |  F11  |  F12  |       |                      |       |   /   |       |       |       |       |       |
    #-------+-------+-------+-------+-------+-------+-------+-------+      +-------+-------+-------+-------+-------+-------+-------+-------+
    #               | CTRL  |       | SHIFT |  ALT  | SPACE |       |      |       | BKSPC |       |       |       |       |
    #               +-------+       +-------+-------+-------+-------+      +-------+-------+-------+-------+       +-------+
    [
        KC.GRAVE,KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,                                     KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.UNDS,
        KC.F1,   KC.F2,   KC.F3,  KC.F4,  KC.F5,   KC.F6,                                      KC.PIPE,  KC.LBRC,   KC.RBRC,   KC.LCBR,   KC.RCBR,  KC.NO,
        KC.F7,   KC.F8,   KC.F9,  KC.F10, KC.F11,  KC.F12,                                     KC.PSLS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, 
                                                         KC.NO,                        KC.NO,
                         KC.LCTL,        KC.LSFT,  KC.LALT, KC.SPC, KC.NO,         KC.NO, KC.BKSP, KC.NO, KC.NO,     KC.NO,
    ],
]

print("Setup complete, time to get CLACK-A-LACK-ING!")

if __name__ == '__main__':
    keyboard.go()