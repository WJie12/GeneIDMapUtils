#if (!requireNamespace("BiocManager", quietly = TRUE))
#  install.packages("BiocManager")

#BiocManager::install("org.Ce.eg.db")
#BiocManager::install("twitteR")
require(org.Ce.eg.db)

wormdata=data.frame(read.csv('D:/SynLethDBNewData/database2019/worm.csv'),header=TRUE,colClasses=c(rep("character",114)),stringsAsFactors=F)

gene_a_id<-wormdata[,2]
gene_a_id<-as.character(gene_a_id)
gene_a_symbol <- mget(gene_a_id,org.Ce.egSYMBOL,ifnotfound=NA)
gene_a_symbol.df <- do.call("rbind", lapply(gene_a_symbol, as.data.frame)) 

gene_b_id<-wormdata[,4]
gene_b_id<-as.character(gene_b_id)
gene_b_symbol <- mget(gene_b_id,org.Ce.egSYMBOL,ifnotfound=NA)
gene_b_symbol.df <- do.call("rbind", lapply(gene_b_symbol, as.data.frame)) 
write.csv(cbind(gene_a_symbol,gene_b_symbol),"D:/SynLethDBNewData/database2019/sl_worm_r.csv", row.names = FALSE)

