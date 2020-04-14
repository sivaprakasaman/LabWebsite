select
  group_id,
  short_name,
  name,
  parent_id,
  comments,
  url,
  primary
from
  ecnweb.rdb_group_information

<dtml-sqlgroup where>
  <dtml-sqltest group_id type="int" multiple optional>
<dtml-or>
  <dtml-sqltest parent_id type="int" multiple optional>
</dtml-sqlgroup>

order by name