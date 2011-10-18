mix<-read.csv('Missing Data Coverage RR.csv') #[c(1:3,16:18)]
mix$Data.Source.Level.1<-as.numeric(as.character(mix$Data.Source.Level.1))
mix<-na.omit(mix)

visualize<-function(mix,rank=F){
  if (rank) {
    print('Using ranks')
    rankify<-function(foo){
      order(foo)
    }
  } else {
    print('Using interval data')
    rankify<-function(foo){
      foo
    }
  }
 
  grey='#00000044'
  par(
    col=grey
  , col.axis=grey
  , col.lab=grey
  , col.main=grey
  , col.sub=grey
  , fg=grey
  #, mar=c(5,10,4,10) # increase y-axis margin
  , las=2 # make label text perpendicular to axis
  )
 
  plot(rankify(Country.Level.1)~rankify(Data.Source.Level.1),data=mix
  , bg=grey, col=0, pch=21, cex=sqrt(Count)
  , axes=F
  , main="Extent of missing data by country and data provider in Mix data" 
  , xlab="Data source, ordered by completeness of data (Down indicates more missing data.)"
  , ylab="Country, ordered by completeness of data (Down indicates more missing data.)"
  , sub="Circle areas correspond to the number of organizations reported"
  )
  makeaxis <- function(side,missingness,orgnames){
    axislabels<-aggregate(missingness,list(orgnames),unique)
    axis(side,at=rankify(axislabels$x),labels=axislabels$Group.1)
  }
  makeaxis(1,mix$Data.Source.Level.1,mix$Data.Source..Organization.Name)
  makeaxis(2,mix$Country.Level.1,mix$Country)
}

#pdf('visualize.pdf',width=9,height=9)
SIDE=1000
#png('visualize.png',width=SIDE,height=SIDE)
visualize(mix,rank=T)
#dev.off()
