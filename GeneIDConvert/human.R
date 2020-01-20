#BiocManager::install("org.Hs.eg.db")
require(org.Hs.eg.db)

data=data.frame(read.csv('D:/SynLethDBNewData/database2019/human.csv'),header=TRUE,colClasses=c(rep("character",29496)),stringsAsFactors=F)

gene_a_id<-data[,2]
gene_a_id<-as.character(gene_a_id)
gene_a_symbol<-data.frame(mapIds(org.Hs.eg.db, keys=gene_a_id, column =c("SYMBOL"), 
                                 keytype="ENTREZID"))

gene_b_id<-data[,4]
gene_b_id<-as.character(gene_b_id)
gene_b_symbol <- data.frame(mapIds(org.Hs.eg.db, keys=gene_b_id, column =c("SYMBOL"), 
                                   keytype="ENTREZID"))
write.csv(cbind(gene_a_symbol,gene_b_symbol),"D:/SynLethDBNewData/database2019/sl_human_r.csv", row.names = FALSE)
