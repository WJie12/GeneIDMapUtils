#BiocManager::install("org.Mm.eg.db")
require(org.Mm.eg.db)

data=data.frame(read.csv('D:/SynLethDBNewData/database2019/mouse.csv'),header=TRUE,colClasses=c(rep("character",402)),stringsAsFactors=F)

gene_a_id<-data[,2]
gene_a_id<-as.character(gene_a_id)
gene_a_symbol <- mget(gene_a_id,org.Mm.egSYMBOL,ifnotfound=NA)
gene_a_symbol.df <- do.call("rbind", lapply(gene_a_symbol, as.data.frame)) 

gene_b_id<-data[,4]
gene_b_id<-as.character(gene_b_id)
gene_b_symbol <- mget(gene_b_id,org.Mm.egSYMBOL,ifnotfound=NA)
gene_b_symbol.df <- do.call("rbind", lapply(gene_b_symbol, as.data.frame)) 
write.csv(cbind(gene_a_symbol.df,gene_b_symbol.df),"D:/SynLethDBNewData/database2019/sl_mouse_r.csv", row.names = FALSE)
