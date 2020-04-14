select
  m.qualified_name,
  m.last_name,
  m.middle_name,
  m.first_name,
  m.suffix,
  m.custom_sort_order,
  m.photo,
  m.classification,
  m.faculty_rank,
  m.building,
  m.office,
  m.office_phone,
  m.url,
  m.alias,
  m.email,
  m.title,
  m.school,
  m.department,
  m.campus,
  m.biography,
  m.bio,
  m.committee_term_end,
  m.committee_role,
  m.appointment_term,
  m.notes,
  m.profile_content,
  m.cv,
  m.resource_id,
  m.group_id,
  g.primary,
  g.parent_id group_parent_id,
  g.short_name group_short_name,
  g.name group_name,
  g.url group_url,
  g.profile_url profile_url,
  g.comments group_comments
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
  <dtml-var order_by>