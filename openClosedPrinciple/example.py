from app import GetNews

o_globo = GetNews(name='oglobo', 
                  url='http://globo.com', 
                  types=[['Principal','hui-premium__title'],['Secundário','hui-highlight-title']])
o_globo.write_on_csv()
