trapIntegrate :: Int
              -> (Double -> Double)
              -> Double
              -> Double
              -> Double
trapIntegrate n f a b
    = let dx          = (b - a) / fromIntegral n
          leftSides   = [a, a + dx .. b - dx]
          trapArea x  = 0.5 * (f x + f (x+dx)) * dx
      in sum $ map trapArea leftSides
