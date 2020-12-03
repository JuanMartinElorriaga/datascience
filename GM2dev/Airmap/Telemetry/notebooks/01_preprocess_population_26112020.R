# DATA CONSOLIDATION AND PRE-PROCESSING FOR TELEMETRY FILES
librerias <- c("lubridate", "dplyr", "readr", "janitor", "data.table")
invisible(lapply(librerias, library,  character.only = T))

# recursive list of .tsv files, beginning from root folder
paths_tsv <- list.files(
  path = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'data', 'raw', 'population', '2020'),
  recursive = T, include.dirs = T, pattern = "*.tsv$", full.names = T)

# merge all .tsv files into a final DF 
# DF_FINAL <- bind_rows(lapply(paths_tsv, fread, verbose=T, fill=T)) # data table
DF_FINAL <- bind_rows(lapply(paths_tsv, read_tsv, na="")) # readr 


# PRE-PROCESSING
# clean column names and remove cols and rows which are entirely empty
DF_FINAL <- DF_FINAL %>% clean_names() %>% remove_empty(which = c("rows","cols"))

# Modification of TIME columns
time_cols <-  c("observed", "received")
# remove scientific format
DF_FINAL[time_cols] <- lapply(DF_FINAL[time_cols], format, scientific=F)
# keep only first 10 digits, since its written in EPOCH TIME
left = function(text, num_char) {
  substr(text, 1, num_char)
}
DF_FINAL[time_cols] <- lapply(DF_FINAL[time_cols], left, 10)
# format as integer
DF_FINAL[time_cols] <- lapply(DF_FINAL[time_cols], as.integer)
# finally, format as datetime (lubridate)
DF_FINAL[time_cols] <- lapply(DF_FINAL[time_cols], as_datetime)

# new columns based on "received" time
DF_FINAL$date   <- format(DF_FINAL$received, format = "%Y-%m-%d")
DF_FINAL$time   <- format(DF_FINAL$received, format = "%H:%M:%S")
DF_FINAL$year   <- format(DF_FINAL$received, format = "%Y")
DF_FINAL$month  <- format(DF_FINAL$received, format = "%m")
DF_FINAL$day    <- format(DF_FINAL$received, format = "%d")
DF_FINAL$hour   <- format(DF_FINAL$received, format = "%H")
DF_FINAL$minute <- format(DF_FINAL$received, format = "%M")
DF_FINAL$second <- format(DF_FINAL$received, format = "%S")

# export to unique .tsv
write_tsv(x = DF_FINAL, na = "", col_names = T, 
          file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'data', 'interim', "full_DB_30112020.tsv"))



# write_tsv(x = DF_stats, na = "", col_names = T, 
#           file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'reports', "DF_stats.tsv"))
# 
# write_tsv(x = DF_status, na = "", col_names = T, 
#           file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'reports', 'DF_status.tsv'))
# 
# write_tsv(x = prof_num, na = "", col_names = T, 
#           file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'reports', 'prof_num.tsv'))



write_tsv(x = DF_trackid_date, na = "", col_names = T, file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'reports', 'track_id_date.tsv'))
write_tsv(x = DF_trackid_hour, na = "", col_names = T, file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'reports', 'track_id_hour.tsv'))
write_tsv(x = DF_trackid_month, na = "", col_names = T, file = file.path('Documents', 'Repositorios', 'AIRMAP', 'airmap_01_exploratoryanalysis_25112020', 'reports', 'track_id_month.tsv'))

