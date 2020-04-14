select
  m.photo,
  m.resource_id,
  m.group_id,
  g.primary,
  g.parent_id group_parent_id,
  g.name group_name
  
from 
  ecnweb.rdb_master m,
  ecnweb.rdb_group_information g

<dtml-sqlgroup where>
  m.group_id = g.group_id and
  m.resource_type_id = 1001 
<dtml-and>
  <dtml-sqltest resource_id column="m.resource_id" type="int" optional>
<dtml-and>
  <dtml-sqltest group_id column="g.group_id" type="int" optional>
</dtml-sqlgroup>

order by
  g.primary desc, m.group_id