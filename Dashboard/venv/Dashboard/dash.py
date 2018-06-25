from flask import Flask,render_template
from dbcon import getCon
from flask import url_for

hostname = 'localhost'
username = 'postgres'
password = 'pass@123'
database = 'Test'

app = Flask(__name__)


def doQuery( conn ) :
    cur = conn.cursor()
    """
    res = []
    cur.execute( "SELECT zip, city FROM zipcodes limit 2" )
    for zip, city in cur.fetchall() :
        temp = [zip,city]
        res.append(temp)
    print(res)
    """
    cur.execute("with x as (select npi_id from addresses where zip1 = '14618' and type = 'practice'), y as (select tref.name,tg.npi_id from taxonomies as tg, taxonomiesref as tref where tg.code = tref.id and tg.is_primary = 'Y' and tg.code like '20%') select row_to_json(r) from (select name from x,y where x.npi_id = y.npi_id)r")
    res = cur.fetchall()
    cur.execute("select * from national_avg")
    nat_avg = cur.fetchall()
    return res,nat_avg

@app.route('/',methods=['GET'])
def index():
	x = getCon()
	result, nat_avg= doQuery(x)
	x.close()
	return render_template('home.html', results = result,national_avg=nat_avg)

if __name__=="__main__":
	app.run(debug = True)
