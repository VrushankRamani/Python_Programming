
from plotnine import *
from plotnine.data import mtcars
print(mtcars.head())


(ggplot(data=mtcars)
 + geom_point(mapping=aes(x="wt", y="mpg", color="factor(gear)"))
 + facet_wrap("~gear"))


(ggplot(data=mtcars)
 + geom_point(aes("wt", "mpg", color="factor(gear)"))
)


(ggplot(data=mtcars)
 + geom_point(aes("wt", "mpg", size="factor(gear)"))
)


(ggplot(data=mtcars)
+ geom_point(aes("wt", "mpg"), color='red')
)
