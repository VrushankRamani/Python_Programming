from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

ggplot(mpg) + aes(x="class", y="hwy") + geom_point()
