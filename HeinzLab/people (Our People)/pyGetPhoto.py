photo = None

if person:
  photo = person['photo']

if not photo:

  if person:
    resource_id = int(person['resource_id'])
  elif resource_id and not same_type(resource_id, 0):
    resource_id = int(resource_id)  
    
  if resource_id:
    
    all_records = container.sqlGetPhotos(resource_id=resource_id)
    
    for record in all_records:
      if record['photo']:
        photo = record['photo']
        break
  
if photo:
  return container.restrictedTraverse('/ResourceDB/ResourceFiles/%s' % photo)
