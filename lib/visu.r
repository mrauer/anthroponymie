library("ggplot2")

options(warn=-1)

jpeg('data/chart.jpg', width = 465, height = 225, units='mm', res = 600, pointsize=16)

data <- read.table("data/nat2018_labeled.csv", header=TRUE, sep=";")

data <- subset(data, data$annais!="XXXX" 
    & data$annais!=1935
    & data$annais!=1934
    & data$annais!=1933
    & data$annais!=1932
    & data$annais!=1931
    & data$annais!=1930
    & data$annais!=1929
    & data$annais!=1928
    & data$annais!=1927
    & data$annais!=1926
    & data$annais!=1925
    & data$annais!=1924
    & data$annais!=1923
    & data$annais!=1922
    & data$annais!=1921
    & data$annais!=1920
    & data$annais!=1919
    & data$annais!=1918
    & data$annais!=1917
    & data$annais!=1916
    & data$annais!=1915
    & data$annais!=1914
    & data$annais!=1913
    & data$annais!=1912
    & data$annais!=1911
    & data$annais!=1910
    & data$annais!=1909
    & data$annais!=1908
    & data$annais!=1907
    & data$annais!=1906
    & data$annais!=1905
    & data$annais!=1904
    & data$annais!=1903
    & data$annais!=1902
    & data$annais!=1901
    & data$annais!=1900)

year <- data$annais
cluster <- data$cluster
count <- data$nombre
data <- data.frame(data$annais, data$nombre, data$cluster)

ggplot(data, aes(fill=cluster, y=count, x=year)) + 
    geom_bar(position="fill", stat="identity", width=1) + 
    ggtitle("Proportion des naissances en France par Cluster Culturel") +
    scale_y_continuous(labels = scales::percent) +
    xlab("Année") + ylab("Proportion") +
    theme_grey(base_size = 22) +
    theme(axis.text.x = element_text(angle = 90, size = 12), plot.title = element_text(size = 32, face = "bold"))

dev.off()
