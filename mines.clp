; Keterangan status kotak
(deftemplate opened(slot no))
(deftemplate flagged(slot no))
(deftemplate closed(slot no))

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
    (square
        (no 0)
        (absis 0)
        (ordinat 0)
        (value 0)
        (adjacent 1 8 9)
        (nflags 0)
    )
)


; Generate kotak adjacent
(deffunction generateAllAdjacent (?size ?no ?absis ?ordinat $?curadj) 
    ; Generate adjacent kanan dan kiri
	(bind $?left (create$  (- (- ?no ?size) 1) (- ?no 1) (- (+ ?no ?size) 1)))
	(bind $?right (create$ (+ (- ?no ?size) 1) (+ ?no 1) (+ (+ ?no ?size) 1)))
    ; Generate adjacent atas
	(bind $?above (create$ (- (- ?no ?size) 1) (- ?no ?size) (+ (- ?no ?size) 1)))
    ; Generate adjacent bawah
	(bind $?below (create$ (- (+ ?no ?size) 1) (+ ?no ?size) (+ (+ ?no ?size) 1)))
    (bind $?adjacent (explode$ ""))
	(if (eq (+ ?ordinat 1) ?size) then 
    	(insert$ $?adjacent 1 $?above)
    	(insert$ $?adjacent 1 $?left)
    	(insert$ $?adjacent 1 $?right)
    )
	(if (eq ?ordinat 0) then 
    	(insert$ $?adjacent 1 $?below)
    	(insert$ $?adjacent 1 $?left)
    	(insert$ $?adjacent 1 $?right)
    )
	(if (eq (+ ?absis 1) ?size) then 
        (insert$ $?adjacent 1 $?below)
    	(insert$ $?adjacent 1 $?left)
    	(insert$ $?adjacent 1 $?above)
    )
	(if (eq ?absis 0) then 
        (insert$ $?adjacent 1 $?below)
    	(insert$ $?adjacent 1 $?above)
    	(insert$ $?adjacent 1 $?right)
    )
	(return $?adjacent)
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
        (bind $?nullarray (explode$ ""))
        (modify ?cursquare (nflags (+ ?nf 1)))
        (modify ?cursquare (adjacent $?nullarray))
    )
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
        (bind $?nullarray (explode$ ""))
        (bind $?nullarray (explode$ ""))
        (modify ?cursquare (adjacent $?nullarray)) 
    )
)

