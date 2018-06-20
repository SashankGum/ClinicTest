with x as (select npi_id,zip1,type
		  from addresses where zip1 = '14623' and type = 'practice'),
		  y as (select tref.id,tref.name,tg.npi_id,tg.code
		  from taxonomies as tg, taxonomiesref as tref
		  where tg.code = tref.id and tref.name = 'Dermatology')
select count(x.npi_id)
from x,y
where x.npi_id = y.npi_id