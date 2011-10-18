mix<-read.csv('Missing Data Coverage RR.csv') #[c(1:3,16:18)]
mix$Data.Source.Level.1<-as.numeric(as.character(mix$Data.Source.Level.1))
mix<-na.omit(mix)

#Make the axis and labels, with optional ranking
makeaxis <- function(side,missingness,orgnames,plot=T,rank=F){
  axislabels.df<-aggregate(missingness,list(orgnames),unique)
  axislabels<-axislabels.df$x
  names(axislabels)<-axislabels.df$Group.1
  rm(axislabels.df)

  if (rank) {
    #print('Using ranks')
    rankify<-function(foo){
      order(foo)
    }
  } else {
    #print('Using interval data')
    rankify<-function(foo){
      foo
    }
  }

  if (plot) {
    axis(side,at=rankify(axislabels),labels=names(axislabels))
  }
  rankify(axislabels)
}


visualize<-function(mix,rank=F){
 
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
 
  x<-makeaxis(1,mix$Data.Source.Level.1,mix$Data.Source..Organization.Name,plot=F,rank=rank)
  y<-makeaxis(2,mix$Country.Level.1,mix$Country,plot=F,rank=rank)
  if (rank){
    ranklab<-" rank "
    rankparens<-" (ranks)"
  } else {
    ranklab<-" "
    rankparens<-""
  }
  xlab<-paste("Data source and",ranklab,"completeness of its data (Down indicates more missing data.)",sep='')
  ylab<-paste("Country and",ranklab,"completeness of its data (Down indicates more missing data.)",sep='')
 main<-paste("Extent of missing data by country and data provider",rankparens,sep='')

  plot(y[Country]~x[Data.Source..Organization.Name],data=mix
  , bg=grey, col=0, pch=21, cex=sqrt(Count)
  , axes=F
  , xlab=xlab
  , ylab=ylab
  , main=main
  , sub="Circle areas correspond to the number of organizations reported by the data source for the country"
  )
  makeaxis(1,mix$Data.Source.Level.1,mix$Data.Source..Organization.Name,rank=rank)
  makeaxis(2,mix$Country.Level.1,mix$Country,rank=rank)
  list(x=x,y=y)
}

pdf('visualize.pdf',width=9,height=9)
SIDE=1000
#png('visualize.png',width=SIDE,height=SIDE)
visualize(mix,rank=T)
visualize(mix,rank=F)
dev.off()
