; Struct kotak minesweeper
(deftemplate square 
    ; id kotak
    (slot no)
    ; letak absis
    (slot absis)
    ; letak ordinat 
    (slot ordinat)
    ; nilai kotak (banyaknya bom yang surround)
    (slot value)
    ; id kotak yang mengelilingi
    (multislot surround)
    ; banyaknya flag yang mengelilingi
    (slot nflags)
)

; Nanti di generate menggunakan Python
(deffacts init
    (square
        (no 0)
        (absis 0)
        (ordinat 0)
        (value 0)
        (surround 1 8 9)
        (nflags 0)
    )
)