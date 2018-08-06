setwd("D:\\IOTChallenge\\all")


library(data.table)

train_numeric_df <- fread("train_numeric.csv")

dim(train_numeric_df)
head(train_numeric_df)



train_cat_df <- fread("train_categorical.csv")
dim(train_cat_df)
head(train_cat_df)




train_dat_df <- fread("train_date.csv")

dim(train_dat_df)
head(train_numeric_df)





library(dplyr)


merged_df <- train_numeric_df%>%
  left_join(train_cat_df)

dim(merged_df)
merged_df <- merged_df%>%left_join(train_dat_df)
dim(merged_df)


write.csv(merged_df, "merged_df.csv",row.names = F, na=  '')






fwrite(merged_df, "merged_df.csv")





orig_col_df <- data.frame(coln = colnames())









test_numeric_df <- fread("test_numeric.csv")
dim(test_numeric_df)



test_cat_df <- fread("test_categorical.csv")
dim(test_cat_df)




test_dat_df <- fread("test_date.csv")
dim(test_dat_df)

library(dplyr)
t_merged_df <- test_numeric_df%>%
  left_join(test_cat_df)

dim(t_merged_df)
t_merged_df <- t_merged_df%>%left_join(test_dat_df)
dim(t_merged_df)

# > dim(test_numeric_df)
# [1] 1183748     969
# > dim(test_cat_df)
# [1] 1183748    2141
# > dim(test_dat_df)
# [1] 1183748    1157
# > dim(t_merged_df)
# [1] 1183748    4265



fwrite(t_merged_df, 't_merged_df.csv')

t_col_df <- data.frame(col_names = colnames(t_merged_df))


fwrite(t_col_df, 't_col_df.csv')
