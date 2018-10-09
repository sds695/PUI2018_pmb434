
## 1. Verify the Null and alternative hypotheses


I think it is an interesting idea to test tourists' trips time against New Yorkers's trips time on CitiBikes, by guessing that tourists should have longer trips because they are visiting and exploring the city. It is also reasonable to use the average duration of trips as the measurements. The Null and alternative hypotheses are formulated correctly in both words and formula.

## 2. Verify that the data support the project:

The data was properly pre-processed by removing all the unrelated values and leaving only user types and trips duration. My concern is about how reliable is the assumption that Subscriber = New Yorker and Customer = Tourist.  It might be reasonable to assume subscribers are New Yorkers since they have a 1-year membership. But for customers, there are possibly New Yorkers who use city bikes regularly by only buying hourly or daily passes. So it would be better if you can find more information to support that assumption. 

Other than that, I think it would also be helpful to extract the means for the two groups separately (the average duration time of New Yorkers and the average duration time of tourists),  so you can compare them together to see which group have a longer trip time and how far are they from the total mean.  

For the plotting, while it makes sense to plot the density against trip durations to show what duration is the most common for each group, it will be more helpful if adding a comparison of the two group's trip duation means. For example, you can calculate the weekly trip duation means for each group,  and then in a histogram plot the two means next to each other for each week. It is a more straightforward way to show which group has a longer average duration. 


## 3. Choose an appropriate test to test H0 given the type of data, and the question asked.

I would suggest using z-test to test H0 given the type of data are the means of two large (n ≥ 30) samples. You can use New Yorker's mean and standard deviation to test how many standard deviations away is the tourists' mean. 


Written by: xh1163
