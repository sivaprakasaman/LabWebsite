first_name = person.get('first_name', '')
middle_name = person.get('middle_name', '')
last_name = person.get('last_name', '')
name = ''
 
if first_name:
  name = name + first_name

if middle_name:
  name = name + ' ' + middle_name

if last_name:
  name = name + ' <strong>%s</strong>' % last_name

return name
