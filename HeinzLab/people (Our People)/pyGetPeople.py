if resource_id:
    
  # if only one person was requested, return only a single dictionary, not a list
  person = container.pyMakePeopleDicts(group_id=group_id, resource_id=resource_id)[0]
  
  # Get the actual photo object, and look for a photo if one wasn't found in the group
  person['photo'] = container.pyGetPhoto(person=person)

  if photo_only:
    return person['photo']
  
  return person

else:
    
  people = container.pyMakePeopleDicts(group_id=group_id, order_by=order_by)
  
  for person in people:
    # Get the actual photo object, and look for a photo if one wasn't found in the group
    person['photo'] = container.pyGetPhoto(person=person)
  
  return people
