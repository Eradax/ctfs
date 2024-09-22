{-# LANGUAGE UndecidableInstances #-}
{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE TypeOperators #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE AllowAmbiguousTypes #-}
{-# OPTIONS_GHC -freduction-depth=0 #-}

data Z -- 0
data S n -- S(n) = n+1

-- Sums two numbers
class PAdd a b r | a b -> r -- PAdd(a, b) = a + b = r
instance PAdd Z Z Z -- 0 + 0 = 0
instance PAdd Z (S x) (S x) -- 0 + (x + 1) = x + 1
instance (PAdd x y z) => PAdd (S x) y (S z) -- x + y = z -> (x + 1) + y = z + 1


-- Multiplies two numbers
class PMul a b r | a b -> r -- PMul(a, b) = a * b = r
instance PMul x Z Z -- PMul(x, 0) = 0
instance PMul Z x Z -- PMul(0, x) = 0
instance (PMul x y xy, PAdd x xy xxy) => PMul x (S y) xxy
-- x * y = xy AND x + xy = x + x*y = xxy -> x * (y + 1) = xxy

-- True and false values
data T -- 1
data F -- 0

-- Takes and of two values
class And a b c | a b -> c -- a & b
instance And T T T -- 1 & 1 = 1
instance And T F F -- 1 & 0 = 0
instance And F T F -- 0 & 1 = 0
instance And F F F -- 0 & 0 = 0

-- Tells if two values are equal
class PEq a b c | a b -> c -- PEq(a, b) = a == b = c
instance PEq Z Z T -- 0 == 0
instance PEq (S x) Z F -- x + 1 != 0
instance PEq Z (S y) F -- 0 != y + 1
instance (PEq x y z) => PEq (S x) (S y) z -- x ?= y -> x+1 ?= y+1

data E -- Empty data type
data x ::: xs -- list const
infixr 5 ::: -- ::: right associative precedence

-- Takes a list and says if all values are E followed by true
class All a b | a -> b -- All(a) = b
instance All E T -- All(e) = 1
instance All (F ::: l) F -- All(0, l) = 0
instance (All l t) => All (T ::: l) t -- All(l) -> All(T, l)

-- Length of list
class Length a b | a -> b -- Length(a) = b
instance Length E Z -- Length(E) = 0
instance (Length xs r) => Length (x:::xs) (S r) -- Length(xs) = r -> Length(x,xs) = r + 1

class Apply f a b | f a -> b -- functions (equal function? i.e. they are the same type)
class MapMany f a b | f a -> b -- functions over lists

instance MapMany E E E -- E(E) = E
instance MapMany E (x ::: xs) E -- E(x,xs) = E
instance MapMany (x ::: xs) E E -- (x, xs)(E) = E
instance (Apply f a b, MapMany fs as bs) => MapMany (f:::fs) (a:::as) (b:::bs)
-- f(a) = b AND fs(as) = bs -> (f,fs)(a, as) = (b, bs)

data C0 -- t
data C1
data C2
data C3
data C4
data C5 -- _
data C6
data C7
data C8
data C9
data C10
data C11
data C12
data C13
data C14
data C15
data C16
data C17
data C18
data C19
data C20
instance (PAdd e (S Z) d, PEq b f a, PMul (S (S (S Z))) x c, PMul (S (S (S (S (S Z))))) (S (S Z)) h, PMul g (S (S (S (S (S (S (S Z))))))) f, PAdd h (S Z) g, PAdd c d b, PMul (S (S (S (S Z)))) (S (S (S (S Z)))) e) => Apply C0 x a
instance (PMul (S (S (S (S Z)))) (S (S Z)) k, PMul d x c, PAdd k (S Z) j, PMul (S (S (S (S Z)))) (S (S (S Z))) e, PEq b f a, PMul (S (S (S (S Z)))) (S (S (S (S (S (S Z)))))) d, PAdd c e b, PAdd i (S Z) h, PMul (S (S (S (S Z)))) (S (S (S (S Z)))) i, PMul g j f, PMul h (S (S (S (S Z)))) g) => Apply C1 x a
instance (PMul j (S (S (S (S (S (S Z)))))) i, PAdd c e b, PMul (S (S (S (S (S Z))))) (S (S Z)) k, PAdd i (S Z) h, PMul d x c, PMul h (S (S (S Z))) g, PAdd f (S Z) e, PMul (S (S (S (S Z)))) (S (S Z)) f, PEq b g a, PAdd k (S Z) j, PMul (S (S (S (S Z)))) (S (S (S Z))) d) => Apply C2 x a
instance (PMul (S (S (S (S Z)))) (S (S (S (S (S (S Z)))))) d, PMul k (S (S (S (S (S (S Z)))))) j, PAdd j (S Z) i, PMul (S (S (S (S (S Z))))) (S (S Z)) k, PAdd c e b, PMul g (S (S Z)) f, PAdd h (S Z) g, PEq b f a, PMul d x c, PMul i (S (S (S (S (S (S Z)))))) h, PMul (S (S (S (S (S (S (S Z))))))) (S (S Z)) e) => Apply C3 x a
instance (PMul (S (S Z)) x c, PAdd c d b, PAdd e (S Z) d, PAdd i (S Z) h, PAdd g (S Z) f, PEq b f a, PMul (S (S (S (S Z)))) (S (S Z)) j, PMul (S (S (S (S (S Z))))) j i, PMul (S (S (S (S (S (S Z)))))) (S (S (S Z))) e, PMul h (S (S Z)) g) => Apply C4 x a
instance (PMul (S (S (S (S Z)))) (S (S (S (S Z)))) d, PMul d x c, PAdd c (S (S (S Z))) b, PEq b (S (S (S Z))) a) => Apply C5 x a
instance (PAdd l (S Z) k, PAdd g (S Z) f, PMul m (S (S (S (S (S Z))))) l, PMul i (S (S Z)) h, PEq b h a, PMul n (S (S Z)) m, PMul f (S (S Z)) e, PAdd c e b, PMul d x c, PAdd j (S Z) i, PAdd o (S Z) n, PMul k (S (S Z)) j, PMul (S (S (S (S Z)))) (S (S (S (S (S (S Z)))))) d, PMul (S (S (S (S (S (S Z)))))) (S (S (S Z))) o, PMul (S (S (S (S (S Z))))) (S (S Z)) g) => Apply C6 x a
instance (PMul (S (S (S (S Z)))) (S (S Z)) e, PEq b f a, PMul (S (S (S (S Z)))) (S (S Z)) l, PAdd c e b, PMul j (S (S Z)) i, PMul (S (S (S (S Z)))) (S (S (S (S (S Z))))) d, PAdd i (S Z) h, PMul (S (S (S (S (S Z))))) (S (S Z)) k, PAdd k (S Z) j, PMul d x c, PMul g l f, PMul h (S (S Z)) g) => Apply C7 x a
instance (PAdd l (S Z) k, PMul d x c, PMul (S (S (S (S Z)))) (S (S Z)) g, PAdd g (S Z) f, PAdd c f b, PAdd j (S Z) i, PEq b h a, PMul i k h, PMul (S (S (S (S (S Z))))) (S (S (S (S (S (S Z)))))) j, PAdd e (S Z) d, PMul (S (S (S (S Z)))) (S (S Z)) l, PMul (S (S (S (S Z)))) (S (S Z)) e) => Apply C8 x a
instance (PMul e (S (S Z)) d, PAdd f (S Z) e, PAdd c g b, PMul d x c, PMul (S (S (S (S (S (S (S Z))))))) (S (S Z)) g, PMul (S (S (S (S (S (S (S Z))))))) (S (S Z)) h, PEq b h a, PMul (S (S (S (S (S Z))))) (S (S Z)) f) => Apply C9 x a
instance (PMul m (S (S (S (S Z)))) l, PAdd p (S Z) o, PMul k (S (S Z)) j, PMul d x c, PAdd n (S Z) m, PMul (S (S (S (S Z)))) (S (S (S Z))) i, PMul (S (S (S (S Z)))) (S (S (S Z))) p, PMul o (S (S (S (S (S (S Z)))))) n, PEq b j a, PMul (S (S (S (S (S Z))))) (S (S Z)) g, PAdd c h b, PMul f (S (S Z)) e, PAdd i (S Z) h, PAdd e (S Z) d, PAdd g (S Z) f, PAdd l (S Z) k) => Apply C10 x a
instance (PEq b f a, PMul g j f, PMul (S (S (S (S Z)))) (S (S Z)) k, PMul (S (S (S (S (S (S (S Z))))))) (S (S Z)) e, PMul h (S (S Z)) g, PAdd i (S Z) h, PAdd c e b, PAdd k (S Z) j, PMul (S (S (S (S Z)))) (S (S (S Z))) i, PMul (S (S (S (S (S Z))))) (S (S Z)) d, PMul d x c) => Apply C11 x a
instance (PMul (S (S (S (S (S (S (S Z))))))) (S (S (S Z))) f, PMul j l i, PAdd i (S Z) h, PAdd e (S Z) d, PEq b g a, PMul (S (S (S (S Z)))) (S (S (S (S Z)))) k, PAdd c f b, PMul h (S (S (S Z))) g, PMul (S (S (S (S Z)))) (S (S (S Z))) e, PMul (S (S (S (S Z)))) (S (S Z)) l, PMul d x c, PAdd k (S Z) j) => Apply C12 x a
instance (PEq b d a, PMul (S (S (S (S Z)))) (S (S (S (S (S (S Z)))))) d, PAdd c (S (S (S (S (S (S Z)))))) b, PMul (S Z) x c) => Apply C13 x a
instance (PMul d x c, PAdd c e b, PEq b f a, PMul (S (S (S (S Z)))) (S (S (S (S (S (S Z)))))) e, PAdd h (S Z) g, PMul (S (S (S (S (S (S (S Z))))))) (S (S Z)) d, PMul (S (S (S (S (S Z))))) (S (S (S (S (S (S Z)))))) h, PMul g i f, PMul (S (S (S (S Z)))) (S (S Z)) i) => Apply C14 x a
instance (PMul (S (S (S (S Z)))) (S (S (S Z))) d, PAdd f (S Z) e, PEq b e a, PMul d x c, PMul g (S (S (S (S (S (S Z)))))) f, PMul (S (S (S (S (S Z))))) (S (S Z)) i, PMul h (S (S (S (S (S Z))))) g, PAdd i (S Z) h, PAdd c (S (S (S (S (S (S (S Z))))))) b) => Apply C15 x a
instance (PMul (S (S (S (S (S Z))))) (S (S Z)) f, PMul d x c, PMul h k g, PAdd f (S Z) e, PMul (S (S (S (S Z)))) (S (S Z)) j, PAdd c (S (S (S (S (S (S Z)))))) b, PMul (S (S (S (S Z)))) (S (S Z)) k, PEq b g a, PMul (S (S (S (S Z)))) (S (S Z)) i, PMul e (S (S Z)) d, PMul i j h) => Apply C16 x a
instance (PMul d x c, PEq b h a, PAdd c e b, PMul (S (S (S (S (S Z))))) (S (S Z)) l, PMul l (S (S (S (S (S Z))))) k, PMul i (S (S Z)) h, PMul f (S (S Z)) e, PAdd j (S Z) i, PMul (S (S (S (S Z)))) (S (S (S (S Z)))) d, PAdd g (S Z) f, PMul k (S (S (S (S (S Z))))) j, PMul (S (S (S (S (S Z))))) (S (S Z)) g) => Apply C17 x a
instance (PMul (S (S (S (S (S (S Z)))))) (S (S (S Z))) e, PAdd e (S Z) d, PMul d x c, PEq b f a, PMul (S (S (S (S (S (S Z)))))) (S (S (S (S (S (S (S Z))))))) h, PAdd h (S Z) g, PMul (S (S (S (S Z)))) (S (S Z)) i, PMul g i f, PAdd c (S (S Z)) b) => Apply C18 x a
instance (PMul (S (S (S (S (S (S (S Z))))))) (S (S (S Z))) d, PMul d x c, PAdd c (S (S (S Z))) b, PEq b e a, PMul f g e, PMul (S (S (S (S Z)))) (S (S Z)) h, PMul (S (S (S (S Z)))) (S (S (S Z))) f, PAdd h (S Z) g) => Apply C19 x a
instance (PMul d x c, PMul (S (S (S (S (S Z))))) (S (S Z)) d, PMul (S (S (S (S (S Z))))) (S (S Z)) h, PMul g (S (S (S (S (S Z))))) f, PMul (S (S (S (S (S Z))))) (S (S (S Z))) e, PAdd c e b, PAdd h (S Z) g, PEq b f a) => Apply C20 x a
type Cs = C0 ::: C1 ::: C2 ::: C3 ::: C4 ::: C5 ::: C6 ::: C7 ::: C8 ::: C9 ::: C10 ::: C11 ::: C12 ::: C13 ::: C14 ::: C15 ::: C16 ::: C17 ::: C18 ::: C19 ::: C20 ::: E

class CheckFlag f r | f -> r
instance (MapMany Cs f a, Length Cs cl, Length f fl, PEq cl fl e, All a t, And e t r) => CheckFlag f r
-- Cs(f) = a, len(Cs) = cl, len(f) = fl, (cl == fl) = e, All(a) = t, e AND t = r -> return r

class ToString t where toString :: t -> String
instance ToString T where toString _ = "Correct!!"
instance ToString F where toString _ = "Incorrect!!"

success :: CheckFlag Flag a => a
success = undefined

main :: IO()
main = putStrLn (toString success)

--- Klistra in flaggan från 'gen_flag.py' på nästa rad ---
type Flag = (S (S (S (S (S (S (S (S (S (S (S (S Z)))))))))))) ::: (S (S (S (S (S (S (S (S (S (S (S (S (S (S (S Z))))))))))))))) ::: (S (S (S (S (S (S (S (S (S (S (S (S Z)))))))))))) ::: E
