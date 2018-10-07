
## 1. Verify the Null and alternative hypotheses


I think it is an interesting idea to test the Tourists' trips time against New Yorkers's trips time on CitiBikes by guessing the tourists should have longer trips time than new yorkers because they are visiting and exploring the city. It is also reasonable to use the average duration of trips as the measurements. The Null and alternative hypotheses are formulated correctly in both words and formulae.

## 2. Verify that the data support the project:

The data was properly pre-processed by removing all the unrelated values other than user types and trips duration. My concern though is about how reliable it is to assume Subscriber = New Yorker and Customer = Tourist.  It might be reasonable to assume subscribers are New Yorkers since they have a 1-year membership. But for customers, as you mentioned,  there are also possibly New Yorkers who use city bikes regularly by only buying 4-hour o 3-day passes. So it would be better if you can find more information to support your assumption. 

Other than that, I saw you have extracted the mean of all trip durations. I think it would also be helpful to extract the means for the two groups separately (the mean duration time of New Yorkers and the mean duration time of tourists),  so you can compare them together to see which group have a longer trip time and how far are they from the total mean.  

For the plot, while it makes sense to plot the density against trip durations to show what duration is the most common for each group, I am not sure if it is the most straightforward way to compare the durations. Because although the plot tells the tourists are more common to have longer trips and New Yorkers are more common to have shorter trips, the higher density of new yorkers could be misleading at first.  

It will help reader to understand the data better if add a comparison of the means of the two groups (also to stay consistent with the null hypothesis formula). For example, you can calculate the weekly means for each group,  and then in a histogram plot the two means next to each other for each week, so the readers can simply compare the hight of bars to see which group has a longer average duration. 


## 3. Choose an appropriate test to test H0 given the type of data, and the question asked.


 I would suggest using z-test to test H0 given the type of data are the means of two populations, with large (n ≥ 30) samples. You can use New Yorker's mean and standard deviation to test how many standard deviations away is the tourists' mean. 
