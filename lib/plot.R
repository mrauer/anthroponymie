options(scipen=999)
pdf("rplot.pdf") 
df <- read.csv('/usr/src/app/data/nat2018_agg.csv', sep = ";")
interaction.plot(df[,2],
df[,1], df[,3],

            lty = 1,
                 lwd = 2,

xlab="Années", ylab="Naissances", col=rainbow(10), legend = TRUE, main = "Naissances par Groupe Culturels", trace.label = "Groupe Culturel") 
dev.off()