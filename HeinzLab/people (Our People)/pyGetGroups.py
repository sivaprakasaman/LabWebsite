if group_id is None and parent_id is None:
  parent_id = 10860

group_data = []

if parent_id:
  group_data = group_data + list(container.sqlGetGroups(parent_id=parent_id))

if group_id:
  group_data = group_data + list(container.sqlGetGroups(group_id=group_id))

if not (group_id or parent_id):
  return

groups = []
for group in group_data:
  groups.append({
    'group_id':group.group_id,
    'name':group.name,
    'short_name':group.short_name,
    'parent_id':group.parent_id,
    'comments':group.comments,
    'url':group.url,
    'primary':group.primary,
    'sub_groups':container.pyGetGroups(parent_id=group.group_id)
  })

def groupSort(a,b):
  a_alternate = a['name'].lower().find('alternate') >= 0
  b_alternate = b['name'].lower().find('alternate') >= 0

  if a_alternate and not b_alternate:
    return 1
  elif b_alternate and not a_alternate:
    return -1
  else:
    return cmp(a['name'],b['name'])

groups.sort(groupSort)

if reverse:
  groups.reverse()

return groups
