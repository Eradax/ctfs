{-# LANGUAGE RecursiveDo, LambdaCase #-}
import Control.Monad
import Data.Functor.Identity
import Control.Monad.Trans.Class
import Debug.Trace
import System.IO.Unsafe
import System.IO
import Control.Monad.Trans.Random
import Control.Monad.Random.Class
import System.Random
import Data.Tuple.Extra
import Data.Maybe
import Data.Bool
import Data.List
import System.Exit
import Data.Char

data Tree a = Leaf a | Node (Tree a) (Tree a) deriving (Eq)
-- Tree is a binary tree

data Bit = One | Zero deriving (Eq)
-- One bit i.e. 1 or 0

type BitString = [Bit]
-- list of bits

parseBitString :: String -> BitString
parseBitString = map (\case '0' -> Zero; '1' -> One;)
-- Takes string of 0s and 1s and transforms it to a bitstring

left :: Tree a -> Tree a
left (Leaf x) = Leaf x
left (Node x _) = x
-- Gets the left child of a node

right :: Tree a -> Tree a
right (Leaf x) = Leaf x
right (Node _ x) = x
-- Gets the right child of a node

leaf :: Tree a -> Bool
leaf (Leaf _) = True
leaf _ = False
-- Returns true if node is a leaf

val :: Tree a -> Maybe a
val (Leaf x) = Just x
val _ = Nothing
-- Gets the value of the node if it's a leaf otherwise return nothing

decodeCh :: Tree a -> BitString -> (Maybe a, BitString)
decodeCh (Leaf x) a = (Just x, a)
decodeCh t [] = (Nothing, [])
decodeCh t (c:cs) = decodeCh ((if c == One then left else right) t) cs
-- Goes through tree according to bitstring and returns the value of the node
-- and the rest of the bitstring

decode :: Tree a -> BitString -> ([a], BitString)
decode t b = let (r, b') = decodeCh t b in if isNothing r then ([], b) else (fromJust r :) `first` decode t b'
-- Returns the values of leafs in Tree, following BitString

encodeCh :: Eq a => Tree a -> a -> BitString
encodeCh (Leaf x) _ = []
encodeCh t c = v
  where (a, b) = (uncurry (&&&) $ uncurry `both` ((.left) &&& (.right)) encodeCh) (t, c)
        (d, e) = decodeCh t `both` (One:a, Zero:b)
        v = if Just c == fst d then One:a else Zero:b
-- Generates a bitstring s.t. we can call decodeCh and get the value

encode :: Eq a => Tree a -> [a] -> BitString
encode t = concatMap (encodeCh t)
-- Appends encodeCh(i) for each i in t

invert :: Bit -> Bool -> Bit
invert x False = x
invert One True = Zero
invert Zero True = One
-- Bit ^ Bool

flips :: [Bool] -> BitString -> BitString
flips = zipWith $ flip invert
-- [Bool] ^ BitString

scramble :: RandomGen r => Tree a -> Rand r (Tree a)
scramble x = do
  r <- getRandom

  if leaf x then return x else do
    y <- scramble (left x)
    z <- scramble (right x)

    return (bool flip id r Node z y)
-- Flips left and right children randomly


scrambleTree :: (Eq a, RandomGen b) => b -> Tree a -> (Tree a, b)
scrambleTree r t = runRand (scramble t) r
-- Runs scramble with a random b on a tree a

unscramble r t (l, xs) = fst (decode t . flips bs . (++ xs) . encode t' $ l)
  where (t', r') = scrambleTree r t
        bs = randoms r'


scrambledTree :: Tree Char
-- scrambledTree = Node (Node (Leaf 'a') (Leaf 'b')) (Node (Leaf 'c') (Leaf 'd'))
scrambledTree = Node (Node (Node (Node (Node (Node (Leaf '0') (Node (Node (Leaf 'H') (Leaf 'f')) (Leaf 'a'))) (Leaf 'p')) (Leaf 's')) (Node (Node (Leaf '}') (Leaf 'R')) (Leaf 'E'))) (Node (Node (Node (Node (Leaf 'K') (Node (Leaf '3') (Leaf 'O'))) (Node (Node (Leaf '9') (Leaf 'v')) (Node (Leaf 'I') (Node (Leaf 'e') (Leaf 'V'))))) (Node (Leaf 'G') (Leaf '7'))) (Node (Node (Node (Node (Node (Leaf 'Q') (Leaf '{')) (Leaf 'l')) (Node (Node (Leaf 'd') (Leaf '5')) (Node (Node (Leaf 'C') (Leaf 'k')) (Leaf 't')))) (Node (Leaf 'S') (Node (Node (Node (Node (Node (Leaf 'j') (Node (Leaf 'h') (Leaf 'X'))) (Node (Leaf 'J') (Leaf 'c'))) (Node (Leaf 'B') (Leaf 'F'))) (Node (Leaf 'U') (Node (Leaf 'M') (Leaf 'm')))) (Leaf '1')))) (Node (Node (Leaf 'T') (Leaf 'Y')) (Node (Leaf 'A') (Leaf 'w')))))) (Node (Node (Node (Node (Node (Node (Node (Leaf 'i') (Leaf 'b')) (Node (Leaf 'x') (Node (Leaf 'o') (Leaf 'D')))) (Leaf '_')) (Node (Leaf 'Z') (Node (Node (Node (Leaf '8') (Node (Node (Leaf '6') (Leaf '2')) (Leaf 'W'))) (Leaf 'g')) (Leaf 'P')))) (Node (Node (Leaf 'u') (Leaf 'L')) (Leaf 'z'))) (Node (Node (Node (Leaf 'r') (Leaf 'n')) (Leaf 'N')) (Leaf '4'))) (Node (Leaf 'y') (Leaf 'q')))

---

bitStringToString :: BitString -> String
bitStringToString = map (\case Zero -> '0'; One -> '1';)

calcFlipl :: RandomGen r => Tree a -> Rand r BitString
calcFlipl t = do
  r <- getRandom
  if leaf t then trace ("R: " ++ show r) (return [if r then One else Zero]) else do
    ll <- calcFlipl(left t)
    rr <- calcFlipl(right t)

    if r 
      then trace ("R: " ++ show r) (return ([One] ++ ll ++ rr))
      else trace ("R: " ++ show r) (return ([Zero] ++ ll ++ rr))

runCalcFlipl :: RandomGen b => b -> Tree a -> BitString
runCalcFlipl r t = (fst (runRand (calcFlipl t) r))

flipl :: BitString
flipl = runCalcFlipl (mkStdGen 420) scrambledTree

---

munscramble :: Tree a -> Int -> (Tree a, Int)
munscramble x i =
  let r = flipl!!i in
  trace ("r: " ++ show (r == One) ++ " i: " ++ show i) (

  if leaf x then (x, i+1)
  else
    let nn = if (r == One) then Node (right x) (left x) else Node (left x) (right x)
        (al, ni) = munscramble (left nn) (i + 1)
        (ar, ai) = munscramble (right nn) (ni)
    in (Node al ar, ai)
    )

munscrambleTree :: (Eq a) => Tree a -> (Tree a)
munscrambleTree t = fst (munscramble t 0)

---

tree :: Tree Char
tree = munscrambleTree scrambledTree

splitOn :: Char -> String -> (String, String)
splitOn c [] = ("", "")
splitOn c xs = (takeWhile (/= c) xs, drop 1 $ dropWhile (/= c) xs)

main :: IO ()
main = do
  let r = mkStdGen 420

  if fst (scrambleTree r tree) /= scrambledTree then
    die "Not the correct tree!"
  else do
    putStrLn "Welcome to REAL haskell hours."
    putStrLn "Please input the encrypted flag"
    putStr "> "

    flag <- getLine
    let d = parseBitString `second` splitOn ':' flag

    putStrLn $ "The flag is: " ++ unscramble r tree d
