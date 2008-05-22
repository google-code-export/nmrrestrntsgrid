-- Find viable entries for RECOORD. Just one criteria.
select e.pdb_id from entry e
where e.pdb_id IN (
   select f.pdb_id from `mrblock` m, mrfile f
   where m.mrfile_id = f.mrfile_id AND
   m.text_type = '2-parsed'  AND (
   m.type = 'distance' OR
   m.type = 'dihedral angle' OR
   m.type = 'dipolar'
   )
)

-- Find doubly counted entries. 
create table virtual_table AS
select b.text_type, f.pdb_id, b.item_count from `mrblock` b, mrfile f
where f.mrfile_id=b.mrfile_id AND
( b.text_type like "3%" OR b.text_type like "4%" ) AND
b.subtype = "full" AND b.program="STAR" 

select *, (v2.item_count - v1.item_count) AS d from `virtual_table` v1, `virtual_table` v2
where v1.pdb_id=v2.pdb_id AND
v1.text_type LIKE "3%" AND
v2.text_type LIKE "4%" AND
v1.item_count < v2.item_count
order by v1.pdb_id ASC

-- find entries in db but not having "2-parsed 	STAR 	entry 	full" Used to be 1 on 7/21/06
-- These might very well be obsoleted entries like 1nj7 or amber entry that failed to be done right.
select e.pdb_id from entry e
where e.pdb_id NOT IN (
   select f.pdb_id from `mrblock` m, mrfile f
   where m.mrfile_id = f.mrfile_id AND
   m.text_type LIKE '4%'  AND 
   m.program = 'STAR' AND
   m.type = 'entry' AND
   m.subtype = 'full' AND
   m.format = 'n/a'
)

delete from entry e
where e.pdb_id = '1nj7'
 

-- get entries that aren't in FRED yet at a certain cutoff
select distinct pdb_id from mrfile 
where detail like '1%' AND
pdb_id not in (
    select distinct f.pdb_id from mrfile f
    where f.detail like '4%'
) AND
pdb_id != '9'
order by pdb_id
