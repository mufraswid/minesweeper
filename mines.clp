; Keterangan status kotak
(deftemplate opened (slot no))
(deftemplate flagged (slot no))
(deftemplate prob (slot p) (slot id))

; Struct kotak minesweeper
(deftemplate square 
    ; no kotak
    (slot no)
    ; letak absis
    (slot absis)
    ; letak ordinat 
    (slot ordinat)
    ; nilai kotak (banyaknya bom yang adjacent)
    (slot value)
    ; no kotak yang mengelilingi
    (multislot adjacent)
    ; banyaknya flag yang mengelilingi
    (slot nflags)
)

; Nanti di generate menggunakan Python
(deffacts init
    (opened (no 0))
    (square
        (no 0)
        (absis 0)
        (ordinat 0)
        (value 0)
        (adjacent 1 8 9 10 11)
        (nflags 1)
    )
)

; Apabila banyak flag + unknown adjacent = value, maka flag kotak sisanya
(defrule flagAllAdjacent
	?cursquare <- (square
		(value ?v &: (> ?v 0))
		(nflags ?nf)
		(adjacent $?a &: (eq (+ (length$ $?a) ?nf) ?v))
    )
=>
    (foreach ?square $?a 
        (assert (flagged (no ?square)))
    )
    (retract ?cursquare)
)

; Apabila banyak flag = value, maka buka kotak sisanya
(defrule openAllAdjacent
	?cursquare <- (square
		(value ?v)
		(nflags ?n &: (eq ?n ?v))
		(adjacent $?a)
    )
=>
    (foreach ?square $?a 
        (assert (opened (no ?square)))
    )
    (retract $cursquare)
)

; ambil kotak dengan probabilitas terendah
(defrule getLowestProb
    ?todo1 <- (prob (p ?p1) (id ?id1))
    ?todo2 <- (prob (p ?p2 &: (< ?p1 ?p2)) (id ?id2))
=>
    (retract ?todo2)
)
