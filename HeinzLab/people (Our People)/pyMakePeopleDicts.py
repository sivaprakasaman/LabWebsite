root = container.getRoot()
primary_group_id = int(container.plPrimaryGroupId()[0])
people_dicts = []
keys = []

if group_id and not same_type(group_id, 0):
  group_id = int(group_id)

if resource_id and not same_type(resource_id, 0):
  resource_id = int(resource_id)

if not group_id:
  group_id = primary_group_id
  
if not order_by or order_by == 'None':
  order_by = "m.custom_sort_order, m.last_name, m.first_name"
  
if resource_id and not all_records:
  people = container.sqlGetPeople(group_id=group_id, resource_id=resource_id).dictionaries()
elif resource_id and all_records:
  people = container.sqlGetPeople(resource_id=resource_id).dictionaries()
else:
  people = container.sqlGetPeople(group_id=group_id, order_by=order_by).dictionaries()

if people:

  if not same_type(people, []):
    people = [people]

  parts = root.ResourceDB.pyGetResourceTypeParts(group_id=primary_group_id, resource_type_id=1001)
  for part in parts:
    # print '%s, %s, id: %s<br>' % (part.name, part.part_type, part.part_id)
    key_dict = {'name':part.name.upper(), 'clob':False}
    if part.part_type == 'large text':
      key_dict['clob'] = True
    keys.append(key_dict)
  keys.append({'name':'RESOURCE_ID', 'clob':False})
      
  for person in people:
  
    person_dict = {}
    
    for key in keys:
      key_name = key['name']
      if key_name in person.keys():
        key_value = person[key_name]
        if key['clob'] and key_value:
          clob_id = int(key_value)
          person_dict[key_name.lower()] = root.ResourceDB.pyGetCLOB(clob_id=clob_id)
        else:
          person_dict[key_name.lower()] = key_value
      
    people_dicts.append(person_dict)
  
return people_dicts
