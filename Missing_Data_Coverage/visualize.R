mix<-read.csv('Missing Data Coverage RR.csv') #[c(1:3,16:18)]
mix$Data.Source.Level.1<-as.numeric(as.character(mix$Data.Source.Level.1))
mix<-na.omit(mix)

#pdf('visualize.pdf',width=9,height=9)
png('visualize.png',width=700,height=700)
grey='#999999CC'
par(
	col=grey,
	col.axis=grey,
	col.lab=grey,
	col.main=grey,
	col.sub=grey,
	fg=grey
#	mar=c(5,10,4,10), # increase y-axis margin
#	par(las=2) # make label text perpendicular to axis
)

#Order 
#order(mix$Country.Level.1)
#order(mix$Data.Source.Level.1)
plot(Country.Level.1~Data.Source.Level.1,data=mix
 , bg=grey, col=0, pch=21, cex=sqrt(Count)
 , axes=F
 , main="Extent of missing data by country and data provider in Mix data" 
 , xlab="Data source (Down is low.)"
 , ylab="Country (Left is low.)"
 , sub="Circle areas correspond to the number of organizations reported"
)
axis(2,at=order(mix$Data.Source.Level.1),labels=mix$Data.Source..Organization.Name)
axis(1,at=order(mix$Country.Level.1),labels=mix$Country)
dev.off()
