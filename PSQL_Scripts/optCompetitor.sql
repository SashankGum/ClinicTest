with x as (select ad.npi_id,ad.zip1,ad.type
		  from addresses as ad),
		  y as (select tref.id,tref.name,tg.npi_id,tg.code
		  from taxonomies as tg, taxonomiesref as tref
		  where tg.code = tref.id and tref.name = 'Dermatology')
select count(x.npi_id)
from x,y
where x.npi_id = y.npi_id and x.zip1 = '14623' and x.type = 'practice'