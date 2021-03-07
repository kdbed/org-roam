module Main

plusAssoc : (l, c, r : Nat) -> l `plus` (c `plus` r) = (l `plus` c) `plus` r
plusAssoc Z     c r = ?plusAssoc_rhs_1
plusAssoc (S l) c r = ?rhs_plusAssoc_2
