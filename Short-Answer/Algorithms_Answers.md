#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
We are setting something to zero and we have to loop over every element that we get in order to complete our calculation. We can trace this by following along the code and counting.
b)
O(n) -> n being the length or range of data passing through.
We are setting something to zero and we have to loop over every element that we get in order to complete our calculation. We can trace this by following along the code and counting.

c)
O(2^n) because of recursion.
## Exercise II

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->

I would do Binary Search with this particular problem. If n = 100 I would go to floor 50 and drop an egg. Egg will probably break so I know not to go any higher and now divide 50 in half. So then I would go to floor 25 and drop the egg. If it does not break then I know a floor between 25 and 50 is the limit. I would then go to the middle of those floors and basically repeat this process until I have my answer.

Runtime of this would be O(log n)