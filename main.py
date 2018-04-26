#from waveform import Waveform
from database import Database

with Database() as db:
    db.update()
    #db._check_table_stock()
    #sql = 'desc trade'
    #print(db.execute(sql))
    #db._check_table_company()


#quit()
#form = Waveform()
#form.mainloop()