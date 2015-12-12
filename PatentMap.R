###########
# joe wrote this code on 10/8/2015 after the meeting last night
# edited the code on 11/20/2015 to get the json from the server and pass back
# edited again on 11/24/2015 to get the json ingestion working correctly
# the image pointer
###########
# install.packages("MASS")
# install.packages("plotrix")
# install.packages("jsonlite")

# this r code will take the matrix passed by the underlying Merilant Patent Match API
# after it is in a matrix (not symmetrical) and plot it on a patent map

# right now read in dataV2.json

# these are the two libraries needed to draw the plot
library(MASS) # may have to 'install.packages("MASS")' first
library(plotrix) #may have to 'install.packages("plotrix")' first
library("jsonlite")

# need to set up some kind of loop to go through all calls
# map_input <- read.csv(file="map_input.txt", header=FALSE)
# for (i in 1:50 ) {
#   print("joe")
# }

setwd("/Users/josephbailey/merilant/")

# json_file <- "http://patent.umd.edu/datav5.json"
json_file <- "patentScores.json"
neighbors <- fromJSON(json_file)

# we start with the threshold defined by the user where 0 is an exact match and 1 is
# all matches; I've hardcoded this to be a 25% threshold
threshold <- 0.25

# this does the mds (multidimensional scaling)
d <- dist(neighbors)
fit <- isoMDS(d, k=2)
x <- fit$points[,1]
y <- fit$points[,2]

# this makes the x and y scales symmetrical based on the range of values for x and y
# we probably need to rethink this so that the scales are consistent across runs
range <- max(-1*min(x),max(x),-1*min(y),max(y))
x <- x/range
y <- y/range

# now the plot is drawn first with the values, then with the center point, and then with the circle
jpeg('rplot.jpeg')
plot(x, y, xlab="", ylab="", col="blue", main="Patent Map", type="p", xlim=c(-1.2,1.2),ylim=c(-1.2,1.2))
points(0,0, col="black")
draw.circle(0,0,threshold,border="red")
dev.off()

# in case I need to export the json:
# exportJson <- toJSON(neighbors_sub, pretty=TRUE)
# write(exportJson, file="datav5.json")

