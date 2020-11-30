; Keterangan status kotak
(deftemplate opened (slot no))
(deftemplate flagged (slot no))
(deftemplate prob (slot p) (slot id))

; Struct kotak minesweeper
(deftemplate square 
    ; no kotak
    (slot no)
    ; nilai kotak (banyaknya bom yang adjacent)
    (slot value)
    ; no kotak yang mengelilingi
    (multislot adjacent)
    ; banyaknya flag yang mengelilingi
    (slot nflags)
)

; Apabila banyak flag + unknown adjacent = value, maka flag kotak sisanya
(defrule flagAllAdjacent
    (declare (salience 2))
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
    (halt)
)

; Apabila banyak flag = value, maka buka kotak sisanya
(defrule openAllAdjacent
    (declare (salience 1))
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
    (halt)
)

; Remove prob fact if square is flagged beforehand
(defrule removeProbOnFlagged
    (declare (salience 1))
    ?pr <- (prob (p ?p) (id ?id))
    (flagged (no ?n&:(eq ?n ?id)))
=>
    (retract ?pr)
)

; Remove prob fact if square is opened beforehand
(defrule removeProbOnOpened
    (declare (salience 1))
    ?pr <- (prob (p ?p) (id ?id))
    (opened (no ?n&:(eq ?n ?id)))
=>
    (retract ?pr)
)

; ambil kotak dengan probabilitas terendah
(defrule getLowestProb
    ?todo1 <- (prob (p ?p1) (id ?id1))
    ?todo2 <- (prob (p ?p2 &: (< ?p1 ?p2)) (id ?id2))
=>
    (retract ?todo2)
)

; open square with lowest prob
(defrule openLowestProb
    (declare (salience -2))
    ?sq <- (prob (p ?p) (id ?id))
=>
    (assert (opened (no ?id)))
    (retract ?sq)
    (halt)
)