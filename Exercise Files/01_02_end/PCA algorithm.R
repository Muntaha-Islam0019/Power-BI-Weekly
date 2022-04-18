dataset = read.csv('C:/Users/LinkedIn Instructor/Desktop/Exercise Files/Data Sources/New York City weather.csv')
dataset$date <- as.Date(dataset$date)
dataset <- dataset[complete.cases(dataset) & (format(dataset$date,"%Y") >= 2010),]
View(dataset)

pca <- prcomp(~ dataset$TMIN + dataset$TMAX)

pca_space <- data.frame(pca$x)
pca_space$date <- dataset$date
View(pca_space)

data <- merge(dataset, pca_space, by = "date")
View(data)