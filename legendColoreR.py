def AshrafColoreR():
    import pandas as pd
    filename= ('legend.table')
    df_Phylum = pd.read_csv(filename,names=['A','B'],sep=' ',header=None)
    with open('legend_Color.r','w') as hndl:
    #     i=0
        hndl.write('colorslm=colorRampPalette(c(')
    #     hndl.write('colors')
        for i in df_Phylum.index:
            hndl.write(df_Phylum.at[i,'A']+'('+str(df_Phylum.at[i,'B'])+'),')
    #     hndl.write('))')
    with open('legend_Color.r','r') as hndl:
        data = hndl.readlines()
    data = str(data)
    data = data[2:-4]
    with open('legend_Color.r','w') as hndl:
        hndl.write(data+')))')
AshrafColoreR()

