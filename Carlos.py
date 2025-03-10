import pandas as pd
import os
import json as js
import numpy as np
def cargar_dataset(archivo):
    import pandas as pd
    import os
    import json as js
    import numpy as np
    extension = os.path.splitext(archivo)[1].lower()
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    else:
            raise ValueError(f"Este formato no está soportado para esta función: {extension}")


#string concreto
def sustitucion_string_concreto(dataframe, cols):  
    import pandas as pd
    import os
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "object") | (data_type == "category"):  
            dataframe[col] = dataframe[col].fillna("Este_es_un_valor_nulo")
    return dataframe  

#sustitucion con numero constante
def sustitucion_constante(dataframe, cols):  
    import pandas as pd
    import os
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            dataframe[col] = dataframe[col].fillna(99)
    return dataframe

    

def cuenta_valores_nulos(dataframe):
    import pandas as pd
    import os
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()

    return("Valores nulos por columna", valores_nulos_cols,
           "Valores nulos por dataframe", valores_nulos_df)

#sustitucion de outliers
def sustituir_outliers_iqr(dataframe, columnas):
    import pandas as pd
    import os
    for columna in columnas:
        data1 = dataframe.fillna(method="bfill")
        data1 = dataframe.fillna(method="ffill")
        data1
        cuantitativas = data1.select_dtypes(include=['float64', 'int64', 'float', 'int'])
        cualitativas = data1.select_dtypes(include=['object','datetime','category'])
        y = cuantitativas
        percentiles25 = y.quantile(0.25) #Q1 medida estandar del 25%
        percentiles75 = y.quantile(0.75) #Q2 medida estandar que toma encuenta la suma de los demas 25% de los cuantiles
        iqr = percentiles75 - percentiles25

        limite_superior_iqr = percentiles75 + 1.5*iqr
        limite_inferior_iqr = percentiles25 - 1.5*iqr
        print("limite superior permitido ", limite_superior_iqr)
        print("limite inferior permitido "), limite_inferior_iqr

        data3_iqr = cuantitativas[(y<=limite_superior_iqr)&(y>=limite_inferior_iqr)]
        data3_iqr
        data4_iqr=data3_iqr.copy()
        data4_iqr=data4_iqr.fillna(round(data3_iqr.mean(),1))
        data4_iqr
        datos_limpios = pd.concat([cualitativas, data4_iqr], axis=1)
        datos_limpios
    
    return dataframe