#name<- snakemake@params[['name']]
name<- "input/Mendelian_1-10"
data <-paste(name, "rda", sep=".")
df <- load(data)

new_m <- cbind(m.subset,folds.subset)
new_m <- cbind(new_m,labels.subset)

file_txt <-  paste(name, "txt", sep=".")
write.table(new_m,file_txt,row.names = FALSE, col.names = FALSE, ,sep = "\t")
