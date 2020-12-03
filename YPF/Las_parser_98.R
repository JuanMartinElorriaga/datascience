#Parseo de archivos .las de un directorio para leer el nombre de pozo y la tabla de datos y cargar todo a un dataframe

las_path   <- 'C:\\Users\\SE31886\\Documents\\Prediccion_MN\\Big Data Exported Files'

#Obtengo la lista de archivos en el directorio
FILE_NAMES<-list.files(las_path,pattern="*.las", recursive=FALSE)

#FILE_NAMES<-'LCav-21.las'

#PARA CADA ARCHIVO EN EL DIRECTORIO
primera_vez=1
for (archivo in FILE_NAMES) {
  #leo las lineas de cada archivo
  RAW_LINES<-readLines(paste(las_path,archivo,sep='/'))
  RAW_LINES<-toupper(RAW_LINES)
  
  
  #Busco la linea donde dice el nombre de pozo y la proceso
  WELL_NAME_ROW <- which(grepl(pattern = "*: WELL NAME",x =RAW_LINES))[1]
  #Quitar de la linea el principio y fin para luego hacer trim y obtener el nombre del pozo
  WELL_NAME<-gsub(":AME","",gsub("WELL.","",gsub(" ","",RAW_LINES[WELL_NAME_ROW])))
  
  #Busco la linea donde empieza la tabla. La que contiene los nombres de columna.
  DATA_NAMES_ROW<-which(grepl(pattern = "~A",x = RAW_LINES))
  #Limpio la fila de nombres de columna y los preparo para el split
  RAW_LINES[DATA_NAMES_ROW]<-gsub("\\s+", "|", trimws(gsub("~","",gsub("~A","",RAW_LINES[DATA_NAMES_ROW]))), perl = TRUE)
  
  #preparo las filas de datos para el split
  FIRST_ROW<-DATA_NAMES_ROW+1
  LAST_ROW<-length(RAW_LINES)
  RAW_LINES[FIRST_ROW:LAST_ROW]<-gsub("\\s+", "|",trimws(RAW_LINES[FIRST_ROW:LAST_ROW]))
  
  #Armo el dataframe
  DATA_TEMP_df<-data.frame(do.call(rbind, strsplit(RAW_LINES[FIRST_ROW:LAST_ROW], "|", fixed=TRUE)),stringsAsFactors = FALSE)
  colnames(DATA_TEMP_df)<-strsplit(RAW_LINES[DATA_NAMES_ROW], "|", fixed=TRUE)[[1]]
  #Convierto las columnas a numericas
  DATA_TEMP_df[] <- lapply(DATA_TEMP_df, function(x) as.numeric(as.character(x)))
  DATA_TEMP_df$WELL=WELL_NAME
  
  
  #DATA FRAME FINAL
  if (primera_vez==1) 
  {
    DATA_df<-data.frame(WELL=DATA_TEMP_df$WELL,DEPTH=DATA_TEMP_df$DEPTH,AT90=DATA_TEMP_df$DRES,RO=DATA_TEMP_df$RO)
    primera_vez=0
  } 
  else 
  {DATA_df<-rbind(DATA_df,data.frame(WELL=DATA_TEMP_df$WELL,DEPTH=DATA_TEMP_df$DEPTH,AT90=DATA_TEMP_df$DRES,RO=DATA_TEMP_df$RO))
  }
}


#POZOS<-as.character(unique(DATA_df$WELL))
#POZOS
rm(DATA_TEMP_df)
